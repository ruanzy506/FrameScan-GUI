# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vuln_Edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Vuln_Edit(object):
    def setupUi(self, Form_Vuln_Edit):
        Form_Vuln_Edit.setObjectName("Form_Vuln_Edit")
        Form_Vuln_Edit.resize(1459, 821)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Vuln_Edit.setWindowIcon(icon)
        Form_Vuln_Edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form_Vuln_Edit.setAutoFillBackground(False)
        Form_Vuln_Edit.setStyleSheet("")
        Form_Vuln_Edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtWidgets.QGridLayout(Form_Vuln_Edit)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(Form_Vuln_Edit)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_vuln_id = QtWidgets.QLabel(Form_Vuln_Edit)
        self.label_vuln_id.setMinimumSize(QtCore.QSize(30, 0))
        self.label_vuln_id.setObjectName("label_vuln_id")
        self.horizontalLayout.addWidget(self.label_vuln_id)
        self.label = QtWidgets.QLabel(Form_Vuln_Edit)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_vuln_cms = QtWidgets.QComboBox(Form_Vuln_Edit)
        self.comboBox_vuln_cms.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_vuln_cms.setEditable(True)
        self.comboBox_vuln_cms.setObjectName("comboBox_vuln_cms")
        self.horizontalLayout.addWidget(self.comboBox_vuln_cms)
        self.label_9 = QtWidgets.QLabel(Form_Vuln_Edit)
        self.label_9.setMinimumSize(QtCore.QSize(70, 35))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit_vuln_file = QtWidgets.QLineEdit(Form_Vuln_Edit)
        self.lineEdit_vuln_file.setObjectName("lineEdit_vuln_file")
        self.horizontalLayout.addWidget(self.lineEdit_vuln_file)
        self.pushButton_vuln_save = QtWidgets.QPushButton(Form_Vuln_Edit)
        self.pushButton_vuln_save.setObjectName("pushButton_vuln_save")
        self.horizontalLayout.addWidget(self.pushButton_vuln_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.vuln_exp_textEdit_shell = QtWidgets.QTextEdit(Form_Vuln_Edit)
        self.vuln_exp_textEdit_shell.setObjectName("vuln_exp_textEdit_shell")
        self.verticalLayout.addWidget(self.vuln_exp_textEdit_shell)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form_Vuln_Edit)
        QtCore.QMetaObject.connectSlotsByName(Form_Vuln_Edit)

    def retranslateUi(self, Form_Vuln_Edit):
        _translate = QtCore.QCoreApplication.translate
        Form_Vuln_Edit.setWindowTitle(_translate("Form_Vuln_Edit", "漏洞插件编辑"))
        self.label_10.setText(_translate("Form_Vuln_Edit", "ID:"))
        self.label_vuln_id.setText(_translate("Form_Vuln_Edit", "None"))
        self.label.setText(_translate("Form_Vuln_Edit", "应用名称:"))
        self.label_9.setText(_translate("Form_Vuln_Edit", "插件文件名称:"))
        self.pushButton_vuln_save.setText(_translate("Form_Vuln_Edit", "保存插件"))

