<?php
require 'config.php';

$req=$sqli_connect->query("select * from users order by id_user DESC");

if (!$req) {
	echo "Render view not working! Error query";
}

while ($data=$req->fetch_array()) {

?>
<div class="well">
<div class="alert alert-info">
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true"></button>
	<strong>username :<b><?php  echo $data["username"]; ?></b></strong>
</div>
	
<div class="alert alert-success">
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true"></button>
	<?php  echo $data["comments"]; ?>
</div>


</div>

<?php } ?>


