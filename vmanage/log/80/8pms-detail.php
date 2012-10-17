<html>
<head>

</head>
<title>8pms-detail</title>
<body>

<h2>WAN simulation 8pms-detail (<a href=../>../UP</a>)</h2>

<a href=8pms-detail.png><img src=8pms-detail.png></a>
<a href=8pms-detail-detail.png><img src=8pms-detail-detail.png></a>
<a href=8pms-detail-before.png><img src=8pms-detail-before.png></a>
<a href=8pms-detail-net.png><img src=8pms-detail-net.png></a>
<br />

<a href=8pms-detail.eps>download 8pms-detail.eps</a>, 
<a href=8pms-detail-detail.eps>download 8pms-detail-detail.eps</a>
<a href=8pms-detail-before.eps>download 8pms-detail-before.eps</a>
<a href=8pms-detail-net.eps>download 8pms-detail-net.eps</a>
<br />
<a href=8pms-detail.tar>download all (8pms-detail.png, 8pms-detail.dat, 8pms-detail.p)</a>
<br />

<a href=8pms-detail.dat>8pms-detail.dat (data file)</a>
<?php
$str = file_get_contents("8pms-detail.dat");
echo "<pre>$str</pre>";
?>

<a href=8pms-detail.dstat>8pms-detail.dstat (network raw data file)</a>, 
<a href=8pms-detail-net.dat>8pms-detail-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("8pms-detail.dstat");
echo "<pre>$str</pre>";
?>

<a href=8pms-detail.log>8pms-detail-r*.log (log files)</a>

<a href=8pms-detail.net>8pms-detail.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("8pms-detail.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

