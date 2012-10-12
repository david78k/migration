<html>
<head>

</head>
<title>8pms</title>
<body>

<h2>WAN simulation 8pms (<a href=../>../UP</a>)</h2>

<a href=8pms.png><img src=8pms.png></a>
<a href=8pms-detail.png><img src=8pms-detail.png></a>
<a href=8pms-before.png><img src=8pms-before.png></a>
<a href=8pms-net.png><img src=8pms-net.png></a>
<br />

<a href=8pms.eps>download 8pms.eps</a>, 
<a href=8pms-detail.eps>download 8pms-detail.eps</a>
<a href=8pms-before.eps>download 8pms-before.eps</a>
<a href=8pms-net.eps>download 8pms-net.eps</a>
<br />
<a href=8pms.tar>download all (8pms.png, 8pms.dat, 8pms.p)</a>
<br />

<a href=8pms.dat>8pms.dat (data file)</a>
<?php
$str = file_get_contents("8pms.dat");
echo "<pre>$str</pre>";
?>

<a href=8pms.dstat>8pms.dstat (network raw data file)</a>, 
<a href=8pms-net.dat>8pms-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("8pms.dstat");
echo "<pre>$str</pre>";
?>

<a href=8pms.log>8pms-r*.log (log files)</a>

<a href=8pms.net>8pms.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("8pms.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

