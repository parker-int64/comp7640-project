from pathlib import Path
import json
BACKEND_DIR = Path(__file__).parent.parent
PROJECT_DIR =  BACKEND_DIR.parent.parent
FRONTEND_DIR = PROJECT_DIR/"Frontend"
STATIC_DIR = FRONTEND_DIR/"dist"



PYMYSQL_CONF = PROJECT_DIR/"sqlconf.json"

dt = json.load(PYMYSQL_CONF.open(encoding='utf-8'))

SQL_HOST = dt["host"]
SQL_USER = dt["user"]
SQL_PASSWD = dt["passwd"]


if __name__ == "__main__":
    print(globals())