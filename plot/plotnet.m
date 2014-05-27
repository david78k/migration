#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
N = str2num(args{2})
postfix = ".net"

%prefix = "rand-6-r2"
data = strcat(prefix, postfix);
%data = strcat(prefix, ".dstat");

%A = dlmread(data, ' ', 2, 0);
% prefix.net
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
output = strcat(data, ".recv");
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
output = strcat(data, ".send");
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
