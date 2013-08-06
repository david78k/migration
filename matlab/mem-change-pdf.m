% Memory change PDF

% VM memory size (Gb = GB*8)
r = 8*8
% bandwidth (Gb/sec)
b = 1
% network(?) error rate (x100%)
err = 0.001
% processing delay (sec)
d = 0.5
% average compression rate (%)
c = 0.5

% downtime: memory transfer time
td = r*c*(1 + err)/b + d

% transferred part of memory to destination
rctmp = b*(td - d)/(c*(1 + err))
rc = min (max (rctmp, 0), r)

% remaining parts of memory 
rr = r - rc

% amount of memory to be recopied
d(rrc)/d(t) = w*rc

% memory changing rate
w = 
