<html>
<head>

</head>
<title></title>
<body>

<h2>LAN  (<a href=../>../UP</a>)</h2>

<a href=.png><img src=.png></a>
<a href=-net.png><img src=-net.png></a>
<br />

<a href=.eps>download .eps</a>, 
<a href=-net.eps>download -net.eps</a>
<br />
<a href=.tar>download all (.png, .dat, .p)</a>
<br />

<a href=.dat>.dat (data file)</a>
<?php
$str = file_get_contents(".dat");
echo "<pre>$str</pre>";
?>

<a href=.dstat>.dstat (network raw data file)</a>, 
<a href=-net.dat>-net.dat (network modified data file)</a>
<?php
$str = file_get_contents(".dstat");
echo "<pre>$str</pre>";
?>

<a href=.log>-r*.log (log files)</a>

<a href=.net>.net (dstat -cnm file)</a>
<?php
$str = file_get_contents(".net");
echo "<pre>$str</pre>";
?>

<br />

</body>
</html>

