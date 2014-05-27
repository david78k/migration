src = ""

library(ggplot2)

require(devEMF)
emf('aapl2.emf')

aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
aapl = aapl[nrow(aapl):1, ]

#print(aapl)
#print(aapl.google)
print(aapl[, 1])

#write.csv(aapl, file = "appl.csv")
#write.table(aapl, file = "appl.tab")

#axis = (1, lab = aapl[2])
#axis = (2, aapl[2])
#box()

#matplot(aapl[,1], aapl[,5], type = "l", col="red")
#plot(aapl[,5], type = "l", col="blue")
#plot(aapl[,1], aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue")
#plot(aapl[,0], aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue")
plot(aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue")

# barplot
library(ggplot2)

require(devEMF)
emf('../log/apachebench/postcopy/1.dest.emf')

#png("../log/apachebench/postcopy/1.dest.emf")
#postscript("plot.eps")
#emf("plot.emf")

#cpus <- scan (pipe("awk '{print }' ../log/apachebench/postcopy/1.dest.dstat"), skip=2)
#cpus <- read.table("../log/apachebench/postcopy/1.dest.dstat", colClasses=3)

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
#benchmark <- read.table("../log/apachebench/postcopy/1.dest.dstat", header = TRUE, row.names = "time", check.names = FALSE)
#benchmark <- read.table("../log/apachebench/postcopy/1.dest.dstat", check.names = FALSE, comment.char = "#")
#benchmark <- read.table("../log/apachebench/postcopy/1.dest.dstat", header = TRUE, check.names = FALSE, comment.char = "#")
#benchmark <- read.table("../log/apachebench/postcopy/1.dest.dstat", check.names = FALSE)

#cpus <- read.table("../log/apachebench/postcopy/1.dest.dstat", header = TRUE, row.name = "time")
#cpus <- read.table(pipe("awk '{print $3}' ../log/apachebench/postcopy/1.dest.dstat | sed '1,2d'"))
cpus <- read.table(pipe("awk '{print $3}' ../log/apachebench/postcopy/1.dest.dstat"), skip=3, nrows=27)
#cpus <- read.table("../log/apachebench/postcopy/1.dest.dstat", skip=1)
#cpus <- scan("../log/apachebench/postcopy/1.dest.dstat", skip=1)
#cpus <- read.csv("../log/apachebench/postcopy/1.dest.dstat", sep=",", head=TRUE)
#print(cpus)
#names(cpus)

#stripchart(cpus)
#plot(cpus)
#hist(cpus)
#boxplot(cpus)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
#barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6))
#barplot((as.matrix(benchmark)), beside = TRUE, col = heat.colors(6), xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
#barplot(benchmark, beside = TRUE, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")

#barplot((as.matrix(cpus)), beside = TRUE, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
barplot(t(as.matrix(metrics)), cex.axis = 1.5, cex.lab = 1.5, cex.names = 1.5, xlab = "TIME (SEC)", ylab = "BANDWIDTH UTILIZATION (MB/s)")
#barplot(t(100 - as.matrix(cpus)), ylim = c(0, 100), cex.axis = 1.5, cex.lab = 1.5, cex.names = 1.5, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
#barplot(cpus, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
