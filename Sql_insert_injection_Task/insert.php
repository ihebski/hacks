<?php
require 'config.php';

if (isset($_POST["username"]) && !empty($_POST["username"])) {
	# code...
	$username=$_POST["username"];
}
if (isset($_POST["msg"]) && !empty($_POST["msg"])) {
	# code...
	$msg=$_POST["msg"];
}

$myRequestQuery="insert into users(username,comments) values ('$username','$msg')";

$req=$sqli_connect->query($myRequestQuery);

if (!$req) {
  echo("Error description: " . mysqli_error($sqli_connect));
}
else
{
	header("location:index.php ");
}



?>