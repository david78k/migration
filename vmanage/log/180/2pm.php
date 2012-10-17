<html>
<head>

</head>
<title>2pm</title>
<body>

<h2>WAN simulation 2pm (<a href=../>../UP</a>)</h2>

<a href=2pm.png><img src=2pm.png></a>
<a href=2pm-detail.png><img src=2pm-detail.png></a>
<a href=2pm-before.png><img src=2pm-before.png></a>
<a href=2pm-net.png><img src=2pm-net.png></a>
<br />

<a href=2pm.eps>download 2pm.eps</a>, 
<a href=2pm-detail.eps>download 2pm-detail.eps</a>
<a href=2pm-before.eps>download 2pm-before.eps</a>
<a href=2pm-net.eps>download 2pm-net.eps</a>
<br />
<a href=2pm.tar>download all (2pm.png, 2pm.dat, 2pm.p)</a>
<br />

<a href=2pm.dat>2pm.dat (data file)</a>
<?php
$str = file_get_contents("2pm.dat");
echo "<pre>$str</pre>";
?>

<a href=2pm.dstat>2pm.dstat (network raw data file)</a>, 
<a href=2pm-net.dat>2pm-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("2pm.dstat");
echo "<pre>$str</pre>";
?>

<a href=2pm.log>2pm-r*.log (log files)</a>

<a href=2pm.net>2pm.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("2pm.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

