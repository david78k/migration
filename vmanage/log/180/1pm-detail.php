<html>
<head>

</head>
<title>1pm-detail</title>
<body>

<h2>WAN simulation 1pm-detail (<a href=../>../UP</a>)</h2>

<a href=1pm-detail.png><img src=1pm-detail.png></a>
<a href=1pm-detail-detail.png><img src=1pm-detail-detail.png></a>
<a href=1pm-detail-before.png><img src=1pm-detail-before.png></a>
<a href=1pm-detail-net.png><img src=1pm-detail-net.png></a>
<br />

<a href=1pm-detail.eps>download 1pm-detail.eps</a>, 
<a href=1pm-detail-detail.eps>download 1pm-detail-detail.eps</a>
<a href=1pm-detail-before.eps>download 1pm-detail-before.eps</a>
<a href=1pm-detail-net.eps>download 1pm-detail-net.eps</a>
<br />
<a href=1pm-detail.tar>download all (1pm-detail.png, 1pm-detail.dat, 1pm-detail.p)</a>
<br />

<a href=1pm-detail.dat>1pm-detail.dat (data file)</a>
<?php
$str = file_get_contents("1pm-detail.dat");
echo "<pre>$str</pre>";
?>

<a href=1pm-detail.dstat>1pm-detail.dstat (network raw data file)</a>, 
<a href=1pm-detail-net.dat>1pm-detail-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("1pm-detail.dstat");
echo "<pre>$str</pre>";
?>

<a href=1pm-detail.log>1pm-detail-r*.log (log files)</a>

<a href=1pm-detail.net>1pm-detail.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("1pm-detail.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

