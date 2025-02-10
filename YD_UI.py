# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YD_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.gridLayout_2 = QGridLayout(self.tab_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.tab_0)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setReadOnly(False)

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_0)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(280, 420))
        self.groupBox_6.setMaximumSize(QSize(280, 420))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_6.setFont(font)
        self.gridLayout_22 = QGridLayout(self.groupBox_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.frame_17 = QFrame(self.groupBox_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_axis1 = QLineEdit(self.frame_17)
        self.lineEdit_axis1.setObjectName(u"lineEdit_axis1")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.lineEdit_axis1.setFont(font1)
        self.lineEdit_axis1.setStyleSheet(u"")
        self.lineEdit_axis1.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_axis1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_axis1.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_axis1, 1, 1, 1, 1)

        self.label_24 = QLabel(self.frame_17)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_23.addWidget(self.label_24, 4, 0, 1, 1)

        self.lineEdit_axis3 = QLineEdit(self.frame_17)
        self.lineEdit_axis3.setObjectName(u"lineEdit_axis3")
        self.lineEdit_axis3.setFont(font1)
        self.lineEdit_axis3.setStyleSheet(u"")
        self.lineEdit_axis3.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_axis3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_axis3.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_axis3, 3, 1, 1, 1)

        self.lineEdit_axis2 = QLineEdit(self.frame_17)
        self.lineEdit_axis2.setObjectName(u"lineEdit_axis2")
        self.lineEdit_axis2.setFont(font1)
        self.lineEdit_axis2.setStyleSheet(u"")
        self.lineEdit_axis2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_axis2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_axis2.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_axis2, 2, 1, 1, 1)

        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_23.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_23.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_23.addWidget(self.label_25, 2, 0, 1, 1)

        self.lineEdit_axis0 = QLineEdit(self.frame_17)
        self.lineEdit_axis0.setObjectName(u"lineEdit_axis0")
        self.lineEdit_axis0.setFont(font1)
        self.lineEdit_axis0.setStyleSheet(u"")
        self.lineEdit_axis0.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_axis0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_axis0.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_axis0, 0, 1, 1, 1)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_23.addWidget(self.label_26, 3, 0, 1, 1)

        self.lineEdit_speed0 = QLineEdit(self.frame_17)
        self.lineEdit_speed0.setObjectName(u"lineEdit_speed0")
        self.lineEdit_speed0.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_speed0.setFont(font1)
        self.lineEdit_speed0.setToolTipDuration(-1)
        self.lineEdit_speed0.setStyleSheet(u"")
        self.lineEdit_speed0.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_speed0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_speed0.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_speed0, 0, 2, 1, 1)

        self.lineEdit_axis4 = QLineEdit(self.frame_17)
        self.lineEdit_axis4.setObjectName(u"lineEdit_axis4")
        self.lineEdit_axis4.setFont(font1)
        self.lineEdit_axis4.setStyleSheet(u"")
        self.lineEdit_axis4.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_axis4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_axis4.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_axis4, 4, 1, 1, 1)

        self.lineEdit_delay0 = QLineEdit(self.frame_17)
        self.lineEdit_delay0.setObjectName(u"lineEdit_delay0")
        self.lineEdit_delay0.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_delay0.setFont(font1)
        self.lineEdit_delay0.setStyleSheet(u"")
        self.lineEdit_delay0.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_delay0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay0.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_delay0, 0, 3, 1, 1)

        self.lineEdit_speed1 = QLineEdit(self.frame_17)
        self.lineEdit_speed1.setObjectName(u"lineEdit_speed1")
        self.lineEdit_speed1.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_speed1.setFont(font1)
        self.lineEdit_speed1.setToolTipDuration(-1)
        self.lineEdit_speed1.setStyleSheet(u"")
        self.lineEdit_speed1.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_speed1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_speed1.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_speed1, 1, 2, 1, 1)

        self.lineEdit_delay1 = QLineEdit(self.frame_17)
        self.lineEdit_delay1.setObjectName(u"lineEdit_delay1")
        self.lineEdit_delay1.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_delay1.setFont(font1)
        self.lineEdit_delay1.setStyleSheet(u"")
        self.lineEdit_delay1.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_delay1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay1.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_delay1, 1, 3, 1, 1)

        self.lineEdit_speed2 = QLineEdit(self.frame_17)
        self.lineEdit_speed2.setObjectName(u"lineEdit_speed2")
        self.lineEdit_speed2.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_speed2.setFont(font1)
        self.lineEdit_speed2.setToolTipDuration(-1)
        self.lineEdit_speed2.setStyleSheet(u"")
        self.lineEdit_speed2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_speed2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_speed2.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_speed2, 2, 2, 1, 1)

        self.lineEdit_delay2 = QLineEdit(self.frame_17)
        self.lineEdit_delay2.setObjectName(u"lineEdit_delay2")
        self.lineEdit_delay2.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_delay2.setFont(font1)
        self.lineEdit_delay2.setStyleSheet(u"")
        self.lineEdit_delay2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_delay2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay2.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_delay2, 2, 3, 1, 1)

        self.lineEdit_speed3 = QLineEdit(self.frame_17)
        self.lineEdit_speed3.setObjectName(u"lineEdit_speed3")
        self.lineEdit_speed3.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_speed3.setFont(font1)
        self.lineEdit_speed3.setToolTipDuration(-1)
        self.lineEdit_speed3.setStyleSheet(u"")
        self.lineEdit_speed3.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_speed3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_speed3.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_speed3, 3, 2, 1, 1)

        self.lineEdit_delay3 = QLineEdit(self.frame_17)
        self.lineEdit_delay3.setObjectName(u"lineEdit_delay3")
        self.lineEdit_delay3.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_delay3.setFont(font1)
        self.lineEdit_delay3.setStyleSheet(u"")
        self.lineEdit_delay3.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_delay3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay3.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_delay3, 3, 3, 1, 1)

        self.lineEdit_speed4 = QLineEdit(self.frame_17)
        self.lineEdit_speed4.setObjectName(u"lineEdit_speed4")
        self.lineEdit_speed4.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_speed4.setFont(font1)
        self.lineEdit_speed4.setToolTipDuration(-1)
        self.lineEdit_speed4.setStyleSheet(u"")
        self.lineEdit_speed4.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_speed4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_speed4.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_speed4, 4, 2, 1, 1)

        self.lineEdit_delay4 = QLineEdit(self.frame_17)
        self.lineEdit_delay4.setObjectName(u"lineEdit_delay4")
        self.lineEdit_delay4.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_delay4.setFont(font1)
        self.lineEdit_delay4.setStyleSheet(u"")
        self.lineEdit_delay4.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_delay4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay4.setReadOnly(False)

        self.gridLayout_23.addWidget(self.lineEdit_delay4, 4, 3, 1, 1)


        self.gridLayout_22.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_16 = QFrame(self.groupBox_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 30))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_16)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_s485_Axis_No = QLineEdit(self.frame_16)
        self.lineEdit_s485_Axis_No.setObjectName(u"lineEdit_s485_Axis_No")
        self.lineEdit_s485_Axis_No.setMinimumSize(QSize(30, 0))
        self.lineEdit_s485_Axis_No.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_s485_Axis_No.setFont(font1)
        self.lineEdit_s485_Axis_No.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.lineEdit_s485_Axis_No, 0, 3, 1, 1)

        self.checkBox_point = QCheckBox(self.frame_16)
        self.checkBox_point.setObjectName(u"checkBox_point")
        self.checkBox_point.setFont(font)

        self.gridLayout_19.addWidget(self.checkBox_point, 0, 1, 1, 1)

        self.checkBox_key = QCheckBox(self.frame_16)
        self.checkBox_key.setObjectName(u"checkBox_key")
        self.checkBox_key.setMinimumSize(QSize(90, 0))
        self.checkBox_key.setFont(font)

        self.gridLayout_19.addWidget(self.checkBox_key, 0, 0, 1, 1)

        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(40, 0))
        self.label_19.setMaximumSize(QSize(40, 16777215))
        self.label_19.setFont(font)

        self.gridLayout_19.addWidget(self.label_19, 0, 2, 1, 1)


        self.gridLayout_22.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.groupBox_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 100))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_15)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(70, 16777215))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_18)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(60, 0))
        self.label_18.setFont(font)

        self.gridLayout_21.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_18, 0, 0, 1, 1)

        self.pushButton_CardStart = QPushButton(self.frame_15)
        self.pushButton_CardStart.setObjectName(u"pushButton_CardStart")
        self.pushButton_CardStart.setMinimumSize(QSize(0, 30))
        self.pushButton_CardStart.setFont(font)
        self.pushButton_CardStart.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_CardStart.setStyleSheet(u"background:rgb(255,255,0)")

        self.gridLayout_24.addWidget(self.pushButton_CardStart, 0, 2, 1, 1)

        self.pushButton_CardStop = QPushButton(self.frame_15)
        self.pushButton_CardStop.setObjectName(u"pushButton_CardStop")
        self.pushButton_CardStop.setMinimumSize(QSize(0, 30))
        self.pushButton_CardStop.setFont(font)
        self.pushButton_CardStop.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_CardStop.setStyleSheet(u"background:rgb(255,0,0)")

        self.gridLayout_24.addWidget(self.pushButton_CardStop, 2, 0, 1, 2)

        self.pushButton_CardNext = QPushButton(self.frame_15)
        self.pushButton_CardNext.setObjectName(u"pushButton_CardNext")
        self.pushButton_CardNext.setMinimumSize(QSize(0, 30))
        self.pushButton_CardNext.setFont(font)
        self.pushButton_CardNext.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_24.addWidget(self.pushButton_CardNext, 2, 2, 1, 1)

        self.pushButton_CardRun = QPushButton(self.frame_15)
        self.pushButton_CardRun.setObjectName(u"pushButton_CardRun")
        self.pushButton_CardRun.setMinimumSize(QSize(0, 30))
        self.pushButton_CardRun.setFont(font)
        self.pushButton_CardRun.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_CardRun.setStyleSheet(u"background:rgb(0,255,0)")

        self.gridLayout_24.addWidget(self.pushButton_CardRun, 1, 0, 1, 2)

        self.lineEdit_CardNo = QLineEdit(self.frame_15)
        self.lineEdit_CardNo.setObjectName(u"lineEdit_CardNo")
        self.lineEdit_CardNo.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_CardNo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_24.addWidget(self.lineEdit_CardNo, 0, 1, 1, 1)

        self.groupBox_34 = QGroupBox(self.frame_15)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMaximumSize(QSize(16777215, 150))
        self.groupBox_34.setFont(font)
        self.gridLayout_61 = QGridLayout(self.groupBox_34)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.checkBox_shoot = QCheckBox(self.groupBox_34)
        self.checkBox_shoot.setObjectName(u"checkBox_shoot")
        self.checkBox_shoot.setFont(font)

        self.gridLayout_61.addWidget(self.checkBox_shoot, 1, 0, 1, 1)

        self.checkBox_end = QCheckBox(self.groupBox_34)
        self.checkBox_end.setObjectName(u"checkBox_end")
        self.checkBox_end.setFont(font)
        self.checkBox_end.setChecked(False)

        self.gridLayout_61.addWidget(self.checkBox_end, 1, 2, 1, 1)

        self.checkBox_start = QCheckBox(self.groupBox_34)
        self.checkBox_start.setObjectName(u"checkBox_start")
        self.checkBox_start.setFont(font)
        self.checkBox_start.setChecked(False)

        self.gridLayout_61.addWidget(self.checkBox_start, 1, 1, 1, 1)

        self.lineEdit_OutNo = QLineEdit(self.groupBox_34)
        self.lineEdit_OutNo.setObjectName(u"lineEdit_OutNo")
        self.lineEdit_OutNo.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_OutNo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_61.addWidget(self.lineEdit_OutNo, 2, 1, 1, 1)

        self.label_78 = QLabel(self.groupBox_34)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(60, 0))
        self.label_78.setFont(font)

        self.gridLayout_61.addWidget(self.label_78, 2, 0, 1, 1)

        self.checkBox_switch = QCheckBox(self.groupBox_34)
        self.checkBox_switch.setObjectName(u"checkBox_switch")
        self.checkBox_switch.setFont(font)

        self.gridLayout_61.addWidget(self.checkBox_switch, 2, 2, 1, 1)

        self.pushButton_CardCloseAll = QPushButton(self.groupBox_34)
        self.pushButton_CardCloseAll.setObjectName(u"pushButton_CardCloseAll")
        self.pushButton_CardCloseAll.setMinimumSize(QSize(0, 50))
        self.pushButton_CardCloseAll.setFont(font)
        self.pushButton_CardCloseAll.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_61.addWidget(self.pushButton_CardCloseAll, 1, 3, 2, 1)


        self.gridLayout_24.addWidget(self.groupBox_34, 3, 0, 1, 3)

        self.pushButton_CardReset = QPushButton(self.frame_15)
        self.pushButton_CardReset.setObjectName(u"pushButton_CardReset")
        self.pushButton_CardReset.setMinimumSize(QSize(0, 30))
        self.pushButton_CardReset.setFont(font)
        self.pushButton_CardReset.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_24.addWidget(self.pushButton_CardReset, 1, 2, 1, 1)


        self.gridLayout_22.addWidget(self.frame_15, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_3 = QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_17 = QGroupBox(self.tab_1)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(0, 0))
        self.groupBox_17.setMaximumSize(QSize(600, 100))
        self.groupBox_17.setFont(font)
        self.gridLayout_35 = QGridLayout(self.groupBox_17)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_79 = QLabel(self.groupBox_17)
        self.label_79.setObjectName(u"label_79")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_79.setFont(font2)

        self.gridLayout_35.addWidget(self.label_79, 2, 0, 1, 1)

        self.lineEdit_five_axis = QLineEdit(self.groupBox_17)
        self.lineEdit_five_axis.setObjectName(u"lineEdit_five_axis")
        self.lineEdit_five_axis.setFont(font1)

        self.gridLayout_35.addWidget(self.lineEdit_five_axis, 2, 1, 1, 1)

        self.label_81 = QLabel(self.groupBox_17)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font2)

        self.gridLayout_35.addWidget(self.label_81, 3, 0, 1, 1)

        self.lineEdit_five_key = QLineEdit(self.groupBox_17)
        self.lineEdit_five_key.setObjectName(u"lineEdit_five_key")
        self.lineEdit_five_key.setFont(font1)

        self.gridLayout_35.addWidget(self.lineEdit_five_key, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.tab_1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_3.addWidget(self.frame_12, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_CardStart.setDefault(True)
        self.pushButton_CardStop.setDefault(True)
        self.pushButton_CardNext.setDefault(True)
        self.pushButton_CardRun.setDefault(True)
        self.pushButton_CardCloseAll.setDefault(True)
        self.pushButton_CardReset.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361", None))
        self.lineEdit_axis1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8f745\uff1a", None))
        self.lineEdit_axis3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_axis2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8f742\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u8f741\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8f743\uff1a", None))
        self.lineEdit_axis0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u8f744\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_speed0.setToolTip(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_speed0.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_speed0.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_speed0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
        self.lineEdit_axis4.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay0.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(\u79d2)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_delay0.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_delay0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_delay0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_speed1.setToolTip(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_speed1.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_speed1.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_speed1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay1.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(\u79d2)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_delay1.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_delay1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_delay1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_speed2.setToolTip(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_speed2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_speed2.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_speed2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay2.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(\u79d2)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_delay2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_delay2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_delay2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_speed3.setToolTip(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_speed3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_speed3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_speed3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay3.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(\u79d2)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_delay3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_delay3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_delay3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_speed4.setToolTip(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_speed4.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_speed4.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_speed4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay4.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(\u79d2)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_delay4.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_delay4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_delay4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
        self.lineEdit_s485_Axis_No.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.checkBox_point.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u8fd0\u52a8", None))
        self.checkBox_key.setText(QCoreApplication.translate("MainWindow", u"\u952e\u76d8\u5b9a\u4f4d", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361\u53f7\uff1a", None))
        self.pushButton_CardStart.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u8fd0\u52a8\u5361", None))
        self.pushButton_CardStop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_CardNext.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u52a8\u4f5c", None))
        self.pushButton_CardRun.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5f00\u542f", None))
        self.lineEdit_CardNo.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"\u673a\u5173\u64cd\u4f5c", None))
        self.checkBox_shoot.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u5c04", None))
        self.checkBox_end.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u70b9", None))
        self.checkBox_start.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u70b9", None))
        self.lineEdit_OutNo.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u53f7\uff1a", None))
        self.checkBox_switch.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5173", None))
        self.pushButton_CardCloseAll.setText(QCoreApplication.translate("MainWindow", u"\u5173\u5168\u90e8", None))
        self.pushButton_CardReset.setText(QCoreApplication.translate("MainWindow", u"\u8f74\u590d\u4f4d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u4e94\u8f74\u65b9\u5411\u8bbe\u7f6e", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361\u4e94\u8f74\u65b9\u5411\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_five_axis.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_five_axis.setText(QCoreApplication.translate("MainWindow", u"[-1,1,1,1,-1]", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u952e\u76d8\u65b9\u5411\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_five_key.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_five_key.setText(QCoreApplication.translate("MainWindow", u"[-1,1,1,1,-1]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

