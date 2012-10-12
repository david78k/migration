<html>
<head>

</head>
<title>1pm</title>
<body>

<h2>WAN simulation 1pm (<a href=../>../UP</a>)</h2>

<a href=1pm.png><img src=1pm.png></a>
<a href=1pm-detail.png><img src=1pm-detail.png></a>
<a href=1pm-before.png><img src=1pm-before.png></a>
<a href=1pm-net.png><img src=1pm-net.png></a>
<br />

<a href=1pm.eps>download 1pm.eps</a>, 
<a href=1pm-detail.eps>download 1pm-detail.eps</a>
<a href=1pm-before.eps>download 1pm-before.eps</a>
<a href=1pm-net.eps>download 1pm-net.eps</a>
<br />
<a href=1pm.tar>download all (1pm.png, 1pm.dat, 1pm.p)</a>
<br />

<a href=1pm.dat>1pm.dat (data file)</a>
<?php
$str = file_get_contents("1pm.dat");
echo "<pre>$str</pre>";
?>

<a href=1pm.dstat>1pm.dstat (network raw data file)</a>, 
<a href=1pm-net.dat>1pm-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("1pm.dstat");
echo "<pre>$str</pre>";
?>

<a href=1pm.log>1pm-r*.log (log files)</a>

<a href=1pm.net>1pm.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("1pm.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

