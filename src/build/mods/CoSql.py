import sqlite3
from datetime import datetime

from src.lib.private import v_sql


class CoSql:
    def __init__(self):
        self.co = sqlite3.connect(v_sql.BDD)
        self.cd = self.co.cursor()

    # ADD
    def ADD_ZONE_DLG(self, marche, nro, pm, refcode3):
        """
        Insert une ligne dans la table t_zone_dlg s'il n'existe pas déjà avec les mêmes données.
        :param marche: marché de la zone
        :param nro: code NRO de la zone
        :param pm: code PM de la zone
        :param refcode3: refcode3 de la zone
        """
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
        """
        Ajoute un dlg dans la table t_dlg s'il n'existe pas déjà avec les mêmes données.
        :param refcode3: refcode3 de la zone
        :param date: date de demande de traitement de l'export
        :param phase: phase de l'export
        :param type_td: transport uniquement T | distri uniquement D | les 2 TD
        :param no_livraison: numéo de livraison
        :param no_version: numéro de version de l'export
        """
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
    def ADD_EXPORT(self, dl_id, no_export, no_etat):
        """
        Ajoute un export dans la table t_exports s'il n'existe pas déjà avec les mêmes données.
        :param dl_id: identifiant du dlg
        :param no_export: numéro de l'export (nombre de fois qu'il a fallut le refaire)
        :param no_etat: numéro qui correspond à l'état dans la table t_etats
        """
        self.cd.execute(f"""
        INSERT INTO t_exports (ex_dl_id,ex_no_export,ex_date,ex_et_id)
        SELECT {dl_id}, {no_export}, '{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', {no_etat};
                """)
        self.co.commit()

        self.close()


    # SELECT
    def GET_PHASE(self):
        self.cd.execute("""
        SELECT * FROM t_phase
        """)
        rtn = self.cd.fetchall()

        self.close()
        return rtn
    def GET_CODE_ZONE(self):
        self.cd.execute("""
        SELECT * FROM t_code_zone
        """)
        rtn = self.cd.fetchall()

        self.close()
        return rtn


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
