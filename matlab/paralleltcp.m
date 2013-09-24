%N = (3BR - 3W - sqrt(3)sqrt(9B^R^-16BRW + 7W^))*BR/(9BR-6W)
% bandwidth in Mbps (to kbps)
%B = 1000*1024*1024;
B = 1000;
%B = 8.3
% RTT in ms (to second)
R = 200*10.^(-3)
%R = 20
% socket buffer size in kbytes (to kbits)
%W = 64*8*1024
W = 64*8

% APT: optimal number of parallel streams
N = (3*B*R-3*W-sqrt(3)*sqrt(9*B.^2*R.^2-16*B*R*W + 7*W.^2))*B*R/(9*B*R-6*W)

% power-law approximation
RTT = R
N = c*(exp(k*ln(0.8/RTT))

for i = 1:1
    
end
