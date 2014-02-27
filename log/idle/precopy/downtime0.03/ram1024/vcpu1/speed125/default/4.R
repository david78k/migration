library(ggplot2)

require(devEMF)
emf('../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.emf')

#png("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.emf")
#postscript("plot.eps")
#emf("plot.emf")

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
benchmark <- read.table("../log/idle/precopy/downtime0.03/ram1024/vcpu1/speed125/default/4.cpu", header = TRUE, row.names = "vwnd", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
#barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6))
barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6), xlab = "TIME (SEC)", ylab = "CPU USAGE (%)")

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
legend("topright", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(6))

