train_titanic <- read.csv("~/GitHub/Data-Science/Datasets/train_titanic.csv", stringsAsFactors=FALSE)


train_titanic$Title <- gsub('(.*, )|(\\..*)', '', train_titanic$Name)
table(train_titanic$Sex, train_titanic$Title)

rare_title <- c('Dona', 'Lady', 'the Countess','Capt', 'Col', 'Don', 
                'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer')

# Also reassign mlle, ms, and mme accordingly
train_titanic$Title[train_titanic$Title == 'Mlle']        <- 'Miss' 
train_titanic$Title[train_titanic$Title == 'Ms']          <- 'Miss'
train_titanic$Title[train_titanic$Title == 'Mme']         <- 'Mrs' 
train_titanic$Title[train_titanic$Title %in% rare_title]  <- 'Rare Title'

# Show title counts by sex again
table(train_titanic$Sex, train_titanic$Title)


# Finally, grab surname from passenger name
train_titanic$Surname <- sapply(train_titanic$Name,  
                       function(x) strsplit(x, split = '[,.]')[[1]][1])
cat(paste('We have <b>', nlevels(factor(full$Surname)), '</b> unique surnames. I would be interested to infer ethnicity based on surname --- another time.'))