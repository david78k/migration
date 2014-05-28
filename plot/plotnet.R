#!/usr/bin/Rscript

src = ""

library(ggplot2)

require(devEMF)

png("aapl.png")
postscript("aapl.eps")
emf('aapl.emf')

aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
aapl = aapl[nrow(aapl):1, ]

#print(aapl)
#print(aapl.google)
print(aapl[, 1])

#matplot(aapl[,1], aapl[,5], type = "l", col="red")
#plot(aapl[,0], aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue")
plot(aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue")

# open value
lines(aapl[,2], type = "l", col="red")

# barplot
#emf('1.dest.emf')

#png("../log/apachebench/postcopy/1.dest.emf")
#postscript("plot.eps")
#emf("plot.emf")

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
#benchmark <- read.table("../log/apachebench/postcopy/1.dest.dstat", header = TRUE, row.names = "time", check.names = FALSE)
#cpus <- read.table(pipe("awk '{print $3}' ../log/apachebench/postcopy/1.dest.dstat | sed '1,2d'"))
##cpus <- read.table(pipe("awk '{print $3}' ../log/apachebench/postcopy/1.dest.dstat"), skip=3, nrows=27)
#cpus <- scan("../log/apachebench/postcopy/1.dest.dstat", skip=1)
#cpus <- read.csv("../log/apachebench/postcopy/1.dest.dstat", sep=",", head=TRUE)
#print(cpus)
#names(cpus)

#stripchart(cpus)
#plot(cpus)
#hist(cpus)
#boxplot(cpus)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
#barplot((as.matrix(cpus)), beside = TRUE, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
##barplot(t(as.matrix(metrics)), cex.axis = 1.5, cex.lab = 1.5, cex.names = 1.5, xlab = "TIME (SEC)", ylab = "BANDWIDTH UTILIZATION (MB/s)")
#barplot(t(100 - as.matrix(cpus)), ylim = c(0, 100), cex.axis = 1.5, cex.lab = 1.5, cex.names = 1.5, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
#barplot(cpus, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
