# cleaning and transformation process

lt_house <- function(houses)
{
  colnames(houses)<- tolower(colnames(houses))
  
  
  houses
}