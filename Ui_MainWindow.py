# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import QParallelAnimationGroup
from PySide2 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(650, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ToolBarWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolBarWidget.sizePolicy().hasHeightForWidth())
        self.ToolBarWidget.setSizePolicy(sizePolicy)
        self.ToolBarWidget.setObjectName(_fromUtf8("ToolBarWidget"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ToolBarWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)
        self.pushButton1 = QtWidgets.QPushButton(self.ToolBarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        self.pushButton1.setStyleSheet(_fromUtf8(""))
        self.pushButton1.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("options.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton1.setIcon(icon)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.verticalLayout_2.addWidget(self.pushButton1)
        self.pushButton4 = QtWidgets.QPushButton(self.ToolBarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy)
        self.pushButton4.setStyleSheet(_fromUtf8(""))
        self.pushButton4.setText(_fromUtf8(""))
        self.pushButton4.setObjectName(_fromUtf8("pushButton4"))
        self.verticalLayout_2.addWidget(self.pushButton4)
        self.pushButton2 = QtWidgets.QPushButton(self.ToolBarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setStyleSheet(_fromUtf8(""))
        self.pushButton2.setText(_fromUtf8(""))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.verticalLayout_2.addWidget(self.pushButton2)
        self.pushButton3 = QtWidgets.QPushButton(self.ToolBarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setStyleSheet(_fromUtf8(""))
        self.pushButton3.setText(_fromUtf8(""))
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
        self.verticalLayout_2.addWidget(self.pushButton3)
        self.horizontalLayout.addWidget(self.ToolBarWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 180, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.widget)
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.horizontalLayout.addWidget(self.mainWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton1.clicked.connect(MainWindow, QtCore.SLOT("onBtn1Clicked()"))

        from Spoiler import Spoiler
        s = Spoiler()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))

