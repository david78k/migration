#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
N = str2num(args{2})

%A = load (data) 

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
plot(x, A(:,1)/1000000, x, A(:,1)/(1000000*N), '-.*');
%plot(x, A(:,1)/1000000, x, A(:,1)/1000000/N, '-.*');
%plot(x, A(:,1)/1000000);
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
plot(x, A(:,2)/1000000, x, A(:,2)/(N*1000000), '-.*');
%plot(x, A(:,2)/1000000, x, A(:,2)/1000000/N, '-.*');
%plot(x, A(:,2)/1000000);
%plot(x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% for controller
%data = strcat(prefix, ".controller");
%output = strcat(prefix, ".vwnd");
%A = load ('lf-0-r1.vwnd', 'ascii')

%vwnds = A(:,1)
%figure;
%gplot rand (100,1) with linespoints
%x = -10:0.1:10;
%plot (x, sin (x));
%plot(x, A(:,2)/1000000, x, A(:,3)/1000000, '-.*');
%plot(A(:,2:3)/1000000);
%plot(A(:,:))
%plot(A(:,[1]));
%plot(A(:,[1, 5]));
%plot(A(:,1:5))
%plot(RTTs, Ns)
%xlabel('ITERATION');
%ylabel('VM WINDOW');
%legend('VM WINDOW', 'THRESHOLD');

%image = "lf-0-r1";
%print -deps $image.eps
%saveas (1, strcat(output, ".png"));
%saveas (1, strcat(output, ".eps"));
%saveas (1, strcat(output, ".emf"));
