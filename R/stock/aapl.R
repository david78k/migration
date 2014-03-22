library(ggplot2)

require(devEMF)
emf('aapl.emf')

aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)

#print(aapl)
#print(aapl.google)

#write.csv(aapl, file = "appl.csv")
#write.table(aapl, file = "appl.tab")

axis = (2, aapl[2])
plot(aapl[3,6], header = TRUE)
#plot(aapl[2], aapl[3,6], header = TRUE)
#plot(aapl[2], aapl[3,6])

# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
#benchmark <- read.table("", header = TRUE, row.names = "vwnd", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
#barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6))
#barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(6), xlab = "TIME (DAY)", ylab = "STOCK PRICE")

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
#legend("topright", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(6))

