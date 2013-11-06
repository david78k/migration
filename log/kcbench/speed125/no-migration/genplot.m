#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
%N = str2num(args{2})

%prefix = "rand-6-r2"
data = prefix;
%data = strcat(prefix, ".bw");
%data = strcat(prefix, ".dstat");

%A = dlmread(data, ' ', 2, 0);
A = load (data);

% vcpu cpusage kcbench(%) elapsedTime(sec)
figure;
output = data
x = A(:,1);
%x = 1:1:length(A);
%ax = plotyy(x, A(:,1)/1000000, x, A(:,2)/1000000, '-.*');
ax = plotyy(x, A(:,2), x, A(:,4));
xlabel('VCPUS');
ylabel(ax(1), 'CPU USAGE (%)');
ylabel(ax(2), 'ELAPSED TIME (sec)');
legend('CPU USAGE(%)', 'ELAPSED TIME(sec)');
%legend('CPU(%)', 'KCBENCH CPU(%)');

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

%{
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
%}

