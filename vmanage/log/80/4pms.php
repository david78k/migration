<html>
<head>

</head>
<title>4pms</title>
<body>

<h2>WAN simulation 4pms (<a href=../>../UP</a>)</h2>

<a href=4pms.png><img src=4pms.png></a>
<a href=4pms-detail.png><img src=4pms-detail.png></a>
<a href=4pms-before.png><img src=4pms-before.png></a>
<a href=4pms-net.png><img src=4pms-net.png></a>
<br />

<a href=4pms.eps>download 4pms.eps</a>, 
<a href=4pms-detail.eps>download 4pms-detail.eps</a>
<a href=4pms-before.eps>download 4pms-before.eps</a>
<a href=4pms-net.eps>download 4pms-net.eps</a>
<br />
<a href=4pms.tar>download all (4pms.png, 4pms.dat, 4pms.p)</a>
<br />

<a href=4pms.dat>4pms.dat (data file)</a>
<?php
$str = file_get_contents("4pms.dat");
echo "<pre>$str</pre>";
?>

<a href=4pms.dstat>4pms.dstat (network raw data file)</a>, 
<a href=4pms-net.dat>4pms-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("4pms.dstat");
echo "<pre>$str</pre>";
?>

<a href=4pms.log>4pms-r*.log (log files)</a>

<a href=4pms.net>4pms.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("4pms.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

