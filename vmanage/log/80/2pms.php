<html>
<head>

</head>
<title>2pms</title>
<body>

<h2>WAN simulation 2pms (<a href=../>../UP</a>)</h2>

<a href=2pms.png><img src=2pms.png></a>
<a href=2pms-detail.png><img src=2pms-detail.png></a>
<a href=2pms-before.png><img src=2pms-before.png></a>
<a href=2pms-net.png><img src=2pms-net.png></a>
<br />

<a href=2pms.eps>download 2pms.eps</a>, 
<a href=2pms-detail.eps>download 2pms-detail.eps</a>
<a href=2pms-before.eps>download 2pms-before.eps</a>
<a href=2pms-net.eps>download 2pms-net.eps</a>
<br />
<a href=2pms.tar>download all (2pms.png, 2pms.dat, 2pms.p)</a>
<br />

<a href=2pms.dat>2pms.dat (data file)</a>
<?php
$str = file_get_contents("2pms.dat");
echo "<pre>$str</pre>";
?>

<a href=2pms.dstat>2pms.dstat (network raw data file)</a>, 
<a href=2pms-net.dat>2pms-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("2pms.dstat");
echo "<pre>$str</pre>";
?>

<a href=2pms.log>2pms-r*.log (log files)</a>

<a href=2pms.net>2pms.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("2pms.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

