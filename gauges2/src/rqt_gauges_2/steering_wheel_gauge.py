import math

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient, QRadialGradient, QBrush
from PyQt5.QtCore import Qt, QPoint, QPointF, QObject, QRect

class SteeringWheelGauge(QWidget):
    # This class creates a gauge object that contains several elements such as a needle, big and small scales
    # and different circles painted with different colors to look like a car Speedometer. It has the ability to
    # modify the minimum and maximum values of the gauge and the units the numbers are displaying. The class contains
    # methods used to modify the values explained before, the marked number of the gauge and the whole design as well.

    def __init__(self, parent=None):
        # Constructor method of the class, initializes all the variables needed to create the gauge.

        super(SteeringWheelGauge, self).__init__(parent)

        self.value = 0
        self.width = 400
        self.height = 400
        self.progress_width = 25
        self.progress_rounded_cap = True
        self.progress_color = 0x39F030
        self.max_value = 45
        self.circle_max_angle = 135
        self.font_size = 40
        self.scale_font_size = 15
        self.font_family = "Verdana"
        self.suffix = "°"
        self.text_color = 0x000000
        self.enable_shadow = True

        self.angle_offset = 0
        self.minValue = -45
        self.maxValue = 45

        self.widget_diameter = min(self.width, self.height)
        self.resize(self.width, self.height)

        self.scale_line_outer_start = (self.widget_diameter)/2
        self.scale_line_length = (self.widget_diameter / 2) - (self.widget_diameter / 20)

        self.text_radius_factor = 0.75
        self.text_radius = self.widget_diameter/2 * self.text_radius_factor


    def draw_big_scaled_marker(self, start_angle_value: int, angle_size: int, scala_count: int):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width / 2, self.height / 2)

        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.rotate(start_angle_value - self.angle_offset)
        steps_size = (float(angle_size) / float(scala_count))
        
        for _ in range(scala_count+1):
            painter.drawLine(self.scale_line_length, 0, self.scale_line_outer_start, 0)
            painter.rotate(steps_size)
        painter.end()

    def create_scale_marker_values_text(self, scale_angle_start_value: int, scale_angle_size: int, scalaCount: int):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.translate(self.width / 2, self.height / 2)
        font = QFont(self.font_family, self.scale_font_size, QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()
        pen_shadow.setBrush(QColor(0, 0, 0, 255))
        painter.setPen(pen_shadow)

        scale_per_div = int((self.maxValue - self.minValue) / scalaCount)

        angle_distance = (float(scale_angle_size) / float(scalaCount))
        for i in range(scalaCount + 1):
            text = str(int(self.minValue + scale_per_div * i))
            w = fm.width(text) + 1
            h = fm.height()
            painter.setFont(QFont(self.font_family, self.scale_font_size))
            angle = angle_distance * i + float(scale_angle_start_value - self.angle_offset)
            x = self.text_radius * math.cos(math.radians(angle))
            y = self.text_radius * math.sin(math.radians(angle))

            text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
        painter.end()

    def updateValue(self, value: float):
        # Updates the value that the gauge is indicating.
        # Args: 
        #   value: Value to update the gauge with.
        value = max(value, self.minValue)
        value = min(value, self.maxValue)
        self.repaint()

    def draw_background_circle(self):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        painter.drawEllipse(0, 0, 400, 400)
        painter.end()

    def paintEvent(self, event):
        # Size variables
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * self.circle_max_angle / self.max_value

        # Draw Circle
        self.draw_background_circle()

        # Painter
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(QFont(self.font_family, self.font_size))

        # Rectangle
        rect = QRect(0, 0, self.width, self.height)
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

        # Pen to draw progress bar
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Create Arc
        painter.setPen(pen)
        painter.drawArc(margin, margin, width, height, 90 * 16, -value * 16)

        # Create Gauge Text
        pen.setColor(QColor(self.text_color))
        painter.setPen(pen)
        painter.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # End Painter
        painter.end()

        self.draw_big_scaled_marker(131, 278, 5)
        self.create_scale_marker_values_text(131, 278, 5)
        