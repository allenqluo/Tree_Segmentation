
# To install older version of lidR
# require(devtools)
# install_version("lidR", version = "3.1.4", repos = "http://cran.us.r-project.org")

library(lidR)
library(raster)

lasfile <- "./data/teak_data/lidarAOI_g.las"
las <- readLAS(lasfile)
las <- normalize_height(las, knnidw())
# Filter for above ground points only
# aboveground <- filter_poi(las, Classification != 2)

# Get CHM and smooth, then detect tree tops
chm_p2r_05 <- grid_canopy(las, 0.5, p2r(subcircle = 0.2))
kernel <- matrix(1,3,3)
chm_p2r_05_smoothed <- raster::focal(chm_p2r_05, w = kernel, fun = median, na.rm = TRUE)
ttops_chm_p2r_05 <- find_trees(chm_p2r_05, lmf(5))

ttops_chm_p2r_05_smoothed <- find_trees(chm_p2r_05_smoothed, lmf(5))
algo <- dalponte2016(chm_p2r_05_smoothed, ttops_chm_p2r_05_smoothed)

las_seg <- segment_trees(las, algo) # segment point cloud
plot(las_seg, bg = "white", size = 4, color = "treeID") # visualize trees

# Compute all metrics
metrics <- cloud_metrics(las_seg, func = .stdmetrics_z)

# Delineate each tree crown and get metrics
# crowns <- delineate_crowns(las_seg)
# crowns1 <- delineate_crowns(las_seg, func = .stdmetrics)
# Get the szn average and area (ZTOP is included in delineate_Crowns)
crowns <- delineate_crowns(las_seg, func = ~list(szn_avg = 90 - mean(abs(ScanAngleRank)),
                                                 area=(max(X)-min(X)) * (max(Y)-min(Y))))

# Compute average crown diameter
crowns[["hrad"]] <- sqrt(crowns[["area"]]/ pi)
crowns[["vrad"]] <-  crowns[["ZTOP"]] / 2

# Save delineated tree crowns
library(rgdal)
writeOGR(crowns, "./data/output/teak_crowns", "crowns", 
         driver = "ESRI Shapefile") #also you were missing the driver argument
