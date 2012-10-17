<html>
<head>

</head>
<title>8pm</title>
<body>

<h2>WAN simulation 8pm (<a href=../>../UP</a>)</h2>

<a href=8pm.png><img src=8pm.png></a>
<a href=8pm-detail.png><img src=8pm-detail.png></a>
<a href=8pm-before.png><img src=8pm-before.png></a>
<a href=8pm-net.png><img src=8pm-net.png></a>
<br />

<a href=8pm.eps>download 8pm.eps</a>, 
<a href=8pm-detail.eps>download 8pm-detail.eps</a>
<a href=8pm-before.eps>download 8pm-before.eps</a>
<a href=8pm-net.eps>download 8pm-net.eps</a>
<br />
<a href=8pm.tar>download all (8pm.png, 8pm.dat, 8pm.p)</a>
<br />

<a href=8pm.dat>8pm.dat (data file)</a>
<?php
$str = file_get_contents("8pm.dat");
echo "<pre>$str</pre>";
?>

<a href=8pm.dstat>8pm.dstat (network raw data file)</a>, 
<a href=8pm-net.dat>8pm-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("8pm.dstat");
echo "<pre>$str</pre>";
?>

<a href=8pm.log>8pm-r*.log (log files)</a>

<a href=8pm.net>8pm.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("8pm.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

