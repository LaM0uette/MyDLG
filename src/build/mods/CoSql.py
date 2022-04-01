import sqlite3

from src.lib.private import v_sql


class CoSql:
    def __init__(self):
        self.co = sqlite3.connect(v_sql.BDD)
        self.cd = self.co.cursor()


    def TEST_CO(self):
        self.cd.execute("SELECT * FROM t_partenaires")
        for i in self.cd.fetchall():
            print(i)

        self.close()
    def close(self):
        self.cd.close()
        self.co.close()
