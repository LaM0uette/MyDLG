import sqlite3

from src.lib.private import v_sql


class CoSql:
    def __init__(self):
        self.co = sqlite3.connect(v_sql.BDD)
        self.cd = self.co.cursor()


    def ADD_ZONE_DLG(self, marche, nro, pm, refcode3):
        self.cd.execute(f"""
        INSERT INTO t_zone_dlg (zo_marche,zo_nro,zo_pm,zo_refcode3)
        SELECT {marche}, {nro}, {pm}, '{refcode3}'
        WHERE NOT EXISTS(
            SELECT zo_refcode3
            FROM t_zone_dlg
            WHERE zo_refcode3 = '{refcode3}'
            );
        """)

        self.close()
    def TEST_CO(self):
        try:
            self.cd.execute("SELECT * FROM t_dlg")
            return False
        except:
            return False
        finally:
            self.close()
    def close(self):
        self.cd.close()
        self.co.close()
