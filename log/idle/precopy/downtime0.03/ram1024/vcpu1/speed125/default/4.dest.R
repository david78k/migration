library(ggplot2)

require(devEMF)
emf('../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.emf')

#png("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.emf")
#postscript("plot.eps")
#emf("plot.emf")

#cpus <- scan (pipe("awk '{print }' ../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu"), skip=2)
#cpus <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", colClasses=3)

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
#benchmark <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", header = TRUE, row.names = "time", check.names = FALSE)
#benchmark <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", check.names = FALSE, comment.char = "#")
#benchmark <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", header = TRUE, check.names = FALSE, comment.char = "#")
#benchmark <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", check.names = FALSE)

#cpus <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", header = TRUE, row.name = "time")
cpus <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", skip=1)
#cpus <- scan("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", skip=1)
#cpus <- read.csv("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.dest.cpu", sep=",", head=TRUE)
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
#barplot((as.matrix(benchmark)), col = heat.colors(6), xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
#barplot((as.matrix(benchmark)), xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")

#barplot((as.matrix(cpus)), beside = TRUE, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
barplot(t(100 - as.matrix(cpus)), ylim = c(0, 100), cex.axis = 1.5, cex.lab = 1.5, cex.names = 1.5, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")
#barplot(cpus, xlab = "TIME (SEC)", ylab = "CPU UTILIZATION (%)")

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
#legend("topright", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(6))

