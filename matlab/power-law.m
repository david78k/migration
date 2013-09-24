% power-law approximation
RTT = 70;
c = 100;
k = 300;

N = c*(exp(k*log(0.8)/RTT))

RTTs = [1 70 180 300]
Ns = zeros(1, length(RTTs))

for i = 1:length(RTTs)
	RTT = RTTs(i)	
	Ns(i) = c*(exp(k*log(0.8)/RTT))
end

figure
plot(RTTs, Ns)
xlabel('RTT')
ylabel('N')

% print -deps plot.eps
saveas (1, "plot.png");
