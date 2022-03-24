# pylint: disable=W0603
'''Sqlite library.'''
from os import stat
import sqlite3
from slib.config import SConfig

SQLITE_FILE = None

class MemoryCacheKeyNotFound(Exception):
    '''Rised when key not found.'''

class SSqlite():
    '''Access Sqlite database.'''

    @staticmethod
    def init(file=None):
        '''Initialize Sqlite database.'''

        global SQLITE_FILE

        if file is not None:
            SQLITE_FILE = file
        else:
            SQLITE_FILE = SConfig.get_str_conf('sqlite_db_file_name')

    @staticmethod
    def execute(sql=None):
        SQLITE_CONN = sqlite3.connect(SQLITE_FILE)

        cur = SQLITE_CONN.cursor()

        count = cur.execute(sql).rowcount

        SQLITE_CONN.commit()

        SQLITE_CONN.close()

        return count

    @staticmethod
    def fetch_all(sql=None):
        SQLITE_CONN = sqlite3.connect(SQLITE_FILE)

        cur = SQLITE_CONN.cursor()

        cur.execute(sql)

        result = cur.fetchall()

        SQLITE_CONN.commit()

        SQLITE_CONN.close()

        return result
