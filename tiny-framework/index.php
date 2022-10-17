<?php
require (dirname(__FILE__) . '/includes/bootstrap.php');
?>
<div class="jumbotron">
	<div class="container">
		<h1>Hello, world!</h1>
		<p>This is my First App</p>
		
	</div>
</div>

<?php 
users::testme();
echo "<br><strong>UsersList</strong><br>";
$user=users::printUsers(); //print the users from the users class 
foreach ($user as $key => $row) {
echo $row["id"]." ".$row["username"].' =>  '.$row["name"].'<br>';
}?>
