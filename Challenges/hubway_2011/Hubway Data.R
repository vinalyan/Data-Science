#install.packages("rgdal")
#install.packages("sp")
#install.packages("raster")
library(ggplot2)
library(sp)
library(rgdal)
library(raster)

hubway_trips <- read.csv("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/hubway_trips.csv")
hubway_stations <- read.csv("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/hubway_stations.csv")
crime_boston <- read.csv("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/crime.csv")


# Who's using the bikes?

table(hubway_trips$gender)
#         Female   Male 
# 472611 271700 834714

# Older or younger people?

summary(hubway_trips$birth_date)

#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
#    1932    1969    1979    1976    1985    1995 1228381 
hubway_trips_cop <- hubway_trips
hubway_trips_cop$age <- 2013 - hubway_trips_cop$birth_date
hubway_trips_cop <- hubway_trips_cop[!is.na(hubway_trips_cop$age),]
hubway_trips_cop$age <- ifelse(hubway_trips_cop$age<35, "young", "old")
table(hubway_trips_cop$age)
# old  young 
# 165636 185008 

# Subscribers or one time users?

table(hubway_trips$subsc_type)

#   Casual Registered 
#   472611    1106414 

# Where are bikes being checked out?
# More in Boston than Cambridge?
hubway_trips_c <- hubway_trips
names(hubway_trips_c)[6] <- "id"
hubway_data_with_gps <- merge(hubway_trips_c, hubway_stations, by = "id")

table(hubway_data_with_gps[hubway_data_with_gps$municipal %in% c("Boston", "Cambridge"),]$municipal)
# Boston  Brookline  Cambridge Somerville 
# 1221956          0     296778          0 

# Crime analysis

# what are the most offensive actions reported in 2015?

order(table(crime_boston$OFFENSE_CODE_GROUP))

names(crime_boston)[15] <- "lat"
names(crime_boston)[16] <- "lng"

hubway_crime_trips <- merge(hubway_stations, crime_boston, by = c("lng"))

tail(sort(table(crime_boston[crime_boston$YEAR == min(crime_boston$YEAR),]$OFFENSE_CODE_GROUP)))

#Vandalism              Medical Assistance                  Drug Violation                           Other 
#2701                            3139                            3300                            3379 
#Larceny                  Motor Vehicle Accident Response 
#5006                            5827                       



xy2 <- crime_boston[crime_boston$YEAR == min(crime_boston$YEAR),c("lng","lat")]
xy2 <- xy2[complete.cases(xy2),]
colnames(xy2) <- c("longitude", "latitude")
spdf2 <- SpatialPointsDataFrame(coords = xy2, data = xy2,
                               proj4string = CRS("+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0"))
s <- shapefile("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/neighborhood/Boston_Neighborhoods.shp")

proj4string(s)
proj4string(spdf2)

plot(s)
plot(spdf2, col="red" , add=TRUE)

res <- over(spdf2, s)
table(res$Name) # count points


# -------------recreation ----------- ##

xy <- hubway_stations[,c("lng","lat")]
colnames(xy) <- c("longitude", "latitude")
spdf <- SpatialPointsDataFrame(coords = xy, data = hubway_stations,
                              proj4string = CRS("+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0"))

# https://data.boston.gov/dataset/open-space
# https://gis.stackexchange.com/questions/133625/checking-if-points-fall-within-polygon-shapefile
# https://data.boston.gov/dataset/open-space/resource/769c0a21-9e35-48de-a7b0-2b7dfdefd35e
s <- shapefile("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/recreation/Open_Space.shp")
#s <- shapefile("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/ot/tl_2015_25_cousub.shp")

proj4string(s)
proj4string(spdf)

plot(s)
plot(spdf, col="red" , add=TRUE)

res <- over(spdf, s)
table(res$ZonAgg) # count points




## -------------neighborhoolds--------------------###

s <- shapefile("~/GitHub/Data-Science/Challenges/hubway_2011/dataset/neighborhood/Boston_Neighborhoods.shp")

proj4string(s)
proj4string(spdf)

plot(s)
plot(spdf, col="red" , add=TRUE)

res <- over(spdf, s)
table(res$Name) # count points



## ---------------------------------###

# python
# https://stackoverflow.com/questions/7861196/check-if-a-geopoint-with-latitude-and-longitude-is-within-a-shapefile/13433127#13433127



library("raster")
library("sp")

x <- getData('GADM', country='ITA', level=1)
class(x)
# [1] "SpatialPolygonsDataFrame"
# attr(,"package")
# [1] "sp"

set.seed(1)
# sample random points
p <- spsample(x, n=300, type="random")
p <- SpatialPointsDataFrame(p, data.frame(id=1:300))
proj4string(x)
# [1] " +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs +towgs84=0,0,0"
proj4string(p)
# [1] " +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs +towgs84=0,0,0"

plot(x)
plot(p, col="red" , add=TRUE)
res <- over(p, x)
table(res$NAME_1) # count points

mydf <- structure(list(longitude = c(128.6979, 153.0046, 104.3261, 124.9019, 
                                     126.7328, 153.2439, 142.8673, 152.689), latitude = c(-7.4197, 
                                                                                          -4.7089, -6.7541, 4.7817, 2.1643, -5.65, 23.3882, -5.571)), .Names = c("longitude", 
                                                                                                                                                                 "latitude"), class = "data.frame", row.names = c(NA, -8L))
