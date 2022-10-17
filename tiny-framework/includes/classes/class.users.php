<?php
/**
* class users 
*/
class users
{
	
	function __construct()
	{
		# code...
	}

	function testme()
	{
		echo "Hi ! I'm user class";
	}

	function printUsers() //print all users on db
	{
		global $db;
		return  $db->get('users'); // we use a prebuilt function from the MysqlDB class check out the documentation
	}

}




