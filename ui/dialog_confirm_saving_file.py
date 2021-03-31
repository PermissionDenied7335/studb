# -*- coding: utf-8 -*-

#made by hand


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class dialog_confirm_saving_file(QObject):
    def __init__(self, parent):
        super(dialog_confirm_saving_file, self).__init__()
        self.setObjectName("Dialog_comfirm_saving_file")
        self.parent = parent
    
    def exec_(self):
        _translate = QCoreApplication.translate
        return QMessageBox.question(self.parent, _translate("Dialog_comfirm_saving_file", "有未保存的文件"), _translate("Dialog_comfirm_saving_file", "是否保存当前文件？"), QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel, QMessageBox.Save)
