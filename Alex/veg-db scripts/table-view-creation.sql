
-- lets save some data (use WHERE "siteID"='WREF')
\copy (SELECT *                  
FROM neonveg.vst_apparentindividual_xy WHERE "siteID"='NIWO') TO '/data/shared/src/arojas/veg-db/data/output/neon-niwo-appidv-xy.csv' DELIMITER ',' CSV HEADER;

\copy (SELECT * 
FROM neonveg.vst_mappingandtagging_xy WHERE "siteID"='NIWO') TO '/data/shared/src/arojas/veg-db/data/output/neon-niwo-mandt-xy.csv' DELIMITER ',' CSV HEADER;

-- the total should be 1760 for WREF
SELECT COUNT(*)
FROM neonveg.vst_apparentindividual AS t1
LEFT JOIN neonveg.vst_apparentindividual AS t2 ON
(
    t2."individualID" = t1."individualID" AND t2."date" > t1."date"
)
WHERE t2."individualID" IS NULL AND t1."siteID"='WREF';

-- Select latest dates for mapping and tagging (WREF total 3634)
SELECT COUNT(t1.*)
FROM neonveg.vst_mappingandtagging AS t1
LEFT JOIN neonveg.vst_mappingandtagging AS t2 ON
(
    t2."individualID" = t1."individualID" AND t2."date" > t1."date"
)
WHERE t2."individualID" IS NULL AND t1."siteID"='WREF';

------

-- fetching latest mapping and tagging data
WITH m AS (
SELECT t1.*
FROM neonveg.vst_mappingandtagging AS t1
LEFT JOIN neonveg.vst_mappingandtagging AS t2 ON
(
    t2."individualID" = t1."individualID" AND t2."date" > t1."date"
)
WHERE t2."individualID" IS NULL AND t1."siteID"='WREF'
)
-- add latest observation data
appidv as (
SELECT t1.*                         
FROM neonveg.vst_appidv AS t1
LEFT JOIN neonveg.vst_appidv AS t2 ON
(
    t2."individualID" = t1."individualID" AND t2."date" > t1."date"
)
WHERE t2."individualID" IS NULL AND t1."siteID"='WREF'
)
SELECT appidv.*, m."plotID", m."pointID", 
FROM appidv, m;

------

-- joining the mapping data with the spatial plots to get exact coordinates of trees
CREATE OR REPLACE VIEW neonveg.vst_mappingandtagging_xy AS
WITH m AS (
	SELECT t1.*, CONCAT(t1."plotID", '.', t1."pointID") as plotptid
	FROM neonveg.vst_mappingandtagging AS t1
	LEFT JOIN neonveg.vst_mappingandtagging AS t2 ON
		(
    			t2."individualID" = t1."individualID" AND t2."date" > t1."date"
		)
	WHERE t2."individualID" IS NULL -- AND t1."siteID"='WREF'
),
p AS (
	SELECT *, CONCAT("plotID", '.', "pointID") as plotptid
	FROM public.neon_tos_plot_points
	WHERE "crdSource" != 'GIS' AND "subtype"='basePlot'
)
SELECT m.*, p."elevation",
p."utmZone",p."horzUncert",p."vertUncert", p."latitude" as plot_lat, p."longitude" as plot_lon,
p."easting" + m."stemDistance"*sin((m."stemAzimuth"*pi())/180) as easting,
p."northing" + m."stemDistance"*cos((m."stemAzimuth"*pi())/180) as northing
FROM m
LEFT JOIN p
ON m.plotptid = p.plotptid;



-- Simple join of mappingandtagging_xy view with the appidv table
CREATE OR REPLACE VIEW neonveg.vst_apparentindividual_xy AS
SELECT a.*, m."subplotID",m."taxonID", m."scientificName", m.easting, m.northing
FROM neonveg.vst_apparentindividual as a
LEFT JOIN neonveg.vst_mappingandtagging_xy as m
	ON a."individualID" = m."individualID";

-- Drop view
-- DROP VIEW neonveg.vst_apparentindividual_xy;


----------------------

-- Get latest non null data for each data column
SELECT DISTINCT 
"individualID","plotID","subplotID","domainID","siteID",
        FIRST_VALUE("stemDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "stemDiameter" is NULL then 0 else 1 END DESC, date desc) AS "stemDiameter",
        FIRST_VALUE(height) OVER(PARTITION BY "individualID" ORDER BY CASE WHEN height is NULL then 0 else 1 END DESC, date desc) AS height,
        FIRST_VALUE("baseCrownHeight") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "baseCrownHeight" is NULL then 0 else 1 END DESC, date desc) AS "baseCrownHeight",
        FIRST_VALUE("maxCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "maxCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "maxCrownDiameter",
        FIRST_VALUE("ninetyCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "ninetyCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "ninetyCrownDiameter",
        FIRST_VALUE("maxBaseCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "maxBaseCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "maxBaseCrownDiameter",
        FIRST_VALUE("ninetyBaseCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "ninetyBaseCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "ninetyBaseCrownDiameter",
        "taxonID",
        "scientificName", "easting",
        "northing"
FROM neonveg.vst_apparentindividual_xy;



-- sanity check
SELECT "individualID", "date", "height", "maxCrownDiameter" FROM neonveg.vst_apparentindividual_xy WHERE "individualID"='NEON.PLA.D01.BART.00004';

SELECT "individualID", "date", "height", "maxCrownDiameter" FROM neonveg.vst_apparentindividual_xy WHERE "individualID"='NEON.PLA.D01.BART.00021' AND (date >= TO_DATE('2016', 'YYYY') and date < TO_DATE('2018', 'YYYY'));

-- Lets create a function to call data
CREATE OR REPLACE FUNCTION totalRecords ()
RETURNS integer AS $total$
declare
	total integer;
BEGIN
   SELECT count(*) into total FROM neonveg.vst_apparentindividual_xy;
   RETURN total;
END;
$total$ LANGUAGE plpgsql;

------------------

---------------
-- SCRATCH
---------------

\copy (SELECT DISTINCT 
"individualID","plotID","subplotID","domainID", "siteID",
        FIRST_VALUE("stemDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "stemDiameter" is NULL then 0 else 1 END DESC, date desc) AS "stemDiameter",
        FIRST_VALUE(height) OVER(PARTITION BY "individualID" ORDER BY CASE WHEN height is NULL then 0 else 1 END DESC, date desc) AS height,
        FIRST_VALUE("baseCrownHeight") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "baseCrownHeight" is NULL then 0 else 1 END DESC, date desc) AS "baseCrownHeight",
        FIRST_VALUE("maxCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "maxCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "maxCrownDiameter",
        FIRST_VALUE("ninetyCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "ninetyCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "ninetyCrownDiameter",
        FIRST_VALUE("maxBaseCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "maxBaseCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "maxBaseCrownDiameter",
        FIRST_VALUE("ninetyBaseCrownDiameter") OVER(PARTITION BY "individualID" ORDER BY CASE WHEN "ninetyBaseCrownDiameter" is NULL then 0 else 1 END DESC, date desc) AS "ninetyBaseCrownDiameter",
        "taxonID",
        "scientificName", "easting",
        "northing"
FROM neonveg.vst_apparentindividual_xy) to '/data/shared/src/arojas/veg-db/data/output/appidv_xy_all_latest.csv' DELIMITER ',' CSV HEADER;



\copy (SELECT * FROM neonveg.vst_apparentindividual_xy WHERE "growthForm" = 'single bole tree' OR "growthForm" = 'multi-bole tree' OR "growthForm" = 'small tree' AND "date" > '2019-12-31') to '/data/shared/src/arojas/NEON/veg-db/data/output/NEON_VST_TREES_2020to2023.csv' DELIMITER ',' CSV HEADER;

\copy (SELECT * FROM neonveg.vst_apparentindividual_xy WHERE "growthForm" = 'single bole tree' OR "growthForm" = 'multi-bole tree' OR "growthForm" = 'small tree') to '/data/shared/src/arojas/NEON/veg-db/data/output/NEON_VST_TREES.csv' DELIMITER ',' CSV HEADER;


