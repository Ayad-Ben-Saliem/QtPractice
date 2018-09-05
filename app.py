import sys

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout






from PyQt5.QtCore import Qt, QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import *
from PySide2.QtCore import SLOT
from docutils.nodes import contact


class Spoiler(QWidget):
    def __init__(self, title="", animationDuration=300, parent=None):
        QWidget.__init__(self, parent)

        self.mainLayout = QGridLayout()
        self.toggleButton = QToolButton()
        self.toggleAnimation = QParallelAnimationGroup()
        self.contentArea = QScrollArea()
        self.headerLine = QFrame()
        self.animationDuration = animationDuration

        self.toggleButton.setStyleSheet("QToolButton { border: none; }")
        self.toggleButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggleButton.setArrowType(Qt.ArrowType.RightArrow)
        self.toggleButton.setText(title)
        self.toggleButton.setCheckable(True)
        self.toggleButton.setChecked(False)

        self.headerLine.setFrameShape(QFrame.HLine)
        self.headerLine.setFrameShadow(QFrame.Sunken)
        self.headerLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.contentArea.setStyleSheet("QScrollArea { background-color: white; border: none; }")
        self.contentArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)
        # let the entire widget grow and shrink with its content
        self.toggleAnimation.addAnimation(QPropertyAnimation())
        self.toggleAnimation.addAnimation(QPropertyAnimation(self))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self.contentArea, b"maximumHeight"))

        # don't waste space
        self.mainLayout.setVerticalSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        row = 0
        self.mainLayout.addWidget(self.toggleButton, 0, 0, 1, 1, Qt.AlignLeft)
        self.mainLayout.addWidget(self.headerLine, 0, 2, 1, 1)
        self.mainLayout.addWidget(self.contentArea, 1, 0, 1, 3)
        self.setLayout(self.mainLayout)

        self.toggleButton.clicked[bool].connect(self.expandShrinkContent)

    def expandShrinkContent(self, checked):
        if checked:
            self.toggleButton.setArrowType(Qt.ArrowType.DownArrow)
            self.toggleAnimation.setDirection(QAbstractAnimation.Forward)

        else:
            self.toggleButton.setArrowType(Qt.ArrowType.RightArrow)
            self.toggleAnimation.setDirection(QAbstractAnimation.Backward)

        self.toggleAnimation.start()

    def setContentLayout(self, contentLayout):

        self.contentArea.setLayout(contentLayout)
        collapsedHeight = self.sizeHint().height() - self.contentArea.maximumHeight()
        contentHeight = contentLayout.sizeHint().height()
        i = 0
        while i < self.toggleAnimation.animationCount():
            i += 1
            spoilerAnimation = self.toggleAnimation.animationAt(i)
            if spoilerAnimation is not None:
                spoilerAnimation.setDuration(self.animationDuration)
                spoilerAnimation.setStartValue(collapsedHeight)
                spoilerAnimation.setEndValue(collapsedHeight + contentHeight)

        contentAnimation = self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1)
        contentAnimation.setDuration(self.animationDuration)
        contentAnimation.setStartValue(0)
        contentAnimation.setEndValue(contentHeight)









app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout(window)

spoiler = Spoiler()

content = QVBoxLayout()
content.addWidget(QLabel("This is test, isn't it eamon?"))

spoiler.setContentLayout(content)

layout.addWidget(spoiler)
layout.setAlignment(Qt.AlignBottom)
window.show()
sys.exit(app.exec_())
