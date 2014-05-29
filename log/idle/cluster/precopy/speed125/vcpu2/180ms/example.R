#!/usr/bin/Rscript

# EXAMPLE CODE FOR DRAWING A LINE PLOT IN R
# 2 February 2008
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rm(list = ls())      # Clear all variables
graphics.off()    # Close graphics windows

prefix = "example"
#png("example.png")
#postscript("example.eps")

# cex
fontsize = 1.5

# Generate sample time series data
ti = 1:50                                   # Generate 50 sample time steps
y1 = 8 + rnorm(50)                          # Generate 50 stochastic data points for time series y1
y2 = seq(10,15,length.out=50) + rnorm(50)   # Generate 50 stochastic data points for time series y2
y3 = seq(80,110,length.out=50) + rnorm(50)  # Generate 50 stochastic data points for time series y3

# Plot the y1 data
#par(oma=c(2,2,2,4))               # Set outer margin areas (only necessary in order to plot extra y-axis)
par(oma=c(0,0,0,0))
# c(bottom,left,top,right)
#par(mar=c(5,7,0,0))
par(mar=c(5,4,0,0)) 
#par(mar=c(5,5,1,1)) # good fit

genplot <- function (type) {
        if(type == "png") {
                #type(paste0(prefix, sep = ".", type))
                png(paste0(prefix, ".png"))
        } else if (type == "pdf") {
                pdf(paste0(prefix, ".pdf"))
        } else if (type == "eps") {
                #png("aapl.png")
                #postscript(paste0(prefix, ".eps"), res = resolution)
                postscript(paste0(prefix, ".eps"))
        } else if (type == "emf") {
		require(devEMF)
                #postscript("aapl.eps")
                emf(paste0(prefix, ".emf"))
                #emf('aapl.emf')
        }

plot(ti, y1,                      # Data to plot - x, y
     type="b",                    # Plot lines and points. Use "p" for points only, "l" for lines only
#     main="Time series plot",     # Main title for the plot
     xlab="TIME (SEC)",                 # Label for the x-axis
     ylab="THROUGHPUT (MB/S)",   # Label for the y-axis
     font.lab=2,                  # Font to use for the axis labels: 1=plain text, 2=bold, 3=italic, 4=bold italic
#     cex = 2,
     cex.axis = fontsize,
     cex.lab = fontsize,
     ylim=c(0,20),                # Range for the y-axis; "xlim" does same for x-axis
     xaxp=c(0,50,5),              # X-axis min, max and number of intervals; "yaxp" does same for y-axis
     bty="l",                     # Box around plot to contain only left and lower lines
     las = 1			  # labels are parallel (=0) or perpendicular(=2) to axis, 1 for x-axis = 0 and y-axis = 1
)

# Add y2 data to the same plot
points(ti, y2,
       type="b",                  # Plot lines and points
       lty=1,                     # Line type: 0=blank, 1=solid, 2=dashed, 3=dotted, 4=dotdash, 5=longdash, 6=twodash
       lwd=1,                     # Line width
       cex = fontsize,
       pch=19,                    # Point type: pch=19 - solid circle, pch=20 - bullet (smaller circle), pch=21 - circle, pch=22 - square, pch=23 - diamond, pch=24 - triangle point-up, pch=25 - triangle point down.
       col="red")                 # Color of the plotted data

#axis(side = 2, las = 1)

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
legend("topleft",                       # x-y coordinates for location of the legend
       legend=c("y1", "y2"),      # Legend labels
       col=c("black", "red"),   # Color of points or lines
       pch=c(21,19),                 # Point type
       lty=c(1,1),                    # Line type
       lwd=c(1,1),                    # Line width
       cex = fontsize
      # title="Time series"             # Legend title
)

# For further information and options see help on:
# "plot" - plot function
# "par" - graphical parameters
# "axis" - adding axes to a plot
# "legend" - adding a legend to a graph

# Tufte tip:
# Minimize the non-data clutter in labels, axes etc.
}

genplot("png")
genplot("pdf")
genplot("emf")

