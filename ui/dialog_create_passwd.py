# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_create_passwd.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_create_passwd(object):
    def setupUi(self, Dialog_create_passwd):
        Dialog_create_passwd.setObjectName("Dialog_create_passwd")
        Dialog_create_passwd.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_create_passwd.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Dialog_create_passwd.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_create_passwd)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_passwd = QtWidgets.QLabel(Dialog_create_passwd)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_passwd.setFont(font)
        self.label_passwd.setObjectName("label_passwd")
        self.verticalLayout.addWidget(self.label_passwd)
        self.lineEdit_passwd = QtWidgets.QLineEdit(Dialog_create_passwd)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.verticalLayout.addWidget(self.lineEdit_passwd)
        self.checkBox_display_passwd = QtWidgets.QCheckBox(Dialog_create_passwd)
        self.checkBox_display_passwd.setObjectName("checkBox_display_passwd")
        self.verticalLayout.addWidget(self.checkBox_display_passwd)
        self.label_confirm_passwd = QtWidgets.QLabel(Dialog_create_passwd)
        self.label_confirm_passwd.setObjectName("label_confirm_passwd")
        self.verticalLayout.addWidget(self.label_confirm_passwd)
        self.lineEdit_confirm_passwd = QtWidgets.QLineEdit(Dialog_create_passwd)
        self.lineEdit_confirm_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_passwd.setObjectName("lineEdit_confirm_passwd")
        self.verticalLayout.addWidget(self.lineEdit_confirm_passwd)
        self.checkBox_display_confirm_passwd = QtWidgets.QCheckBox(Dialog_create_passwd)
        self.checkBox_display_confirm_passwd.setObjectName("checkBox_display_confirm_passwd")
        self.verticalLayout.addWidget(self.checkBox_display_confirm_passwd)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_create_passwd)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_create_passwd)
        self.buttonBox.accepted.connect(Dialog_create_passwd.accept)
        self.buttonBox.rejected.connect(Dialog_create_passwd.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_create_passwd)

    def retranslateUi(self, Dialog_create_passwd):
        _translate = QtCore.QCoreApplication.translate
        Dialog_create_passwd.setWindowTitle(_translate("Dialog_create_passwd", "创建新密码"))
        self.label_passwd.setText(_translate("Dialog_create_passwd", "请输入密码："))
        self.checkBox_display_passwd.setText(_translate("Dialog_create_passwd", "显示密码"))
        self.label_confirm_passwd.setText(_translate("Dialog_create_passwd", "确认密码："))
        self.checkBox_display_confirm_passwd.setText(_translate("Dialog_create_passwd", "显示密码"))
