#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
N = str2num(args{2})
postfix = ".net"

startrow = 7;

% receive and send column starting 0
recvcol = 8;
sendcol = 9;

fontsize = 18;
%fontsize = 20; % too close distance between axis and axis labels

%prefix = "rand-6-r2"
data = strcat(prefix, postfix)
%data = strcat(prefix, ".dstat");

%A = dlmread(data, ' ', 2, 0);
% prefix.net
%A = load (data);
% load .csv file
A = csvread(prefix, startrow, recvcol);

% both receive and send
figure;
output = data
x = 1:1:length(A);
plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '--rs', 'LineWidth', 2);
%plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '--');
%plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('RECEIVE', 'SEND');

set(gca,'FontSize',fontsize)
set(findall(gcf,'type','text'),'FontSize',fontsize)

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% receive 
figure;
output = strcat(prefix, ".recv");
x = 1:1:length(A);
plot(x, A(:,1)/1000000, x, A(:,1)/(1000000*N), ':');
%plot(x, A(:,1)/1000000);
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

set(gca,'FontSize',fontsize)
set(findall(gcf,'type','text'),'FontSize',fontsize)
%set(gca,'FontSize',fontsize,'fontWeight','bold')
%set(findall(gcf,'type','text'),'FontSize',fontsize,'fontWeight','bold')

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% send
figure;
output = strcat(prefix, ".send");
x = 1:1:length(A);
plot(x, A(:,2)/1000000, x, A(:,2)/(1000000*N), '--', 'LineWidth', 3);
%plot(x, A(:,2)/1000000);
%plot(x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

set(gca,'FontSize',fontsize)
set(findall(gcf,'type','text'),'FontSize',fontsize)

ylabh = get(gca,'YLabel');
set(ylabh, 'Units', 'Normalized', 'Position', [-0.1, 0.5, 0]);

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));
