# -*- coding: utf-8 -*-

import sqlite3 


class DBHelper:
    
    def __init__(self, dbname="teledata.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.c = self.conn.cursor()
        self.setup()
# id INTEGER AUTOINCREMENT,
    def setup(self):
        stmt = """CREATE TABLE IF NOT EXISTS data ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    contacted INTEGRER NULL,
                                                    tlgrm_user DEFAULT none                                                  
                                                   )"""
        self.c.execute(stmt)
        self.conn.commit()

    def add_tlgrm_user(self, contacted, tlgrm_user):
        self.c.execute("INSERT INTO data (contacted, tlgrm_user) VALUES (?, ?)", (contacted, tlgrm_user))
        self.conn.commit()

    def del_tlgrm_user(self, tlgrm_id):
        self.c.execute("DELETE FROM data WHERE tlgrm_id=?", (tlgrm_id, ))
        self.conn.commit()

    def checkifexist(self, tlgrm_user):
        self.c.execute("SELECT tlgrm_user FROM data WHERE tlgrm_user=?", (tlgrm_user, ))
        user = self.c.fetchone()
        if user is not None:
            return user[0]
        else:
            return None

    def getusertocontact(self, limit=50):
        self.c.execute("SELECT tlgrm_user FROM data WHERE contacted = 0 limit "+str(limit))
        user = self.c.fetchall()
        if user is not None:
            return user
        else:
            return None

    def total(self, where = None):
        if where == 'contacted':
            self.c.execute("SELECT count(*) FROM data WHERE contacted IS NOT 0")
        elif where == 'notcontacted':
            self.c.execute("SELECT count(*) FROM data WHERE contacted = 0 ")
        else:
            self.c.execute("SELECT count(*) FROM data ")
        user = self.c.fetchone()
        if user is not None:
            return user[0]
        else:
            return None
    def updateuser_to_contacted(self,user):
        self.c.execute(" update data set contacted = 1 WHERE tlgrm_user=?", (user, ))
        self.conn.commit()

    def refresh_contacted(self):
        self.c.execute(" update data set contacted = 0 ")
        self.conn.commit()