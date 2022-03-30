-- Insertion d'une nouvelle zone
INSERT INTO t_zone_dlg (zo_marche,zo_nro,zo_pm,zo_refcode3)
SELECT 24, 22, 8, 'BIMI'
WHERE NOT EXISTS(
    SELECT zo_refcode3
    FROM t_zone_dlg
    WHERE zo_refcode3 = 'BIMI'
    );

-- Insertion d'un nouveau dlg
INSERT INTO t_dlg (dl_zo_id,dl_init_date,dl_phase,dl_td,dl_no_livraison,dl_no_version)
SELECT (SELECT dlg.zo_id FROM t_zone_dlg dlg WHERE dlg.zo_refcode3 = 'BIMI') AS zo, '29/03/2022', 'EXE', 'TD', 1, 1
WHERE NOT EXISTS(
    SELECT dl_phase,dl_td,dl_no_livraison,dl_no_version
    FROM t_dlg
    WHERE dl_zo_id = zo
    AND dl_phase = 'EXE'
    AND dl_td = 'TD'
    AND dl_no_livraison = 1
    AND dl_no_version = 1
    );




-- Select table
SELECT * FROM t_zone_dlg;
SELECT * FROM t_dlg;

-- Delete table
DELETE FROM t_zone_dlg;
DELETE FROM t_dlg;

