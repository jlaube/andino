# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'andino_calibrateRdmIcs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CalibrationUI(object):
    def setupUi(self, CalibrationUI):
        if not CalibrationUI.objectName():
            CalibrationUI.setObjectName(u"CalibrationUI")
        CalibrationUI.setWindowModality(Qt.NonModal)
        CalibrationUI.resize(920, 578)
        CalibrationUI.setAutoFillBackground(False)
        self.min_value_label = QLabel(CalibrationUI)
        self.min_value_label.setObjectName(u"min_value_label")
        self.min_value_label.setGeometry(QRect(450, 70, 131, 31))
        font = QFont()
        font.setPointSize(12)
        self.min_value_label.setFont(font)
        self.real_distance = QTextEdit(CalibrationUI)
        self.real_distance.setObjectName(u"real_distance")
        self.real_distance.setGeometry(QRect(580, 70, 51, 31))
        self.computed_wheel_radius = QTextEdit(CalibrationUI)
        self.computed_wheel_radius.setObjectName(u"computed_wheel_radius")
        self.computed_wheel_radius.setGeometry(QRect(670, 110, 51, 31))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        self.computed_wheel_radius.setFont(font1)
        self.max_value_label = QLabel(CalibrationUI)
        self.max_value_label.setObjectName(u"max_value_label")
        self.max_value_label.setGeometry(QRect(460, 110, 201, 21))
        self.max_value_label.setFont(font)
        self.btnRun = QPushButton(CalibrationUI)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(640, 30, 81, 31))
        self.topic_label = QLabel(CalibrationUI)
        self.topic_label.setObjectName(u"topic_label")
        self.topic_label.setGeometry(QRect(480, 36, 101, 21))
        self.topic_label.setFont(font)
        self.groupBox = QGroupBox(CalibrationUI)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 421, 301))
        self.groupBox_2 = QGroupBox(CalibrationUI)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 330, 291, 211))
        self.distance = QTextEdit(CalibrationUI)
        self.distance.setObjectName(u"distance")
        self.distance.setGeometry(QRect(580, 30, 61, 31))

        self.retranslateUi(CalibrationUI)

        QMetaObject.connectSlotsByName(CalibrationUI)
    # setupUi

    def retranslateUi(self, CalibrationUI):
        CalibrationUI.setWindowTitle(QCoreApplication.translate("CalibrationUI", u"Andino Calibration", None))
        self.min_value_label.setText(QCoreApplication.translate("CalibrationUI", u"Real distance (m):", None))
        self.real_distance.setHtml(QCoreApplication.translate("CalibrationUI", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.real_distance.setPlaceholderText("")
        self.computed_wheel_radius.setMarkdown(QCoreApplication.translate("CalibrationUI", u"0\n"
"\n"
"", None))
        self.computed_wheel_radius.setHtml(QCoreApplication.translate("CalibrationUI", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:7px; margin-bottom:7px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.computed_wheel_radius.setPlaceholderText("")
        self.max_value_label.setText(QCoreApplication.translate("CalibrationUI", u"Computed Wheel-Raius (m):", None))
        self.btnRun.setText(QCoreApplication.translate("CalibrationUI", u"Run", None))
        self.topic_label.setText(QCoreApplication.translate("CalibrationUI", u"Distance (m):", None))
        self.groupBox.setTitle(QCoreApplication.translate("CalibrationUI", u"Odometry", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CalibrationUI", u"Configuration", None))
    # retranslateUi

