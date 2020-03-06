library(ggplot2)
library(tidyr)
library(dplyr)
library(jpeg)
library(officer)
library(EBImage)
library(broom)
library(purrr)
library(flextable)

#1)positive control (isotype vs minimal conc)
#read the file and preprocess:
setwd('C:/Users/korostelevaas/PycharmProjects/cytometry')
data<-as.data.frame(read.delim(file=file.choose(), sep = ";", header=F, dec = ","))
data <- tail(data,-2)
names <- c('Tube', 'Sample ID', 'live singlets Events', 'live singlets Median PE-A')
colnames(data) <- names
unstained <- grep('unstained', data$Tube)
isotype <- grep('isotype', data$Tube)
zero <- grep('-0-', data$Tube)
minimal <- grep('-3.09-', data$Tube
                )
indexes <- c(unstained, isotype, zero, minimal)
data <- data[indexes, ]
data$`live singlets Median PE-A` <- sapply(as.vector(data$`live singlets Median PE-A`),
                                           gsub, pattern = ",", replacement= ".")
#choose isotype and minimal_conc from data

isotype <- grep('isotype', data$Tube)
isotype <- data[isotype, ]
isotype <- as.numeric(as.vector(isotype$`live singlets Median PE-A`))
isotype1 <- isotype[1:3]
isotype2 <- isotype[4:6]
isotype3 <- isotype[7:9]
isotype4 <- isotype[10:12]
min_conc <- grep('-3.09-', data$Tube)
min_conc <- data[min_conc,]
 

min_conc <- as.numeric(as.vector(min_conc$`live singlets Median PE-A`))
min_conc1 <- min_conc[1:3]
min_conc2 <- min_conc[4:6]
min_conc3 <- min_conc[7:9]
min_conc4 <- min_conc[10:12]
##boxplot for measurments:
#isotype1
isotype1 <- data.frame(group = "isotype", value = isotype1)
min_conc1 <- data.frame(group = "min_conc", value = min_conc1)
plot.data1 <- rbind(isotype1, min_conc1)


jpeg('plot1.jpeg')
ggplot(plot.data1, aes(x=group, y=value, fill=group)) + geom_boxplot() +
  ggtitle("Boxplot comparison: isotype cntrl vs min.concentration ST1")+
  labs(y="Value, RFU", x = "Group")
dev.off() 

ttest_iso1 <- t.test(isotype1$value, min_conc1$value)

#report difference if p<0.05 AND boxplot shows intersection for data
#2
isotype2 <- data.frame(group = "isotype", value = isotype2)
min_conc2 <- data.frame(group = "min_conc", value = min_conc2)
plot.data <- rbind(isotype2, min_conc2)


jpeg('plot2.jpeg')
ggplot(plot.data, aes(x=group, y=value, fill=group)) + geom_boxplot() +
  ggtitle("Boxplot comparison: isotype cntrl vs min.concentration ST2")+
  labs(y="Value, RFU", x = "Group")

dev.off() 

ttest_iso2 <- t.test(isotype2$value, min_conc2$value)
ttest_iso2
#3
isotype3 <- data.frame(group = "isotype", value = isotype3)
min_conc3 <- data.frame(group = "min_conc", value = min_conc3)
plot.data <- rbind(isotype3, min_conc3)



jpeg('plot3.jpeg')
ggplot(plot.data, aes(x=group, y=value, fill=group)) + geom_boxplot() +
  ggtitle("Boxplot comparison: isotype cntrl vs min.concentration ST3")+
  labs(y="Value, RFU", x = "Group")
dev.off() 

ttest_iso3 <- t.test(isotype3$value, min_conc3$value)
ttest_iso3

#4

isotype4 <- data.frame(group = "isotype", value = isotype4)
min_conc4 <- data.frame(group = "min_conc", value = min_conc4)
plot.data <- rbind(isotype4, min_conc4)


jpeg('plot4.jpeg')
ggplot(plot.data, aes(x=group, y=value, fill=group)) + geom_boxplot() +
  ggtitle("Boxplot comparison: isotype cntrl vs min.concentration ST4")+
  labs(y="Value, RFU", x = "Group")
dev.off() 

ttest_iso4 <- t.test(isotype4$value, min_conc4$value)
ttest_iso4

#table
tab <- map_df(list(ttest_iso1, ttest_iso2, ttest_iso3, ttest_iso4), tidy)
tab$sample <- c('ST_1', 'ST_2', 'ST_3', 'ST_4')
tab <- cbind(tab$sample, tab$p.value, tab$conf.low, tab$conf.high, tab$method, tab$alternative)
colnames(tab) <- c('Name', 'p-value', 'High_conf', 'Low_conf', 'Method', 'Alternative')
table <- flextable(as.data.frame(tab))


#2) Unstained vs negative control

unstained <- grep('unstained', data$Tube)
unstained <- data[unstained, ]
unstained1 <- as.numeric(as.vector(unstained$`live singlets Median PE-A`[1:6]))

unstained2 <- as.numeric(as.vector(unstained$`live singlets Median PE-A`[7:12]))
negative <- grep('-0-', data$Tube)
negative <- data[negative,]
negative <- as.numeric(as.vector(negative$`live singlets Median PE-A`))
negative1 <- negative[1:6]
negative2 <- negative[7:12]

#choose unstained and negative controlfrom data
wilc1 <- wilcox.test(unstained1, negative1)
wilc2 <- wilcox.test(unstained2, negative2)
tab_wilc <- map_df(list(wilc1, wilc2), tidy)
tab_wilc$sample <- c('PLATE_1', 'PLATE_2')


tab_wilc <- cbind(tab_wilc$sample, format(round(tab_wilc$p.value, 4), nsmall = 2),tab_wilc$method, tab_wilc$alternative)
colnames(tab_wilc) <- c('Name', 'p-value', 'Method', 'Alternative')
wil_table <- flextable(as.data.frame(tab_wilc))


#report difference if p>0.001

#Report generating

#img = readImage("C:/Users/path_to_directory_there_picture_should_be/rplot.jpg")

my_doc <- read_docx() 
my_doc <- my_doc %>% 
  body_add_par( 'Operating controls in cytometry analysis', style = "Normal") %>%
  body_add_par("", style = "Normal") %>%
  body_add_par("PART 1. Isotypic control vs minimal concentration", style = "Normal") %>% 
  body_add_img(src = 'plot1.jpeg', width = 6, height = 6)  %>%
  body_add_par("", style = "Normal") %>%
  body_add_img(src = 'plot2.jpeg', width = 6, height = 6)  %>%
  body_add_par("", style = "Normal") %>%
  body_add_img(src = 'plot3.jpeg', width = 6, height = 6)  %>%
  body_add_par("", style = "Normal") %>%
  body_add_img(src = 'plot4.jpeg', width = 6, height = 6)  %>%
  body_add_par("", style = "Normal") %>%
  body_add_par( "Student's t-test results", style = "Normal") %>%
  body_add_flextable(table) %>%
  body_add_par("", style = "Normal") %>%
  body_add_par("PART 2. Unstained vs negative control", style = "Normal") %>% 
  body_add_par("", style = "Normal") %>%
  body_add_flextable(wil_table)
  
 
print(my_doc, target = 'C:/Users/korostelevaas/PycharmProjects/cytometry/report.docx')



