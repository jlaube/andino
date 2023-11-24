import os

from nav_msgs.msg import Odometry
from python_qt_binding import loadUi
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSlot
from ament_index_python.resources import get_resource
from PyQt5.QtCore import Qt, pyqtSlot
from rosidl_runtime_py.utilities import get_message
from rqt_py_common.topic_completer import TopicCompleter


class CalibrationWidget(QWidget):
    def __init__(self, node):
        super(CalibrationWidget, self).__init__()
        self.setObjectName('Calibration_widget')
        _, package_path = get_resource('packages', 'andino_rqt')
        ui_file = os.path.join(package_path, 'share', 'andino_rqt', 'resource', 'andino_calibrate.ui')
        loadUi(ui_file, self)
        self.node = node

        # Odometry reader
        self.odom_sub = self.node.create_subscription(Odometry, '/diff_controller/odom', self.odom_callback, 10)

        # Config reader

        # Signals
        self.btnRun.pressed.connect(self.runCalibration)

    @pyqtSlot()
    def runCalibration(self):
        self.real_distance_m.setText("1.3")
    
    def odom_callback(self, msg):
        self.odometry_x_m.setText(str(round(msg.pose.pose.position.x, 2)))
        self.odometry_y_m.setText(str(round(msg.pose.pose.position.y, 2)))
        self.odometry_z_m.setText(str(round(msg.pose.pose.position.z, 2)))

