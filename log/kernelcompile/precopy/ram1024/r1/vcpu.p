data = "vcpu"
figure = "vcpu.png"

set terminal png enhanced size 640,355 font 16
#set terminal png enhanced size 640,355 font 16 size 640,355
#set terminal postscript eps enhanced solid color
set output figure 
set   autoscale                        # scale axes automatically

unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically

set tmargin 1;
#set bmargin at screen 0.15
#set object rectangle from screen 0,0 to screen 1,0.5 #    lw 0 fillstyle noborder behind
#set multiplot;
#set size 1,0.7;
#set size ratio 0.5;
#set size ratio 0.5;
#set origin 0.0,0.5;

# first plot
#set title "bandwidth limit 50 MB/s"
set xlabel "VCPU"
set ylabel ""
#set ylabel "downtime (millisec)"
#set ylabel "total migration time (millisec)"
#set ylabel "total transferred data (kbytes)"
#set ylabel "throughput (mbps)"
#set y2label "cpu usage (%)"
#set y2tic auto
set ytics nomirror
#set y2tics
set tics out
set autoscale y
set autoscale y2;
#set key title "migration speed 40MB/s"
#set key box 
#set key horiz 
set key out horiz
set key left top
#set key center top
#set key left
#set key right
#set key 0.01,100
#set label "Yield Point" at 0.003,260
#set arrow from 0.0028,250 to 0.003,280
#set xr [0.0:0.022]
set yr [0:]
#set yr [0:140]
#set y2r [0:100]
#set format y "%gkm"

set style histogram cluster gap 2
set style fill solid border -1
set boxwidth 0.2 absolute
#set boxwidth 0.3 absolute
#set xtic rotate by -45 scale 0

#set style line 1 lt 2 lw 3
#set style line 1 linetype 2 linecolor rgb "orange" linewidth 1.000 pointtype 8 pointsize default
#plot data using ($14/1000000) title 'send' smooth freq with linespoints, \

#plot data using 2:xtic(1) notitle smooth freq with boxes lc rgb "grey"
#data using ($0+0.3):17 title 'xbzrle+auto-converge' smooth freq with boxes lc rgb "red", 
plot data using ($0-0.3):7 title 'default' smooth freq with boxes lc rgb 'black', data using ($0-0.1):13 title 'xbzrle' smooth freq with boxes lc rgb 'grey', data using ($0+0.1):19 title 'auto-converge' smooth freq with boxes lc rgb 'white', data using ($0+0.3):25 title 'xbzrle+auto-converge' smooth freq with boxes fs pattern 1 lc rgb 'black', data using 0:(0):xticlabel(1) title '' w l


# total time
#plot data using ($0-0.3):2 title 'default' smooth freq with boxes lc rgb "black", #data using ($0-0.1):7 title 'xbzrle' smooth freq with boxes lc rgb "grey", #data using ($0+0.1):12 title 'auto-converge' smooth freq with boxes lc rgb "white", #data using ($0+0.3):17 title 'xbzrle+auto-converge' smooth freq with boxes fs pattern 1 lc rgb "black", #data using 0:(0):xticlabel(1) title '' w l

# downtime
#plot data using ($0-0.3):3 title 'default' smooth freq with boxes lc rgb "black", #data using ($0-0.1):8 title 'xbzrle' smooth freq with boxes lc rgb "grey", #data using ($0+0.1):13 title 'auto-converge' smooth freq with boxes lc rgb "white", #data using ($0+0.3):18 title 'xbzrle+auto-converge' smooth freq with boxes fs pattern 1 lc rgb "black", #data using 0:(0):xticlabel(1) title '' w l

# total transferred data in kbytes
#plot data using ($0-0.3):4 title 'default' smooth freq with boxes lc rgb "black", #data using ($0-0.1):9 title 'xbzrle' smooth freq with boxes lc rgb "grey", #data using ($0+0.1):14 title 'auto-converge' smooth freq with boxes lc rgb "white", #data using ($0+0.3):19 title 'xbzrle+auto-converge' smooth freq with boxes fs pattern 1 lc rgb "black", #data using 0:(0):xticlabel(1) title '' w l

# migration throughput in mbps
#plot data using ($0-0.3):5 title 'default' smooth freq with boxes lc rgb "black", #data using ($0-0.1):10 title 'xbzrle' smooth freq with boxes lc rgb "grey", #data using ($0+0.1):15 title 'auto-converge' smooth freq with boxes lc rgb "white", #data using ($0+0.3):20 title 'xbzrle+auto-converge' smooth freq with boxes fs pattern 1 lc rgb "black", #data using 0:(0):xticlabel(1) title '' w l

#plot data using 3:xtic(1) notitle smooth freq with boxes lc rgb "grey"

#plot data using 2:xtic(1) title 'time' smooth freq with boxes fs pattern 1

#plot data using 1:2 title 'time' smooth freq with linespoints

#data using (100 - $3) axis x1y2 title 'cpu usage' with lines lc rgb "black"

#data using ($5*5.6) axis x1y2 title 'VM window' with linespoints, \

#data using 11 title 'free memory' with linespoints, \
#data using 1:($2/1000000) axis x2y2 title 'receive' with lines linetype 11 
# second plot
#unset multiplot;

