import MySQLdb

from . import sql_vrb


class Sql:
    param_local = {
        "host": "localhost",
        "port": 3306,
        "user": "LaM0uette",
        "passwd": "Jesuisunmotdepasse*",
        "db": "ptf"
    }
    param = {
        "host": sql_vrb.host,
        "port": sql_vrb.port,
        "user": sql_vrb.user,
        "passwd": sql_vrb.passwd,
        "db": "ptf"
    }

    def __init__(self):
        self.co = MySQLdb.connect(**self.param)
        self.cd = self.co.cursor(MySQLdb.cursors.DictCursor)

    def LST_CLIENTS(self):
        self.cd.execute(
            """
            SELECT *
            FROM t_clients
            """)
        return self.cd.fetchall()
    def LST_VILLES(self):
        self.cd.execute(
            """
            SELECT vl_nom
            FROM t_villes
            ORDER BY vl_nom
            """)
        return self.cd.fetchall()
    def LST_VILLES_CODE_POSTAL(self, insee):
        self.cd.execute(
            f"""
            SELECT vl_nom
            FROM t_villes
            WHERE vl_code_postal = {insee}
            ORDER BY vl_nom
            """)
        return self.cd.fetchall()
    def LST_VILLES_INSEE(self, insee):
        self.cd.execute(
            f"""
            SELECT vl_nom
            FROM t_villes
            WHERE vl_code_insee = {insee}
            ORDER BY vl_nom
            """)
        return self.cd.fetchall()

    def GET_CLIENT(self, cl_id):
        self.cd.execute(
            f"""
            SELECT *
            FROM t_clients
            WHERE cl_id = {cl_id}
            """)
        return self.cd.fetchone()
    def GET_CLIENTS(self):
        self.cd.execute(
            """
            SELECT cl_id, cl_civilite, cl_nom, cl_prenom
            FROM t_clients
            """)
        return self.cd.fetchall()
    def ADD_CLIENT(self, **kwargs):
        self.cd.execute(
            f"""
            INSERT INTO t_clients(
            cl_civilite,
            cl_nom,
            cl_prenom,
            cl_date_naissance,
            cl_situation_familiale,
            cl_nb_enfants,
            cl_activite_pro,
            cl_mail,
            cl_num_fixe,
            cl_num_mobile,
            cl_ville,
            cl_adresse,
            cl_insee,
            cl_date_crea,
            cl_origine_crea,
            cl_notes)
            VALUES(
            "{kwargs.get("cl_civilite")}",
            "{kwargs.get("cl_nom")}",
            "{kwargs.get("cl_prenom")}",
            "{kwargs.get("cl_date_naissance")}",
            "{kwargs.get("cl_situation_familiale")}",
            {kwargs.get("cl_nb_enfants")},
            "{kwargs.get("cl_activite_pro")}",
            "{kwargs.get("cl_mail")}",
            "{kwargs.get("cl_num_fixe")}",
            "{kwargs.get("cl_num_mobile")}",
            "{kwargs.get("cl_ville")}",
            "{kwargs.get("cl_adresse")}",
            "{kwargs.get("cl_insee")}",
            "{kwargs.get("cl_date_crea")}",
            "{kwargs.get("cl_origine_crea")}",
            "{kwargs.get("cl_notes")}")
            """)
        self.co.commit()
        self.close()
    def MODIF_CLIENT(self, **kwargs):
        self.cd.execute(
            f"""
            UPDATE t_clients 
            SET cl_civilite = "{kwargs.get("cl_civilite")}",
            cl_nom = "{kwargs.get("cl_nom")}",
            cl_prenom = "{kwargs.get("cl_prenom")}",
            cl_date_naissance = "{kwargs.get("cl_date_naissance")}",
            cl_situation_familiale = "{kwargs.get("cl_situation_familiale")}",
            cl_nb_enfants = {kwargs.get("cl_nb_enfants")},
            cl_activite_pro = "{kwargs.get("cl_activite_pro")}",
            cl_mail = "{kwargs.get("cl_mail")}",
            cl_num_fixe = "{kwargs.get("cl_num_fixe")}",
            cl_num_mobile = "{kwargs.get("cl_num_mobile")}",
            cl_ville = "{kwargs.get("cl_ville")}",
            cl_adresse = "{kwargs.get("cl_adresse")}",
            cl_insee = "{kwargs.get("cl_insee")}",
            cl_date_crea = "{kwargs.get("cl_date_crea")}",
            cl_origine_crea = "{kwargs.get("cl_origine_crea")}",
            cl_notes = "{kwargs.get("cl_notes")}"
            WHERE cl_id = {kwargs.get("cl_id")}
            """)
        self.co.commit()
        self.close()
    def SUPPR_CLIENT(self, cl_id):
        self.cd.execute(
            f"""
            DELETE FROM t_clients
            WHERE cl_id = {cl_id}
            """)
        self.co.commit()

        self.cd.execute(
            f"""
            DELETE FROM t_contrat
            WHERE ct_cl_id = {cl_id}
            """)
        self.co.commit()

        self.close()

    def GET_COMP(self):
        self.cd.execute(
            f"""
            SELECT pt_compagnie
            FROM t_partenaires
            ORDER BY pt_compagnie
            """)
        return self.cd.fetchall()
    def GET_CONTRAT(self, ct_id):
        self.cd.execute(
            f"""
            SELECT *
            FROM t_contrat
            WHERE ct_id = {ct_id}
            """)
        return self.cd.fetchone()
    def ADD_CONTRAT(self, **kwargs):
        self.cd.execute(
            f"""
            INSERT INTO t_contrat(
            ct_ca_id,
            ct_cl_id,
            ct_date_ouverture,
            ct_compagnie,
            ct_nom_contrat,
            ct_prime_annuel,
            ct_commission)
            VALUES(
            {kwargs.get("ct_ca_id")},
            {kwargs.get("ct_cl_id")},
            "{kwargs.get("ct_date_ouverture")}",
            "{kwargs.get("ct_compagnie")}",
            "{kwargs.get("ct_nom_contrat")}",
            {kwargs.get("ct_prime_annuel")},
            {kwargs.get("ct_commission")})
            """)
        self.co.commit()
        self.close()
    def MODIF_CONTRAT(self, **kwargs):
        self.cd.execute(
            f"""
            UPDATE t_contrat 
            SET ct_date_ouverture = "{kwargs.get("ct_date_ouverture")}",
            ct_compagnie = "{kwargs.get("ct_compagnie")}",
            ct_nom_contrat = "{kwargs.get("ct_nom_contrat")}",
            ct_prime_annuel = {kwargs.get("ct_prime_annuel")},
            ct_commission = {kwargs.get("ct_commission")}
            WHERE ct_id = {kwargs.get("ct_id")}
            """)
        self.co.commit()
        self.close()
    def ADD_ENCOURS(self, **kwargs):
        self.cd.execute(
            f"""
            INSERT INTO t_contrat(
            ct_ca_id,
            ct_cl_id,
            ct_date_ouverture,
            ct_compagnie,
            ct_nom_contrat,
            ct_encours,
            ct_uc,
            ct_date_dernier_versement,
            ct_vp_annuel,
            ct_prime_annuel,
            ct_commission)
            VALUES(
            {kwargs.get("ct_ca_id")},
            {kwargs.get("ct_cl_id")},
            "{kwargs.get("ct_date_ouverture")}",
            "{kwargs.get("ct_compagnie")}",
            "{kwargs.get("ct_nom_contrat")}",
            {kwargs.get("ct_encours")},
            {kwargs.get("ct_uc")},
            "{kwargs.get("ct_date_dernier_versement")}",
            {kwargs.get("ct_vp_annuel")},
            {kwargs.get("ct_prime_annuel")},
            {kwargs.get("ct_commission")})
            """)
        self.co.commit()
        self.close()
    def MODIF_ENCOURS(self, **kwargs):
        self.cd.execute(
            f"""
            UPDATE t_contrat 
            SET ct_date_ouverture = "{kwargs.get("ct_date_ouverture")}",
            ct_compagnie = "{kwargs.get("ct_compagnie")}",
            ct_nom_contrat = "{kwargs.get("ct_nom_contrat")}",
            ct_encours = {kwargs.get("ct_encours")},
            ct_uc = {kwargs.get("ct_uc")},
            ct_date_dernier_versement = "{kwargs.get("ct_date_dernier_versement")}",
            ct_vp_annuel = {kwargs.get("ct_vp_annuel")},
            ct_prime_annuel = {kwargs.get("ct_prime_annuel")},
            ct_commission = {kwargs.get("ct_commission")}
            WHERE ct_id = {kwargs.get("ct_id")}
            """)
        self.co.commit()
        self.close()
    def SUPPR_CONTRAT(self, ct_id):
        self.cd.execute(
            f"""
            DELETE FROM t_contrat
            WHERE ct_id = {ct_id}
            """)
        self.co.commit()
        self.close()

    def DATE_DERNIER_CONTACT(self, cl_id, dt):
        self.cd.execute(
            f"""
            UPDATE t_clients 
            SET cl_date_dernier_contact = "{dt}"
            WHERE cl_id = {cl_id}
            """)
        self.co.commit()
        self.close()

    def GET_LAST_CLIENT(self):
        self.cd.execute(
            f"""
            SELECT MAX(cl_id)
            FROM t_clients
            """)
        return self.cd.fetchone()
    def MAJ_SELECT_V(self, vue, id_cl):
        self.cd.execute(
            f"""
            SELECT *
            FROM {vue}
            WHERE ct_cl_id = {id_cl}
            ORDER BY ct_id
            """)
        return self.cd.fetchall()

    def TEST_CO(self):
        self.cd.execute("SELECT * FROM t_partenaires")
        for i in self.cd.fetchall():
            print(i)

        self.close()
    def close(self):
        self.cd.close()
        self.co.close()
