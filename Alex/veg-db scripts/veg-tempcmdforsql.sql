
CREATE TEMP TABLE tmp AS SELECT * FROM neonveg.vst_mappingandtagging LIMIT 0; \COPY tmp FROM '/data/shared/src/arojas/NEON/veg-db/scripts/veg-temp/YELL.DP1.10098.001.2022-09/NEON.D12.YELL.DP1.10098.001.vst_mappingandtagging.basic.20230306T220653Z.csv' CSV HEADER;
INSERT INTO neonveg.vst_mappingandtagging AS mandt 
    SELECT * FROM tmp
ON CONFLICT DO NOTHING;
    