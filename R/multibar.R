library(ggplot2)

#png("plot.png")

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
benchmark <- read.table("data.dat", header = TRUE, row.names = "Title", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(4))

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
legend("topleft", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(4))

#ggsave("plot.png",width=4,height=4,dpi=100)

png("plot.png")
#eps("plot.eps")
