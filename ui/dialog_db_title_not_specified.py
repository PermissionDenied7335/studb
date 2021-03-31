# -*- coding: utf-8 -*-

#made by hand


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class dialog_db_title_not_specified(QObject):
    def __init__(self, parent):
        super(dialog_db_title_not_specified, self).__init__()
        self.setObjectName("Dialog_db_title_not_specified")
        self.parent = parent
    
    def exec_(self):
        _translate = QCoreApplication.translate
        return QMessageBox.critical(self.parent, _translate("Dialog_db_title_not_specified", "未指定数据库标题"), _translate("Dialog_db_title_not_specified", "必须为数据库指定标题！"), QMessageBox.Ok, QMessageBox.Ok)
