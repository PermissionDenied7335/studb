# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\studb\ui\dialog_select_template.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_select_template(object):
    def setupUi(self, Dialog_select_template):
        Dialog_select_template.setObjectName("Dialog_select_template")
        Dialog_select_template.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_select_template.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Dialog_select_template.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_select_template)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog_select_template)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.description_title = QtWidgets.QLabel(Dialog_select_template)
        self.description_title.setObjectName("description_title")
        self.verticalLayout_2.addWidget(self.description_title)
        self.description = QtWidgets.QTextBrowser(Dialog_select_template)
        self.description.setObjectName("description")
        self.verticalLayout_2.addWidget(self.description)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_select_template)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_select_template)
        self.buttonBox.accepted.connect(Dialog_select_template.accept)
        self.buttonBox.rejected.connect(Dialog_select_template.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_select_template)

    def retranslateUi(self, Dialog_select_template):
        _translate = QtCore.QCoreApplication.translate
        Dialog_select_template.setWindowTitle(_translate("Dialog_select_template", "数据库模板"))
        self.description_title.setText(_translate("Dialog_select_template", "描述："))
