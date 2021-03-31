import base64
import json
import uuid
import os
import io
import pandas

from constants import *

class database():
    def __init__(self):
        self.__df     = None
    
    def open(self, path):
        with open(path, "r") as sdb:
            _raw_data = json.load(sdb)
        self.__type       = _raw_data["type"]
        if self.__type == "text":
            self.title        = base64.urlsafe_b64decode(_raw_data["title"]).decode(INTERNAL_CHARSET)
            self.__encryption = _raw_data["encryption"]
            _raw_db           = io.StringIO(base64.urlsafe_b64decode(_raw_data["database"]).decode(INTERNAL_CHARSET))
            
            if self.__encryption is not None:
                return (_raw_db.getvalue().encode(INTERNAL_CHARSET), self.__encryption)
            else:
                self.__df = pandas.read_csv(_raw_db)
                self.__df = self.__df.set_index(INDEX_NAME)
            
            return DB_OK
        else:
            return DB_FAILURE
    
    def new(self, title, template, language, encryption = None):
        self.title        = title
        self.__encryption = encryption
        
        with open(template, "r") as fd:
            _raw_template = json.load(fd)
        if _raw_template["type"] == "text":
            if language in _raw_template.keys():
                _template = io.StringIO(base64.urlsafe_b64decode(_raw_template[language]["database"]).decode(INTERNAL_CHARSET))
            else:
                _template = io.StringIO(base64.urlsafe_b64decode(_raw_template["default"]["database"]).decode(INTERNAL_CHARSET))
                
            self.__df = pandas.read_csv(_template)
            self.__df = self.__df.set_index(INDEX_NAME) 
            return DB_OK
        else:
            return DB_FAILURE
    
    def index(self):
        return self.__df.index.tolist()
    
    def columns(self):
        return self.__df.columns.tolist()
    
    def get_all(self):
        return self.__df.values.tolist()
    
    def update(self, index, column, data):
        self.__df[column][index] = data
        return DB_OK
    
    def add_column(self, column):
        self.__df.insert(self.__df.columns.size, column, None)
        return DB_OK
    
    def delete_column(self, column):
        self.__df = self.__df.drop(column, 1)
        return DB_OK
    
    def add_index(self):
        self.__df.loc[self.__df.index.size] = None
        return DB_OK
    
    def delete_index(self, index):
        self.__df = self.__df.drop(index, 0)
        return DB_OK
    
    def import_from_csv(self, path, mode = DB_CONCAT):
        _temp = pandas.read_csv(path)
        if mode == DB_OVERRIDE:
            self.__df = _temp
        elif mode == DB_CONCAT:
            self.__df.concat(_temp)
        else:
            raise ValueError("\"mode\" cannot be \"" + str(mode) + "\"!")
        return DB_OK
            
    
    def export_to_csv(self, path):
        self.__df.to_csv(path)
        return DB_OK
    
    def decrypt(self, data):
        _raw_db   = io.StringIO(data.decode(INTERNAL_CHARSET))
        self.__df = pandas.read_csv(_raw_db)
        self.__df = self.__df.set_index(INDEX_NAME)
        return DB_OK

    def save(self, path):
        if self.__df is not None:
            _raw_data = {}
            _raw_data["title"]      = base64.urlsafe_b64encode(self.title.encode(INTERNAL_CHARSET)).decode(INTERNAL_CHARSET)
            _raw_data["type"]       = "text"
            _raw_data["encryption"] = self.__encryption
            _raw_data["database"]   = base64.urlsafe_b64encode(self.__df.to_csv().encode(INTERNAL_CHARSET)).decode(INTERNAL_CHARSET)
            
            with open(path, "w") as sdb:
                json.dump(_raw_data, sdb)
            
            return DB_OK
        
        else:
            return DB_FAILURE

        
