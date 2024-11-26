# Import files
import neonutilities
import os
# import pandas as pd
# import glob
# import numpy as np

vegprod = "DP1.10098.001"

siteid = "TEAK"
url_list = neonutilities.api.list_available_urls("DP1.10098.001",siteid)

# print (url_list)

dirname = os.path.dirname(__file__)
# vegdir = os.path.join(dirname, "NEON_struct-plant")
vegdir = os.path.join(dirname, "data")
if not os.path.exists(vegdir):
    os.makedirs(vegdir)
    
# print(vegdir)

neonutilities.api.download_urls(url_list,download_folder_root=f"{vegdir}/", zip=False)