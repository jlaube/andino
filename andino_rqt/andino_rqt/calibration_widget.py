import os
import math

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from python_qt_binding import loadUi
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSlot
from ament_index_python.resources import get_resource
from PyQt5.QtCore import Qt, pyqtSlot
from rosidl_runtime_py.utilities import get_message
from rqt_py_common.topic_completer import TopicCompleter
from .andino_cfg_reader import *


class CalibrationWidget(QWidget):
    def __init__(self, node):
        super(CalibrationWidget, self).__init__()
        self.setObjectName('Calibration_widget')
        _, package_path = get_resource('packages', 'andino_rqt')
        ui_file = os.path.join(package_path, 'share', 'andino_rqt', 'resource', 'andino_calibrate.ui')
        loadUi(ui_file, self)
        self.node = node
        self.stop_when = 0.0

        # Config reader
        cfg_reader = AndinoConfigReader(node)
        self.wheel_radius_m.setText(cfg_reader.readWheelRadius())
        self.speed = 0.0

        # Odometry reader
        self.odom_sub = self.node.create_subscription(Odometry, '/diff_controller/odom', self.odom_callback, 10)

        # Andino comander
        self.comander = self.node.create_publisher(Twist, '/diff_controller/cmd_vel_unstamped', 10)

        # Signals
        self.btnRun.pressed.connect(self.runCalibration)
        self.btnCalculate.pressed.connect(self.calculateCalibration)

        self.timer = None

    @pyqtSlot()
    def runCalibration(self):
        self.stop_when = float(self.distance_m.text()) + float(self.odometry_x_m.text())
        self.speed = 1.0
        self.timer = self.node.create_timer(0.05, self.timer_callback)

    def calculateIdealRadius(self, distance, real_distance, wheel_radius=0.035):
        if distance == 0:
            return -1
        return real_distance * wheel_radius / distance

    @pyqtSlot()
    def calculateCalibration(self):
        calculated_radius = self.calculateIdealRadius(float(self.distance_m.text()), float(self.real_distance_m.text()), float(self.wheel_radius_m.text()))
        self.computed_wheel_radius_m.setText(str(round(calculated_radius, 3)))

    def odom_callback(self, msg):
        self.odometry_x_m.setText(str(round(msg.pose.pose.position.x, 2)))
        self.odometry_y_m.setText(str(round(msg.pose.pose.position.y, 2)))
        self.odometry_z_m.setText(str(round(msg.pose.pose.position.z, 2)))

    def timer_callback(self):
        current_pos = float(self.odometry_x_m.text())
        msg = Twist()

        self.node.get_logger().info("current_pos: " + self.odometry_x_m.text() + " self.stop_when: " + str(self.stop_when))
        if (abs(current_pos - self.stop_when) <= 0.03):
            # Publish speed 0
            self.speed = 0.0
            self.timer.cancel()
            self.timer.destroy()
            self.node.get_logger().info("timer cancelled")


        msg.linear.x = self.speed
        self.comander.publish(msg)

