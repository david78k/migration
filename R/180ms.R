library(ggplot2)

#emf(180ms.emf)
png("180ms.png")
#postscript("plot.eps")
#require(devEMF)
#emf("plot.emf")

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
benchmark <- read.table("180ms.dat", header = TRUE, row.names = "vwnd", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(4))

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
legend("topleft", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(4))

