% Memory change PDF

% VM memory size (Gb = GB*8)
r = 8*8
% bandwidth (Gb/sec)
b = 1
% network(?) error rate (x100%)
err = 0.001
% delay (sec)
d = 0.5

% memory trasfer time
td = r*(1 + err)/b + d
