set client_min_messages = 'WARNING';
-- postgis-users/2006-January/010870.html
CREATE TEMP TABLE tmp (orig geometry);
INSERT INTO tmp (orig) VALUES ('01020000207D18000007000000D7A3701D641B3FC18B6CE7FB5A721841FA7E6A9C5E1B3FC191ED7C3F9872184139B4C816591B3FC1E3A59BC4D472184104560E4D891A3FC177BE9F1ABF7118417B14AEA7961A3FC18716D94E0C711841022B8716671B3FC1C74B370939721841D7A3701D641B3FC18B6CE7FB5A721841');

-- Repeat tests with new function names.
SELECT ST_snaptogrid(orig, 0.001) ~= ST_snaptogrid(ST_snaptogrid(orig, 0.001), 0.001) FROM tmp;
SELECT ST_snaptogrid(orig, 0.005) ~= ST_snaptogrid(ST_snaptogrid(orig, 0.005), 0.005) FROM tmp;
SELECT ST_snaptogrid(orig, 0.002) ~= ST_snaptogrid(ST_snaptogrid(orig, 0.002), 0.002) FROM tmp;
SELECT ST_snaptogrid(orig, 0.003) ~= ST_snaptogrid(ST_snaptogrid(orig, 0.003), 0.003) FROM tmp;
SELECT ST_snaptogrid(orig, 0.0002) ~= ST_snaptogrid(ST_snaptogrid(orig, 0.0002), 0.0002) FROM tmp;
DROP TABLE tmp;

-- The geometry bbox is updated
WITH geom AS
(
    SELECT ST_SnapToGrid('POLYGON((0 0, 10 0, 10 10, 10.6 10, 10.5 10.5, 10 10, 0 10, 0 0))', 10) as g
    UNION ALL
    SELECT ST_SnapToGrid('POLYGON((0 0, 10 0, 10 10, 10.6 10, 10.5 10.5, 10 10, 0 10, 0 0))', 'POINT(0 0)', 10, 10, 10, 10) as g
)
Select ST_AsText(g) as geometry, postgis_getbbox(g) AS box from geom;
reset client_min_messages;


-- #5241
SELECT '#5241' AS t, ST_AsText(ST_SnapToGrid( ST_GeomFromText('MULTIPOLYGON (((9 9, 9 1, 1 1, 2 4, 7 7, 9 9)), EMPTY)', 4326),  20.1, 20.1, 20.1, 20.1));
SELECT '#5241' AS t, ST_AsText(ST_SnapToGrid( ST_GeomFromText('MULTIPOLYGON (((9 9, 9 1, 1 1, 2 4, 7 7, 9 9)), EMPTY)', 4326), 1, 1, 1, 1));
