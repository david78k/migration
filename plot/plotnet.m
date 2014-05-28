#!/usr/bin/octave -qf

args = argv();
prefix = args{1}
N = str2num(args{2})
postfix = ".net"

startrow = 7;

% receive and send column starting 0
recvcol = 8;
sendcol = 9;

%fontsize = 16;
%fontsize = 18;
fontsize = 20; % too close distance between axis and axis labels

linewidth = 3;
markersize = 5;

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
pl = plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '-*', 'LineWidth', linewidth, 'MarkerSize', markersize);
%pl = plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '-*-', 'LineWidth', linewidth);
%plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '--rs');
%plot(x, A(:,1)/1000000, x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/S)');
legend('RECEIVE', 'SEND');

set(pl(1), 'LineWidth', linewidth);
set(pl(2), 'LineWidth', linewidth);

set(gca,'FontSize',fontsize)
set(findall(gcf,'type','text'),'FontSize',fontsize)

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));

% receive 
figure;
output = strcat(prefix, ".recv");
x = 1:1:length(A);
pl = plot(x, A(:,1)/1000000, x, A(:,1)/(1000000*N), '-*', 'LineWidth', linewidth, 'MarkerSize', markersize);
%plot(x, A(:,1)/1000000, x, A(:,1)/(1000000*N), ':');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/s)');
legend('AGGREGATE', 'PER VM');

set(pl(1), 'LineWidth', linewidth);
set(pl(2), 'LineWidth', linewidth);

set(get(gca, 'YLabel'), 'Position', [-1, 5, 0]);
%set(get(gca, 'YLabel'), 'Units', 'Normalized', 'Position', [-0.1, 0.5, 0]);

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
pl = plot(x, A(:,2)/1000000, x, 'LineWidth', linewidth, A(:,2)/(1000000*N), '-.*', 'MarkerSize', markersize);
%pl = plot(x, A(:,2)/1000000, x, 'LineWidth', linewidth, A(:,2)/(1000000*N), '---.', 'LineWidth', linewidth);
%pl = plot(x, A(:,2)/1000000, x, 'LineWidth', linewidth, A(:,2)/(1000000*N), '--..', 'LineWidth', linewidth);
%plot(x, A(:,2)/1000000);
%plot(x, A(:,2)/1000000, '-.*');
xlabel('TIME (SEC)');
ylabel('THROUGHPUT (MB/S)');
legend('AGGREGATE', 'PER VM');

yh = get(gca, 'YLabel');
p=get(yh,'position');
set(yh,'position',[p(1)+5 p(2)])

set(gca,'FontSize',fontsize)
set(findall(gcf,'type','text'),'FontSize',fontsize)

%set(pl(1), 'LineWidth', linewidth);
%set(pl(2), 'LineWidth', linewidth);
 
%ylabh = get(gca,'YLabel');
%set(ylabh, 'Units', 'Normalized', 'Position', [-0.1, 0.5, 0]);
%%set(get(gca, 'YLabel'), 'Position', [-2, 5, 0]);
%set(get(gca, 'YLabel'), 'Units', 'Normalized', 'Position', [-0.2, 0.5, 0]);
%set(get(gca, 'YLabel'), 'Units', 'Normalized', 'Position', [-1, 1, 0]);

%xlabh = get(gca,'XLabel');
%set(xlabh,'Position',get(xlabh,'Position') - [0 .2 0])
%ylabh = get(gca,'YLabel');
%set(ylabh,'Position',get(ylabh,'Position') - [0.5 0.5 0])

saveas (1, strcat(output, ".png"));
saveas (1, strcat(output, ".eps"));
saveas (1, strcat(output, ".emf"));
