library(ggplot2)

#emf(180ms.emf)

require(devEMF)
png("180ms.emf")
#postscript("plot.eps")
#emf("plot.emf")

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
benchmark <- read.table("180ms.dat", header = TRUE, row.names = "vwnd", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6))

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
legend("topright", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(6))

