import os
import sys
import stat
import locale

DB_OK            = 0
DB_FAILURE       = 1

DB_ORDER_DESC    = 0
DB_ORDER_ASC     = 1

DB_CONCAT        = 0
DB_OVERRIDE      = 1

DB_SUFFIX        = ".sdb"
TEMPLATE_SUFFIX  = ".sdbt"

LANGUAGE         =locale.getdefaultlocale()[0]

INTERNAL_CHARSET = "utf-8"

INDEX_NAME       = "_id"

if os.name == "nt":
    DEFAULTS_DIR         = sys.path[0] + "\\"
    GLOBAL_TEMPLATES_DIR = DEFAULTS_DIR + "templates\\"
    
    _HOME                = os.path.expanduser('~') + "\\"
    
    CONFIG_DIR           = _HOME + ".studb\\"
    USER_TEMPLATES_DIR   = CONFIG_DIR + "templates\\"
    if not os.access(CONFIG_DIR, os.F_OK):
        os.mkdir(CONFIG_DIR)
    if not os.access(CONFIG_DIR, os.R_OK) or not os.access(CONFIG_DIR, os.W_OK):
        os.chmod(CONFIG_DIR, stat.S_IWRITE)
    
    if not os.access(USER_TEMPLATES_DIR, os.F_OK):
        os.mkdir(USER_TEMPLATES_DIR)
    if not os.access(USER_TEMPLATES_DIR, os.R_OK) or not os.access(USER_TEMPLATES_DIR, os.W_OK):
        os.chmod(USER_TEMPLATES_DIR, stat.S_IWRITE)
    
    del _HOME

elif os.name == "posix":
    DEFAULTS_DIR         = "/etc/studb/"
    GLOBAL_TEMPLATES_DIR = DEFAULTS_DIR + "template/"
    
    CONFIG_DIR           = os.path.expanduser('~') + "/.studb/"
    USER_TEMPLATES_DIR   = CONFIG_DIR + "templates/"
    if not os.access(CONFIG_DIR, os.F_OK):
        os.mkdir(CONFIG_DIR)
    if not os.access(CONFIG_DIR, os.R_OK) or not os.access(CONFIG_DIR, os.W_OK):
        os.chmod(CONFIG_DIR, stat.S_IRUSR | stat.S_IWUSR)
    
    if not os.access(USER_TEMPLATES_DIR, os.F_OK):
        os.mkdir(USER_TEMPLATES_DIR)
    if not os.access(USER_TEMPLATES_DIR, os.R_OK) or not os.access(USER_TEMPLATES_DIR, os.W_OK):
        os.chmod(USER_TEMPLATES_DIR, stat.S_IRUSR | stat.S_IWUSR)
