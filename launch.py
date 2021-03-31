import sys
import re
import os
import json

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from db_handler import *
from constants import *
from ui import *


class dialog_select_template(QDialog, Ui_Dialog_select_template):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_select_template, self).__init__(parent)
        self.setupUi(self)
        
        _global_templates = os.listdir(GLOBAL_TEMPLATES_DIR)
        _del_list = []
        for i in range(len(_global_templates)):
            if _global_templates[i][-len(TEMPLATE_SUFFIX):] != TEMPLATE_SUFFIX:
                _del_list.append(i)
            _global_templates[i] = GLOBAL_TEMPLATES_DIR + _global_templates[i]
        for i in range(len(_del_list), 0, -1):
            del _global_templates[_del_list[i]]
        _del_list.clear()
        
        _user_templates = os.listdir(USER_TEMPLATES_DIR)
        for i in range(len(_user_templates)):
            if _user_templates[i][-len(TEMPLATE_SUFFIX):] != TEMPLATE_SUFFIX:
                _del_list.append(i)
            _user_templates[i] = USER_TEMPLATES_DIR + _user_templates[i]
        for i in range(len(_del_list), 0, -1):
            del _user_templates[_del_list[i]]
        
        templates = _global_templates + _user_templates
        
        self.items = {}
        for item in templates:
            with open(item) as fd:
                _raw_template = json.load(fd)
            if LANGUAGE in _raw_template.keys():
                self.listWidget.addItem(base64.urlsafe_b64decode(_raw_template[LANGUAGE]["name"]).decode(INTERNAL_CHARSET))
                self.items[base64.urlsafe_b64decode(_raw_template[LANGUAGE]["name"]).decode(INTERNAL_CHARSET)] = (item, base64.urlsafe_b64decode(_raw_template[LANGUAGE]["description"]).decode(INTERNAL_CHARSET))#(path, description)
            else:
                self.listWidget.addItem(base64.urlsafe_b64decode(_raw_template["default"]["name"]).decode(INTERNAL_CHARSET))
                self.items[base64.urlsafe_b64decode(_raw_template["default"]["name"]).decode(INTERNAL_CHARSET)] = (item, base64.urlsafe_b64decode(_raw_template["default"]["description"]).decode(INTERNAL_CHARSET))#(path, description)
        
        self.listWidget.clicked.connect(self.show_description)
    
    def show_description(self, item):
        self.description.setText(self.items[item.data()][1])
        self.result = (item.data(), self.items[item.data()][0])#(name, path)

class dialog_new(QDialog, Ui_Dialog_new):
    def __init__(self, parent):
        self.result   = None
        self.template = None
        self.parent   = parent
        super(dialog_new, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton_db_template.clicked.connect(self.select_template)
        self.buttonBox.accepted.connect(self.check)
    
    def select_template(self):
        dialog = dialog_select_template(self)
        if dialog.exec_():
            if dialog.result is not None:
                self.pushButton_db_template.setText(dialog.result[0])
                self.template = dialog.result[1]
    
    def check(self):
        if self.lineEdit_db_title.text() == "":
            dialog_db_title_not_specified(self).exec_()
        elif self.template is None:
            dialog_template_not_selected(self).exec_()
        else:
            self.result = (self.lineEdit_db_title.text(), self.template)#(title, path)
            self.accept()

class dialog_create_passwd(QDialog, Ui_Dialog_create_passwd):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_create_passwd, self).__init__(parent)
        self.setupUi(self)

class dialog_change_db_title(QDialog, Ui_Dialog_change_db_title):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_change_db_title, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.check)
    
    def check(self):
        if self.lineEdit.text() == "":
            dialog_db_title_not_specified(self).exec_()
        else:
            self.result = self.lineEdit.text()
            self.accept()

class dialog_set_column_name(QDialog, Ui_Dialog_set_column_name):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_set_column_name, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.check)
    
    def check(self):
        if self.lineEdit.text() == "":
            dialog_db_title_not_specified(self).exec_()
        else:
            self.result = self.lineEdit.text()
            self.accept()

class dialog_delete_row(QDialog, Ui_Dialog_delete_row):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_delete_row, self).__init__(parent)
        self.setupUi(self)
        
        self.spinBox.valueChanged.connect(self.update)
    
    def update(self, value):
        self.result = int(value)

class dialog_delete_column(QDialog, Ui_Dialog_delete_column):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        super(dialog_delete_column, self).__init__(parent)
        self.setupUi(self)
        
        self.comboBox.currentIndexChanged.connect(self.update)
    
    def update(self):
        self.result = self.comboBox.currentText()

class dialog_about(QDialog, Ui_Dialog_about):
    def __init__(self, parent):
        self.parent = parent
        super(dialog_about, self).__init__(parent)
        self.setupUi(self)

class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        
        #file status
        self.not_saved    = False
        self.current_file = None
        self.current_path = ""
        
        self.action_new.triggered.connect(self.new_file)
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save_file)
        self.action_add_row.triggered.connect(self.add_row)
        self.action_del_row.triggered.connect(self.del_row)
        self.action_add_column.triggered.connect(self.add_column)
        self.action_del_column.triggered.connect(self.del_column)
        self.action_about_this.triggered.connect(self.about)
        self.action_about_qt.triggered.connect(self.about_qt)
        self.action_change_db_title.triggered.connect(self.change_db_title)
    
    def new_file(self):
        dialog = dialog_new(self)
        if dialog.exec_():
            if dialog.result is not None:
                if self.not_saved:
                    if dialog_confirm_saving_file(self).exec_():
                        self.save_file()
                self.not_saved    = True
                self.current_file = database()
                self.current_file.new(dialog.result[0], dialog.result[1], LANGUAGE)
                self.update_workspace()
    
    def open_file(self):
        self.current_path = QFileDialog.getOpenFileName(self, None, None, "*.sdb")[0]
        if self.current_path != "":
            if self.not_saved:
                if dialog_confirm_saving_file(self).exec_():
                    self.save_file()
            self.not_saved    = True
            self.current_file = database()
            self.current_file.open(self.current_path)
            self.update_workspace()
    
    def save_file(self):
        if self.current_file is not None: 
            if self.current_path == "":
                self.current_path = QFileDialog.getSaveFileName(self, None, None, "*.sdb")[0]
            self.current_file.save(self.current_path)
    
    def update_workspace(self):
        self.tableWidget.blockSignals(True)
        self.action_add_row.setEnabled(True)
        self.action_del_row.setEnabled(True)
        self.action_add_column.setEnabled(True)
        self.action_del_column.setEnabled(True)
        self.action_change_db_title.setEnabled(True)
        self.tableWidget.itemChanged.connect(self.update_database)
        self.label.setText(self.current_file.title)
        self.tableWidget.setColumnCount(len(self.current_file.columns()))
        self.tableWidget.setRowCount(len(self.current_file.index()))
        self.tableWidget.setHorizontalHeaderLabels(self.current_file.columns())
        items = self.current_file.get_all()
        for i in range(len(items)):
            for j in range(len(items[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(items[i][j])))
        self.tableWidget.blockSignals(False)
    
    def update_database(self, item):
        self.current_file.update(item.row(), self.current_file.columns()[item.column()], item.text())
    
    def change_db_title(self):
        dialog = dialog_change_db_title(self)
        if dialog.exec_():
            if dialog.result is not None:
                self.current_file.title = dialog.result
                self.update_workspace()
    
    def add_row(self):
        self.current_file.add_index()
        self.update_workspace()
    
    def add_column(self):
        dialog = dialog_set_column_name(self)
        if dialog.exec_():
            if dialog.result is not None:
                self.current_file.add_column(dialog.result)
                self.update_workspace()
    
    def del_row(self):
        dialog = dialog_delete_row(self)
        dialog.spinBox.setMaximum(len(self.current_file.index()))
        if dialog.exec_():
            if dialog.result is not None:
                self.current_file.delete_index(dialog.result - 1)
                self.update_workspace()
    
    def del_column(self):
        dialog = dialog_delete_column(self)
        dialog.comboBox.addItems(self.current_file.columns())
        if dialog.exec_():
            if dialog.result is not None:
                self.current_file.delete_column(dialog.result)
                self.update_workspace()
    
    def about(self):
        dialog_about(self).exec_()
    
    def about_qt(self):
        QMessageBox.aboutQt(self, None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    _translate = QCoreApplication.translate
    if os.access("qt_" + LANGUAGE + ".qm", os.R_OK):
        trans = QTranslator()
        trans.load("qt_" + LANGUAGE + ".qm")
        app.installTranslator(trans)
    
    mw = main_window()
    mw.show()
    sys.exit(app.exec_())
