import sqlite3
from datetime import datetime

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
        self.co.commit()

        self.close()

    def ADD_DLG(self, refcode3, date, phase, type_td, no_livraison, no_version):
        self.cd.execute(f"""
        INSERT INTO t_dlg (dl_zo_id,dl_init_date,dl_phase,dl_td,dl_no_livraison,dl_no_version)
        SELECT (SELECT dlg.zo_id FROM t_zone_dlg dlg WHERE dlg.zo_refcode3 = '{refcode3}') AS zo, '{date}', '{phase}', '{type_td}', {no_livraison}, {no_version}
        WHERE NOT EXISTS(
            SELECT dl_phase,dl_td,dl_no_livraison,dl_no_version
            FROM t_dlg
            WHERE dl_zo_id = zo
            AND dl_phase = '{phase}'
            AND dl_td = '{type_td}'
            AND dl_no_livraison = {no_livraison}
            AND dl_no_version = {no_version}
            );
        """)
        self.co.commit()

        self.close()

    def ADD_EXPORT(self, zo_id, phase, type_td, no_livraison, no_version, no_export, no_etat):
        self.cd.execute(f"""
        INSERT INTO t_exports (ex_dl_id,ex_no_export,ex_date,ex_et_id)
        SELECT (SELECT dl_id
                FROM t_dlg
                WHERE dl_zo_id = {zo_id}
                AND dl_phase = '{phase}'
                AND dl_td = '{type_td}'
                AND dl_no_livraison = {no_livraison}
                AND dl_no_version = {no_version}) AS dlg, {no_export}, '{datetime.now()}', {no_etat};
                """)
        self.co.commit()

        self.close()


    def TEST_CO(self):
        try:
            self.cd.execute("SELECT * FROM t_dlg")
            return True
        except:
            return False
        finally:
            self.close()

    def close(self):
        self.cd.close()
        self.co.close()
