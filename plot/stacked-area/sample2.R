#!/usr/bin/Rscript

#options(echo=TRUE)
# trailingOnly=TRUE means that only your arguments are returned
args <- commandArgs(trailingOnly = TRUE)
print(args)
src <- args[1]
#N <- as.numeric(args[2])

data <- read.table(src, na.strings = "NA", fill = TRUE, header=TRUE)
print(data)

data <- reshape(data,
                varying = c("castiron", "steel", "plastic"),
                v.names = "mmiles",
                timevar = "material",
                times = c("castiron", "steel", "plastic"),
                direction = "long")
 
data <- subset(data, select = -c(id))
print(data)

library(ggplot2)

graph = ggplot(data, aes(x = year, y = mmiles, fill = material)) + 
        geom_area(position = 'stack') 
#        geom_area(position = 'stack') +
#        labs(x = "Year", 
#             y = "Total Miles of Pipeline in Millions",
#             title = "Composition of Natural Gas Pipeline Material in the United States") +
#        scale_fill_discrete(name = "Material", 
#                            breaks = c("plastic", "steel", "castiron"),
#                            labels = c("Plastic", "Steel", "Cast Iron")) +
#        theme(axis.text = element_text(size = 12, color = 'black'),
#              axis.title = element_text(size = 14, face = 'bold'),
#              legend.title = element_text(size = 14, face = 'bold'),
#              legend.text = element_text(size = 12),
#              plot.title = element_text(size = 18, face = 'bold'))
 
png("sample2.png")
plot(graph)
