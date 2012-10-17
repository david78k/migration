<html>
<head>

</head>
<title>concur</title>
<body>

<h2>WAN simulation concur (<a href=../>../UP</a>)</h2>

<a href=concur.png><img src=concur.png></a>
<a href=concur-detail.png><img src=concur-detail.png></a>
<a href=concur-before.png><img src=concur-before.png></a>
<a href=concur-net.png><img src=concur-net.png></a>
<br />

<a href=concur.eps>download concur.eps</a>, 
<a href=concur-detail.eps>download concur-detail.eps</a>
<a href=concur-before.eps>download concur-before.eps</a>
<a href=concur-net.eps>download concur-net.eps</a>
<br />
<a href=concur.tar>download all (concur.png, concur.dat, concur.p)</a>
<br />

<a href=concur.dat>concur.dat (data file)</a>
<?php
$str = file_get_contents("concur.dat");
echo "<pre>$str</pre>";
?>

<a href=concur.dstat>concur.dstat (network raw data file)</a>, 
<a href=concur-net.dat>concur-net.dat (network modified data file)</a>
<?php
$str = file_get_contents("concur.dstat");
echo "<pre>$str</pre>";
?>

<a href=concur.log>concur-r*.log (log files)</a>

<a href=concur.net>concur.net (dstat -cnm file)</a>
<?php
$str = file_get_contents("concur.net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

