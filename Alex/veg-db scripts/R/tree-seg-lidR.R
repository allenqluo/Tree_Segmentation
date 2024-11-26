
# To install older version of lidR
# require(devtools)
# install_version("lidR", version = "3.1.4", repos = "http://cran.us.r-project.org")

setwd("/data/shared/src/arojas/NEON/veg-db/scripts")
library(lidR)
library(raster)
library(stringr)

fd <- "/data/shared/src/arojas/NEON/data/baseplots-lidar"
las_files <- list.files(fd, pattern = '*\\.las')

dirs_sitebp <- list.dirs(path = fd, full.names = TRUE, recursive = FALSE)

for (fdir_site in dirs_sitebp) {
  # print(fdir_site)
  fdir_str <- file.path(fdir_site,"*")
  fdirs_years <- Sys.glob(fdir_str)
  print(fdir_site)
  for (fdir_yr in fdirs_years) {
    print(fdir_yr)
  }
} 










################
################
################
################


for(fn in las_files){
  

  
  # Get coords to save output filename
  coords <- str_extract(fn, "[0-9]{6}_[0-9]{7}")
  outfile<-sprintf("./data/output/raster/crowns/tree-seg-%s.tif",coords)
  print(coords)
  # read las data
  lasfile <- paste(fd,fn,sep="")
  las <- readLAS(lasfile)
  # dir.create(file.path("./data/output/crowns", ))
  # normalize
  las <- normalize_height(las, knnidw())
  
  # Local Maximum Filter on a CHM
  # Get CHM and smooth, then detect tree tops
  chm_p2r_05 <- grid_canopy(las, 0.5, p2r(subcircle = 0.2))
  kernel <- matrix(1,3,3)
  chm_p2r_05_smoothed <- raster::focal(chm_p2r_05, w = kernel, fun = median, na.rm = TRUE)
  # lmf(5)
  ttops_chm_p2r_05 <- find_trees(chm_p2r_05, lmf(5))
  
  ttops_chm_p2r_05_smoothed <- find_trees(chm_p2r_05_smoothed, lmf(5))
  
  # algo <- dalponte2016(chm_p2r_05_smoothed, ttops_chm_p2r_05_smoothed)
  algo <- silva2016(chm_p2r_05_smoothed, ttops_chm_p2r_05_smoothed)
  # algo <- silva2016(chm_p2r_05, ttops_chm_p2r_05)
  # write and save raster
  crowns_raster <- algo()
  writeRaster(crowns_raster,outfile)
  
}


