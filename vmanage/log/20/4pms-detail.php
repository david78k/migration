<html>
<head>

</head>
<title>4pms-detail</title>
<body>

<h2>WAN simulation 4pms-detail (<a href=../>../UP</a>)</h2>

<a href=4pms-detail.png><img src=4pms-detail.png></a>
<a href=4pms-detail-detail.png><img src=4pms-detail-detail.png></a>
<a href=4pms-detail-before.png><img src=4pms-detail-before.png></a>
<a href=4pms-detail-net.png><img src=4pms-detail-net.png></a>
<br />

<a href=4pms-detail.eps>download 4pms-detail.eps</a>, 
<a href=4pms-detail-detail.eps>download 4pms-detail-detail.eps</a>
<a href=4pms-detail-before.eps>download 4pms-detail-before.eps</a>
<a href=4pms-detail-net.eps>download 4pms-detail-net.eps</a>
<br />
<a href=4pms-detail.tar>download all (4pms-detail.png, 4pms-detail.dat, 4pms-detail.p)</a>
<br />

<a href=4pms-detail.dat>4pms-detail.dat (data file)</a>
<?php
$str = file_get_contents("4pms-detail.dat");
echo "<pre>$str</pre>";
?>

<a href=4pms-detail.dstat>4pms-detail.dstat (network raw data file)</a>, 
<a href=4pms-detail-net.dat>4pms-detail-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("4pms-detail.dstat");
echo "<pre>$str</pre>";
?>

<a href=4pms-detail.log>4pms-detail-r*.log (log files)</a>

<a href=4pms-detail.net>4pms-detail.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("4pms-detail.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

