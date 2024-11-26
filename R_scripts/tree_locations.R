vst <- loadByProduct(dpID="DP1.10098.001", 
                     site="TEAK",
                     check.size=F)

View(vst$vst_perplotperyear)

vst.trees <- vst$vst_perplotperyear[which(
  vst$vst_perplotperyear$treesPresent=="Y"),]

# make variable for plot sizes
plot.size <- numeric(nrow(vst.trees))

# populate plot sizes in new variable
plot.size[which(vst.trees$plotType=="tower")] <- 40
plot.size[which(vst.trees$plotType=="distributed")] <- 20

# create map of plots
symbols(vst.trees$easting,
        vst.trees$northing,
        squares=plot.size, inches=F,
        xlab="Easting", ylab="Northing")

View(vst$vst_mappingandtagging)

# calculate individual tree locations
vst.loc <- getLocTOS(data=vst$vst_mappingandtagging,
                     dataProd="vst_mappingandtagging")
View(vst.loc)

vst.2022_loc <- subset(vst.loc, !grepl("2015", date))
View(vst.2022_loc)

# print variable names that are new
names(vst.loc)[which(!names(vst.loc) %in% 
                       names(vst$vst_mappingandtagging))]


plot(vst.loc$adjEasting, vst.loc$adjNorthing, 
     pch=".", xlab="Easting", ylab="Northing")


plot(vst.loc$adjEasting[which(vst.loc$plotID=="TEAK_046")], 
     vst.loc$adjNorthing[which(vst.loc$plotID=="TEAK_046")], 
     pch=20, xlab="Easting", ylab="Northing")

text(vst.loc$adjEasting[which(vst.loc$plotID=="TEAK_046")], 
     vst.loc$adjNorthing[which(vst.loc$plotID=="TEAK_046")],
     labels=vst.loc$taxonID[which(vst.loc$plotID=="TEAK_046")],
     cex=1)


plot(vst.2022_loc$adjEasting[which(vst.2022_loc$plotID=="TEAK_015")], 
     vst.2022_loc$adjNorthing[which(vst.2022_loc$plotID=="TEAK_015")], 
     pch=20, xlab="Easting", ylab="Northing")

text(vst.2022_loc$adjEasting[which(vst.2022_loc$plotID=="TEAK_015")], 
     vst.2022_loc$adjNorthing[which(vst.2022_loc$plotID=="TEAK_015")],
     labels=vst.2022_loc$taxonID[which(vst.2022_loc$plotID=="TEAK_015")],
     cex=1)

write.csv(vst.2022_loc, "C:/Users/allen/OneDrive/Desktop/Work/Scripts/Tree Segmentation/R_scripts/tree_locations.csv", row.names = FALSE)