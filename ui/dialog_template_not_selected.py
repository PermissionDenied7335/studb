# -*- coding: utf-8 -*-

#made by hand


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class dialog_template_not_selected(QObject):
    def __init__(self, parent):
        super(dialog_template_not_selected, self).__init__()
        self.setObjectName("Dialog_template_not_selected")
        self.parent = parent
    
    def exec_(self):
        _translate = QCoreApplication.translate
        return QMessageBox.critical(self.parent, _translate("Dialog_template_not_selected", "未指定数据库模板"), _translate("Dialog_template_not_selected", "必须为数据库指定模板！"), QMessageBox.Ok, QMessageBox.Ok)
