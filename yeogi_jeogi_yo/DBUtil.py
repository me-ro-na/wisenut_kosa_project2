import cx_Oracle as oracle

import os
os.putenv('NLS_LANG', '.UTF8')

# DB정보 수정 필수!
oracle_dsn = oracle.makedsn(host="localhost", port=1521, sid="xe")

class Database():
    def __init__(self):
        # DB정보 수정 필수!
        self.db = oracle.connect(dsn=oracle_dsn, user="유저명", password="비밀번호")
        self.cursor = self.db.cursor()
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
    def commit():
        self.db.commit()