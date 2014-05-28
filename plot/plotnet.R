#!/usr/bin/Rscript

#args <- commandArgs(trailingOnly = TRUE)
#rnorm(n=as.numeric(args[1]), mean=as.numeric(args[2]))

#prefix = "aapl"
src = "4vms-r1.dest.dstat.csv"
N = 4 # number of parallel migrations
prefix = paste0(src, ".recv")

startcol = 9
#integer: the number of lines of the data file to skip before beginning to read data.
startrow = 6

linewidth = 2.5

# second line type: 2 for dashed, 3 for dotted, 4 for dotdash, 5 for longdash, 6 for twodash
secondlty = 5 # best
#secondlty = 2 # good 
#secondlty = 3 # too pale

fontsize = 1.5 # works
#fontsize = 1.6 # a little bit big
#fontsize = 1.7 # big
#fontsize = 1.8 # too big
#fontsize = 2 # too big, outside the box

#function.names <- c("png", "eps", "emf")

library(ggplot2)

require(devEMF)

genplot <- function (type) {
	if(type == "png") {
		#type(paste0(prefix, sep = ".", type))
		png(paste0(prefix, ".png"))
	} else if (type == "eps") {
		#png("aapl.png")
		postscript(paste0(prefix, ".eps"))
	} else if (type == "emf") {
		#postscript("aapl.eps")
		emf(paste0(prefix, ".emf"))
		#emf('aapl.emf')
	}

	# aggregate throughput
	#matplot(aapl[,1], aapl[,5], type = "l", col="red")
	plot(data[,startcol]/1000000.0, xlab = "TIME", ylab = "THROUGHPUT (MB/S)", type = "l", col="blue", cex.axis = fontsize, cex.lab = fontsize, lwd = linewidth)
	#plot(aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue", cex.axis = fontsize, cex.lab = fontsize)

	# per VM. lty 5 for longdash, lty 2 for dashed
	lines(data[,startcol]/1000000/N, type = "l", lty = secondlty, col="red", lwd = linewidth)

	# open value
	#lines(aapl[,2], type = "l", col="red")
	
	names <- c("AGGREGATE", "PER VM")
	# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
	# lty for line types, lwd for line width
	#legend("center", names, cex = 1.5)
	legend("center", names, lty = c(1, secondlty), col=c("blue", "red"), lwd = c(linewidth, linewidth), bty = 'n',  cex = 1.5)
	#legend("topright", names, lty = 1, bty = 'n',  cex = 1.5)
}

#aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
data <- read.csv(src, sep=",", skip = startrow, header=1)
#aapl = aapl[, startcol]
#aapl = aapl[nrow(aapl):1, ]

#print(aapl)

genplot("png")
genplot("eps")
genplot("emf")

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
