# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{border:none}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_left = QFrame(self.centralwidget)
        self.fr_left.setObjectName(u"fr_left")
        self.fr_left.setMinimumSize(QSize(240, 0))
        self.fr_left.setMaximumSize(QSize(240, 16777215))
        self.fr_left.setStyleSheet(u"*{border: none}\n"
"\n"
"QFrame{\n"
"background-color: #22222C;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #8e8f93;\n"
"    font-family: \"Calibri\";\n"
"    font-size: 10pt;\n"
"    font-weight: bold;   \n"
"    line-height: 29px;\n"
"    letter-spacing: 1px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #f2f2f2;\n"
"    text-align: left;    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover#bt_0{\n"
"    icon: url(:/img/icon_light/home.svg);\n"
"}\n"
"\n"
"QPushButton:hover#bt_1{\n"
"    icon: url(:/img/icon_light/book.svg);\n"
"}\n"
"\n"
"QPushButton:hover#bt_2{\n"
"    icon: url(:/img/icon_light/bar-chart-2.svg);\n"
"}\n"
"\n"
"QPushButton:hover#bt_3{\n"
"    icon: url(:/img/icon_light/settings.svg);\n"
"}\n"
"\n"
"QPushButton:hover#bt_4{\n"
"    icon: url(:/img/icon_light/bell.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #8e8f93;\n"
"    text-align: left;    \n"
"}\n"
"\n"
"QPushButton:pressed#bt_0{\n"
"    icon: url(:/img/icon_gray/home.svg);\n"
"}\n"
"\n"
"QPushButton:pressed#bt_"
                        "1{\n"
"    icon: url(:/img/icon_gray/book.svg);\n"
"}\n"
"\n"
"QPushButton:pressed#bt_2{\n"
"    icon: url(:/img/icon_gray/bar-chart-2.svg);\n"
"}\n"
"\n"
"QPushButton:pressed#bt_3{\n"
"    icon: url(:/img/icon_gray/settings.svg);\n"
"}\n"
"\n"
"QPushButton:pressed#bt_4{\n"
"    icon: url(:/img/icon_gray/bell.svg);\n"
"}")
        self.fr_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_left.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_left)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 30)
        self.fr_side = QFrame(self.fr_left)
        self.fr_side.setObjectName(u"fr_side")
        self.fr_side.setMinimumSize(QSize(0, 0))
        self.fr_side.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_side.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.fr_side)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(65)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setContentsMargins(30, 50, 15, 60)
        self.bt_0 = QPushButton(self.fr_side)
        self.bt_0.setObjectName(u"bt_0")
        icon = QIcon()
        icon.addFile(u":/img/icon_gray/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_0.setIcon(icon)
        self.bt_0.setIconSize(QSize(14, 14))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.bt_0)

        self.bt_1 = QPushButton(self.fr_side)
        self.bt_1.setObjectName(u"bt_1")
        icon1 = QIcon()
        icon1.addFile(u":/img/icon_gray/book.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_1.setIcon(icon1)
        self.bt_1.setIconSize(QSize(14, 14))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.bt_1)

        self.bt_2 = QPushButton(self.fr_side)
        self.bt_2.setObjectName(u"bt_2")
        icon2 = QIcon()
        icon2.addFile(u":/img/icon_gray/bar-chart-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_2.setIcon(icon2)
        self.bt_2.setIconSize(QSize(14, 14))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.bt_2)

        self.bt_4 = QPushButton(self.fr_side)
        self.bt_4.setObjectName(u"bt_4")
        icon3 = QIcon()
        icon3.addFile(u":/img/icon_gray/bell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_4.setIcon(icon3)
        self.bt_4.setIconSize(QSize(14, 14))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.bt_4)

        self.label_3 = QLabel(self.fr_side)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: #f2f2f2;\n"
"    font-size: 10pt;\n"
"    letter-spacing: 0px;\n"
"    font-family: \"Roboto\";\n"
"    font-weight: Normal;   \n"
"    text-align: center;\n"
"	border-radius: 8px;\n"
"	background-color: #7672FB;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.label_3)

        self.bt_3 = QPushButton(self.fr_side)
        self.bt_3.setObjectName(u"bt_3")
        icon4 = QIcon()
        icon4.addFile(u":/img/icon_gray/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_3.setIcon(icon4)
        self.bt_3.setIconSize(QSize(14, 14))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.bt_3)


        self.verticalLayout_2.addWidget(self.fr_side)

        self.verticalSpacer = QSpacerItem(20, 379, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.fr_left)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/img/icon_light/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.fr_left)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #f2f2f2;\n"
"    font-size: 13pt;\n"
"    letter-spacing: 1px;\n"
"    font-family: \"Calibri\";\n"
"    font-weight: Bold;   \n"
"    text-align: center;\n"
"}")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.fr_left)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"    color: #8e8f93;\n"
"    font-family: \"Calibri\";\n"
"    font-size: 10pt;\n"
"    font-weight: Normal;   \n"
"    line-height: 29px;\n"
"    letter-spacing: 0px;\n"
"    text-align: left;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.bt_5 = QPushButton(self.fr_left)
        self.bt_5.setObjectName(u"bt_5")
        self.bt_5.setMinimumSize(QSize(185, 40))
        self.bt_5.setMaximumSize(QSize(16777215, 16777215))
        self.bt_5.setStyleSheet(u"QPushButton{\n"
"	color: #f2f2f2;\n"
"    font-size: 10pt;\n"
"    letter-spacing: 1px;\n"
"    font-family: \"Open Sans\";\n"
"    font-weight: bold;   \n"
"    text-align: center;\n"
"	border-radius: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.2, y1:0, x2:1, y2:0.8, stop:0 rgba(122, 119, 			240, 255), stop:0.8 rgba(164, 122, 229, 255), stop:1 rgba(171, 113, 169, 255));\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(165, 115, 237);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border: 1px solid  ;\n"
"	background-color: rgb(165, 115, 237);\n"
"}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.bt_5, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.fr_left)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: #2e2e3c;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(\":/img/icon_gray/padlock.svg\");\n"
"    width: 16px; /* Ancho del icono */\n"
"    height: 16px; /* Alto del icono */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\":/img/icon_light/lock-open.svg\");\n"
"    width: 16px; /* Ancho del icono */\n"
"    height: 16px; /* Alto del icono */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"    color: #f2f2f2;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 10pt;\n"
"    font-weight: Normal;   \n"
"    line-height: 29px;\n"
"    letter-spacing: 2px;\n"
"    text-align: left;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(\":/img/icon_gray/toggle-button-left.png\");\n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\":/img/icon_light/toggle-button-right.png\");\n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"\n"
"")
        self.checkBox.setIconSize(QSize(0, 0))
        self.checkBox.setAutoRepeatDelay(0)
        self.checkBox.setAutoRepeatInterval(0)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.fr_lock = QFrame(self.frame)
        self.fr_lock.setObjectName(u"fr_lock")
        self.fr_lock.setMinimumSize(QSize(30, 30))
        self.fr_lock.setMaximumSize(QSize(30, 30))
        self.fr_lock.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border-radius: 15px;\n"
"")
        self.fr_lock.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_lock.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.fr_lock)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 0, 3, 0)
        self.checkBox_3 = QCheckBox(self.fr_lock)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(0, 0))
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(\":/img/icon_gray/lock-open.png\");\n"
"    width: 18px; \n"
"    height:18px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\":/img/icon_light/padlock.png\");\n"
"    width: 18px; \n"
"    height: 18px;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_3.setIconSize(QSize(0, 0))
        self.checkBox_3.setAutoRepeatDelay(0)
        self.checkBox_3.setAutoRepeatInterval(0)

        self.gridLayout.addWidget(self.checkBox_3, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.fr_lock)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_0.setText(QCoreApplication.translate("MainWindow", u"   Go home", None))
        self.bt_1.setText(QCoreApplication.translate("MainWindow", u"   Register", None))
        self.bt_2.setText(QCoreApplication.translate("MainWindow", u"   Analytics", None))
        self.bt_4.setText(QCoreApplication.translate("MainWindow", u"   Updates", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" 17", None))
        self.bt_3.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Will give you everthing you need \n"
"For your projects as a developer. \n"
"", None))
        self.bt_5.setText(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.checkBox_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Aditional Tools", None))
        self.checkBox.setText("")
        self.checkBox_3.setText("")
    # retranslateUi

