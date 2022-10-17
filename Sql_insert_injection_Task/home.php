
	<div class="jumbotron">
		<div class="container">
			<form  method="POST" action="insert.php" role="form" id="myform">
			<p>What is your feedback about our service ?!</p>			
				<div class="form-group">
					<label for="">Username</label>
					<input type="text" class="form-control" placeholder="username" name="username">
				</div>
				<div class="form-group">
					<label for="">message</label>
					<textarea class="form-control" rows="3" name="msg"></textarea>
				</div>
				<button type="button" class="btn btn-primary" id="sub">Submit</button>
			</form>
		</div>
	</div>

<script type="text/javascript">
	$("#sub").click(function(){
$("#myform").submit();
});

</script>