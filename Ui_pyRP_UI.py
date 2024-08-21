# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyRP_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect, QSize,Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import ( QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton,QSlider,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(353, 424)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 331, 391))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSlider = QSlider(self.layoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(16)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(180, 0))

        self.verticalLayout.addWidget(self.comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_5)

        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_auth = QLabel(self.layoutWidget)
        self.label_auth.setObjectName(u"label_auth")

        self.horizontalLayout_3.addWidget(self.label_auth)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_ver = QLabel(self.layoutWidget)
        self.label_ver.setObjectName(u"label_ver")

        self.horizontalLayout_3.addWidget(self.label_ver)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5bc6\u7801\u751f\u6210\u5668", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u751f\u6210\u5668", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u957f\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\uff01\u4f4d\u6570\uff01", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u5f3a\u5ea6", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5f3a\u5ea6\u8bf4\u660e\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u7ed3\u679c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210\uff01\u5e76\u590d\u5236\uff01", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\uff1a", None))
        self.label_auth.setText(QCoreApplication.translate("Form", u"\uff01\u4f5c\u8005\uff01", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7248\u672c\uff1a", None))
        self.label_ver.setText(QCoreApplication.translate("Form", u"\uff01ver\uff01", None))
    # retranslateUi

