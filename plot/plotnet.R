#!/usr/bin/Rscript

#options(echo=TRUE)
# trailingOnly=TRUE means that only your arguments are returned
args <- commandArgs(trailingOnly = TRUE)
print(args)
src <- args[1]
N <- as.numeric(args[2])

#prefix = "aapl"
#src = "4vms-r1.dest.dstat.csv"
#N = 4 # number of parallel migrations
#prefix = paste0(src, ".recv")
prefix = paste0(src, ".send")

# for receiver
#startcol = 9
# for sender
startcol = 10
#integer: the number of lines of the data file to skip before beginning to read data.
startrow = 6

# figure size in pixel
fheight = 200
fwidth = 300

linewidth = 2.5

# second line color
secondlc = "red"

# second line type: 2 for dashed, 3 for dotted, 4 for dotdash, 5 for longdash, 6 for twodash
#secondlty = 5 # best
secondlty = 2 # good 
#secondlty = 3 # too pale

#legendpos = "bottom"
legendpos = "center"
#legendpos = "topright"

# cex
fontsize = 1
#fontsize = 1.5 
#fontsize = 2 

#library(ggplot2)
require(devEMF)

#aapl <- read.csv("http://www.google.com/finance/historical?q=NASDAQ:AAPL&authuser=0&output=csv ", sep=",", header=1)
data <- read.csv(src, sep=",", skip = startrow, header=1)
#aapl = aapl[nrow(aapl):1, ]
#print(aapl)

genplot <- function (type) {
# EXAMPLE CODE FOR DRAWING A LINE PLOT IN R
# 2 February 2008
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#rm(list = ls())      # Clear all variables
#graphics.off()    # Close graphics windows

	if(type == "png") {
		#type(paste0(prefix, sep = ".", type))
		png(paste0(prefix, ".png"), height=fheight, width=fwidth)
		#png(paste0(prefix, ".png"), height=300, width=400)
	#	png(paste0(prefix, ".png"))
	} else if (type == "pdf") {
		pdf(paste0(prefix, ".pdf"), height=1.5*fheight/100.0, width=1.5*fwidth/100.0)
	} else if (type == "eps") {
		#png("aapl.png")
		#postscript(paste0(prefix, ".eps"), res = resolution)
		postscript(paste0(prefix, ".eps"))
	} else if (type == "emf") {
		#postscript("aapl.eps")
		emf(paste0(prefix, ".emf"), height=1.5*fheight/100.0, width=1.5*fwidth/100.0)
		#emf('aapl.emf')
	}

# Plot the y1 data
#par(oma=c(2,2,2,4))               # Set outer margin areas (only necessary in order to plot extra y-axis)

	# margins: oma for the number of lines in outer margin, mar for the number of lines in inside margin
	# c(bottom, left, top, right)
	#par(oma=c(0,0,0,0))               # Set outer margin areas (only necessary in order to plot extra y-axis)
	par(mar=c(5,5,1,1)) # good fit
	#par(mar=c(4,5,0,0))  # both too tight
	#par(mar=c(4,6,0,0)) # bottom good, left wide
	#par(mar=c(6,6,0,0)) # bit wide

#layout(rbind(1,2), heights=c(7,1))  # put legend on bottom 1/8th of the chart

# aggregate throughput
#plot(data[,startcol]/1000000.0,            # Data to plot - x, y
plot(data[,startcol]/1024.0/1024.0,            # Data to plot - x, y
#   type="b",                    # Plot lines and points. Use "p" for points only, "l" for lines only
     type="l",                    # Plot lines and points. Use "p" for points only, "l" for lines only
#     main="Time series plot",     # Main title for the plot
     xlab="TIME (SEC)",                 # Label for the x-axis
     ylab="THROUGHPUT (MB/S)",   # Label for the y-axis
     font.lab=2,                  # Font to use for the axis labels: 1=plain text, 2=bold, 3=italic, 4=bold italic
     cex.axis = fontsize,
     cex.lab = fontsize,
#     ylim=c(0,20),                # Range for the y-axis; "xlim" does same for x-axis
#     xaxp=c(0,50,5),              # X-axis min, max and number of intervals; "yaxp" does same for y-axis
#     bty="l",                     # Box around plot to contain only left and lower lines
     las = 1                      # labels are parallel (=0) or perpendicular(=2) to axis, 1 for x-axis = 0 and y-axis = 1
)

# Add y2 data to the same plot
#points(data[,startcol]/1000000.0/N,
points(data[,startcol]/1024.0/1024.0/N,
       type="l",                  # Plot lines and points
       lty=secondlty,                     # Line type: 0=blank, 1=solid, 2=dashed, 3=dotted, 4=dotdash, 5=longdash, 6=twodash
       lwd=2,                     # Line width
#       pch=20,                    # Point type: pch=19 - solid circle, pch=20 - bullet (smaller circle), pch=21 - circle, pch=22 - square, pch=23 - diamond, pch=24 - triangle point-up, pch=25 - triangle point down.
#       pch=19,                    # Point type: pch=19 - solid circle, pch=20 - bullet (smaller circle), pch=21 - circle, pch=22 - square, pch=23 - diamond, pch=24 - triangle point-up, pch=25 - triangle point down.
       col=secondlc)                 # Color of the plotted data

# Add y3 data to the same plot, but on a different axis
#par(new=T,                        # The next high-level plotting command (actually plot.new) should not clean the frame before drawing ìas if it was on a new deviceî.
#    oma=c(2,2,2,4))               # Increase the size of the outer margins to accomodate second y axis

#plot(ti, y3,
#       yaxt="n",                  # Do not plot the y-axis
#       ylab="",                   # Do not plot the y-axis label
#       xlab="",                   # Do not plot the x-axis label
#       type="b",                  # Plot lines and points
#       lty=1,                     # Line type: 0=blank, 1=solid, 2=dashed, 3=dotted, 4=dotdash, 5=longdash, 6=twodash
#       lwd=1,                     # Line width
#       pch=19,                    # Point type: pch=19 - solid circle, pch=20 - bullet (smaller circle), pch=21 - circle, pch=22 - square, pch=23 - diamond, pch=24 - triangle point-up, pch=25 - triangle point down.
#       col="blue")                # Color of the plotted data

#axis(4,                           # Add a second axis: 1=below, 2=left, 3=above and 4=right
#    pretty(range(y3),10))         # Intervals for the second y-axis

#mtext("Response (y3)",            # Add second y-axis label
#      side=4,                     # Add to right hand side of plot
#      line=3,                     # Add to line 3 from the margin
#      font=2)                     # Print label in bold

# Add a legend to the plot
#legend("topright",                       # x-y coordinates for location of the legend
#legend("bottom",                       # x-y coordinates for location of the legend
legend(legendpos,                       # x-y coordinates for location of the legend
       legend=c("AGGREGATE", "PER VM"),      # Legend labels
       col=c("black", secondlc),   # Color of points or lines
#       pch=c(NA,20),                 # Point type
       #pch=c(21,19),                 # Point type
       lty=c(1,secondlty),                    # Line type
       lwd=c(1,2),                    # Line width
       cex = fontsize,
	bty = 'n'
)
	#matplot(aapl[,1], aapl[,5], type = "l", col="red")
	#plot(data[,startcol]/1000000.0, xlab = "TIME (SEC)", ylab = "THROUGHPUT (MB/S)", type = "l", col="blue", cex.axis = fontsize, cex.lab = fontsize, lwd = linewidth)
	#plot(aapl[,5], xlab = "TIME", ylab = "PRICE ($)", type = "l", col="blue", cex.axis = fontsize, cex.lab = fontsize)

	# per VM. lty 5 for longdash, lty 2 for dashed
	#lines(data[,startcol]/1000000.0/N, type = "l", lty = secondlty, col=secondlc, lwd = linewidth)

	# open value
	#lines(aapl[,2], type = "l", col="red")
	
	#names <- c("AGGREGATE", "PER VM")
	# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
	# lty for line types, lwd for line width
	#legend("center", names, lty = c(1, secondlty), col=c("blue", secondlc), lwd = c(linewidth, linewidth), bty = 'n',  cex = fontsize)
	#legend("topright", names, lty = 1, bty = 'n',  cex = 1.5)
}

genplot("png")
genplot("pdf")
#genplot("eps")
genplot("emf")

