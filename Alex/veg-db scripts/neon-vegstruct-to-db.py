# Import necessary libraries
import neonutilities
import glob
import argparse
import sys
import os
import subprocess
import shutil

# --------------------------COMMAND LINE ARGUMENTS AND ERROR HANDLING---------------------------- #
# Set up argument and error handling
parser = argparse.ArgumentParser(description='Downloads and uploads data')
parser.add_argument('--site', required=True, help='NEON site code e.g. NIWO')
parser.add_argument('--year', required=False, help="Year to download data.")
args = parser.parse_args()

# --------------------------------SET ARGUMENTS TO VARIABLES------------------------------------- #
# veg structure product
vegprod = "DP1.10098.001"

# get site
siteid = args.site
year = args.year

if year is None:
    siteurls = neonutilities.api.list_available_urls(vegprod,siteid)
else:
    siteurls = neonutilities.api.list_available_urls_by_year(vegprod,siteid,year)

# Get relative path from this file (wherever the python script is located is the dirname)
dirname = os.path.dirname(__file__)
vegdir = os.path.join(dirname, "veg-temp")
if not os.path.exists(vegdir):
    os.makedirs(vegdir)

# Lets download data
neonutilities.api.download_urls(siteurls,download_folder_root=f"{vegdir}/",
                                zip=False)

# get the subdirs where data was downloaded (e.g. 2021-09)
list_of_dirs = glob.glob(f"{vegdir}/*")

if len(list_of_dirs)==0:
    print("No veg-struct data downloaded for site: ", siteid)
    shutil.rmtree(vegdir)
    sys.exit(1)

# Loop through each folder, get the appindv and upload to vegdb
for subdir in list_of_dirs:
    # get vstappidv
    appidv = glob.glob(subdir+"/*apparentindividual*")
    if len(appidv)==0:
        continue
    # get absolute path
    appidv = os.path.abspath(appidv[0])

    # Generate command string
    cmd_str = """
CREATE TEMP TABLE tmp AS SELECT * FROM neonveg.vst_apparentindividual LIMIT 0; \COPY tmp FROM '{0}' CSV HEADER;
insert into neonveg.vst_apparentindividual
    SELECT * FROM tmp
ON CONFLICT DO NOTHING;
    """.format(appidv)
    sqlfile = open(vegdir+"cmdforsql.sql","w")
    sqlfile.write(cmd_str)
    sqlfile.close()

    # Now upload into cuny db neonveg schema
    cmdList = f"PGPASSWORD=80Fx-reS psql -d cuny -U cuny -a -f '{vegdir}cmdforsql.sql'"
    subprocess.run(cmdList,shell=True,stdout=subprocess.DEVNULL)

# Loop through each folder, get the mappingandtagging and upload to vegdb
for subdir in list_of_dirs:
    # get vstappidv
    mandt = glob.glob(subdir+"/*mappingandtagging*")
    if len(mandt)==0:
        print("No mappingandtagging table for year: ", subdir)
        continue
    # get absolute path
    mandt = os.path.abspath(mandt[0])

    # Generate command string
    cmd_str = """
CREATE TEMP TABLE tmp AS SELECT * FROM neonveg.vst_mappingandtagging LIMIT 0; \COPY tmp FROM '{0}' CSV HEADER;
INSERT INTO neonveg.vst_mappingandtagging AS mandt 
    SELECT * FROM tmp
ON CONFLICT DO NOTHING;
    """.format(mandt)
    sqlfile = open(vegdir+"cmdforsql.sql","w")
    sqlfile.write(cmd_str)
    sqlfile.close()

    # Now upload into cuny db neonveg schema
    cmdList = f"PGPASSWORD=80Fx-reS psql -d cuny -U cuny -a -f '{vegdir}cmdforsql.sql'"
    subprocess.run(cmdList,shell=True,stdout=subprocess.DEVNULL)

# Clean working space (remove temp dir for veg-struc, etc.)
shutil.rmtree(vegdir)