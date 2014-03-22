#read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)

#aapl.google <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
#aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep="\t", header=1)

print(aapl)
#print(aapl.google)

write.csv(aapl, file = "appl.csv")
write.table(aapl, file = "appl.tab")
#write.csv(aapl.google, file = "aapl.csv")
