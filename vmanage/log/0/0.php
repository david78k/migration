<html>
<head>

</head>
<title>0</title>
<body>

<h2>WAN simulation 0 (<a href=../>../UP</a>)</h2>

<a href=0.png><img src=0.png></a>
<a href=0-detail.png><img src=0-detail.png></a>
<a href=0-before.png><img src=0-before.png></a>
<a href=0-net.png><img src=0-net.png></a>
<br />

<a href=0.eps>download 0.eps</a>, 
<a href=0-detail.eps>download 0-detail.eps</a>
<a href=0-before.eps>download 0-before.eps</a>
<a href=0-net.eps>download 0-net.eps</a>
<br />
<a href=0.tar>download all (0.png, 0.dat, 0.p)</a>
<br />

<a href=0.dat>0.dat (data file)</a>
<?php
$str = file_get_contents("0.dat");
echo "<pre>$str</pre>";
?>

<a href=0.dstat>0.dstat (network raw data file)</a>, 
<a href=0-net.dat>0-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("0.dstat");
echo "<pre>$str</pre>";
?>

<a href=0.log>0-r*.log (log files)</a>

<a href=0.net>0.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("0.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

