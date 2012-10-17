<html>
<head>

</head>
<title>1pms</title>
<body>

<h2>WAN simulation 1pms (<a href=../>../UP</a>)</h2>

<a href=1pms.png><img src=1pms.png></a>
<a href=1pms-detail.png><img src=1pms-detail.png></a>
<a href=1pms-before.png><img src=1pms-before.png></a>
<a href=1pms-net.png><img src=1pms-net.png></a>
<br />

<a href=1pms.eps>download 1pms.eps</a>, 
<a href=1pms-detail.eps>download 1pms-detail.eps</a>
<a href=1pms-before.eps>download 1pms-before.eps</a>
<a href=1pms-net.eps>download 1pms-net.eps</a>
<br />
<a href=1pms.tar>download all (1pms.png, 1pms.dat, 1pms.p)</a>
<br />

<a href=1pms.dat>1pms.dat (data file)</a>
<?php
$str = file_get_contents("1pms.dat");
echo "<pre>$str</pre>";
?>

<a href=1pms.dstat>1pms.dstat (network raw data file)</a>, 
<a href=1pms-net.dat>1pms-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("1pms.dstat");
echo "<pre>$str</pre>";
?>

<a href=1pms.log>1pms-r*.log (log files)</a>

<a href=1pms.net>1pms.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("1pms.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

