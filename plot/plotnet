#!/bin/bash

if [ $# -lt 1 ]; then
        #echo "usage: $0 script-name [eps]"
        echo "usage: plotnet script-name [eps]"
        exit 1
fi

data=$1
prefix=${data%\.*}
name=$prefix.p
#data=$prefix.dat
figure=${prefix}.net.png
terminal="png size 640,355"
ratio=0.5

if [ $# -eq 2 ]; then
        ratio=1
        figure=$prefix.eps
        terminal="postscript eps enhanced color"
        #terminal="postscript eps enhanced color size 320,175"
        #terminal="epslatex size 3in, 2in"
fi

function gnuplot_net() {
# script file to generate gnuplot script "script.p"
######################## data preprocessing ######################

tmp=$(mktemp)
#echo $tmp
# starting at 8 sample times
#more +8 $data | awk -F '|' '{print $4}' | sed 's/- /0/g' | sed 's/M/000000/g' | sed 's/k/000/g' | sed 's/0 |/0|/g' > $tmp
more $data | awk -F '|' '{print $4}' | sed 's/- /0/g' | sed 's/M/000000/g' | sed 's/k/000/g' | sed 's/0 |/0|/g' > $tmp
#awk -F '|' '{print $4}' $data > $tmp
#cat $tmp
data=$tmp

############################ create script #######################
cat >$name << GNUPLOT_EOF
data = "$data"
figure = "$figure"

set terminal $terminal
#set terminal $terminal size 640,355
#set terminal png
#set terminal postscript eps enhanced solid color
#set terminal hp500c 300 tiff
set output figure
set   autoscale                        # scale axes automatically

unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically

set tmargin 1;
#set bmargin at screen 0.15
#set object rectangle from screen 0,0 to screen 1,0.5 \
#    lw 0 fillstyle noborder behind
#set multiplot;
#set size 1,0.7;
#set size ratio 0.5;
#set size ratio $ratio;
#set origin 0.0,0.5;

# first plot
#set title "bandwidth limit 50 MB/s"
#set title "PI controller with bandwidth limit change from unlimited to 50 MB/s"
set xlabel "TIME (sec)"
set ylabel "THROUGHPUT (MB/s)"
#set y2label "cpu usage (%)"
#set y2tic auto
set ytics nomirror
#set y2tics
set tics out
set autoscale y
set autoscale y2;
#set key title "migration speed 40MB/s"
#set key left
set key horiz
#set key 0.01,100
#set label "Yield Point" at 0.003,260
#set arrow from 0.0028,250 to 0.003,280
#set xr [0.0:0.022]
set yr [0:]
#set yr [0:140]
#set format y "%gkm"

# Input file contains tab-separated fields
#set datafile separator "\t"

#set style line 1 lt 2 lw 3
#set style line 1 linetype 2 linecolor rgb "orange" linewidth 1.000 pointtype 8 pointsize default

#plot data using (\$2/1000000) title 'eth1' smooth freq with linespoints

plot data using (\$14/1000000) notitle smooth freq with lines
#plot data using (\$2/1000000) notitle smooth freq with linespoints

#plot data every ::3 using (\$14!=0 ? \$14 : \$13) notitle smooth freq with linespoints
#plot data every ::3 using (\$14!=0 ? \$13 : 1/0) notitle smooth freq with linespoints

#plot "<awk -F '|' '{print \$4}' data | awk '{print \$2}'" every ::3 using 1:2 notitle smooth freq with linespoints

#plot data every ::3 using (\$14) notitle smooth freq with linespoints

#plot data every ::3 using (\$14) title 'eth1' smooth freq with linespoints
#data using (100 - \$5) axis x1y2 title 'cpu usage' with lines lc rgb "black"

#data using (\$5*5.6) axis x1y2 title 'VM window' with linespoints, \\

#data using 11 title 'free memory' with linespoints, \\
#plot data using 1:4 title 'user' with linespoints, \\
#data using 1:5 title 'system' with linespoints, \\
#data using 1:6 title 'idle' with linespoints, \\
#data using 1:(\$2/1000000) axis x2y2 title 'receive' with lines linetype 11
# second plot
#unset multiplot;

GNUPLOT_EOF

#################### generate/upload images ######################
gnuplot $name
#gnuplot emf $name

rm $tmp

#git add .
#git commit -a -m $name
#git push
}

function R_net() {
#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
N = str2num(args{2})

%prefix = "rand-6-r2"
data = strcat(prefix, ".bw");
%data = strcat(prefix, ".dstat");

%A = dlmread(data, ' ', 2, 0);
A = load (data);

% both receive and send
figure;
output = data
x = 1:1:length(A);
plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('RECEIVE', 'SEND');

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% receive 
figure;
output = strcat(prefix, ".bw.recv");
x = 1:1:length(A);
%plot(x, A(:,1)/1000000, x, A(:,1)/(1000000*N), '-.*');
plot(x, A(:,1)/1000000);
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% send
figure;
output = strcat(prefix, ".bw.send");
x = 1:1:length(A);
%plot(x, A(:,2)/1000000, x, A(:,2)/(N*1000000), '-.*');
plot(x, A(:,2)/1000000);
%plot(x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));
}

function matlab_net() {

}


