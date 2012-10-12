<html>
<head>

</head>
<title>2pms-detail</title>
<body>

<h2>WAN simulation 2pms-detail (<a href=../>../UP</a>)</h2>

<a href=2pms-detail.png><img src=2pms-detail.png></a>
<a href=2pms-detail-detail.png><img src=2pms-detail-detail.png></a>
<a href=2pms-detail-before.png><img src=2pms-detail-before.png></a>
<a href=2pms-detail-net.png><img src=2pms-detail-net.png></a>
<br />

<a href=2pms-detail.eps>download 2pms-detail.eps</a>, 
<a href=2pms-detail-detail.eps>download 2pms-detail-detail.eps</a>
<a href=2pms-detail-before.eps>download 2pms-detail-before.eps</a>
<a href=2pms-detail-net.eps>download 2pms-detail-net.eps</a>
<br />
<a href=2pms-detail.tar>download all (2pms-detail.png, 2pms-detail.dat, 2pms-detail.p)</a>
<br />

<a href=2pms-detail.dat>2pms-detail.dat (data file)</a>
<?php
$str = file_get_contents("2pms-detail.dat");
echo "<pre>$str</pre>";
?>

<a href=2pms-detail.dstat>2pms-detail.dstat (network raw data file)</a>, 
<a href=2pms-detail-net.dat>2pms-detail-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("2pms-detail.dstat");
echo "<pre>$str</pre>";
?>

<a href=2pms-detail.log>2pms-detail-r*.log (log files)</a>

<a href=2pms-detail.net>2pms-detail.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("2pms-detail.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

