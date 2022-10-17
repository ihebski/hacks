<?php
/**
 * Initiation File
 * Including All base classes as well as config file
 */

//Include Config file
	
	require_once(dirname(__FILE__) . "/config.php");
//Include general function of the app
	include_once(dirname(__FILE__) . "/functions/security.php");
	include_once(dirname(__FILE__) . "/functions/general.php");
//Include layout of the page with css and Js no need to includes this anymore on pages	
	require_once(dirname(dirname(__FILE__))."/templates/layout.php");

/*
if(DEVELOPER_MODE){
	ini_set('display_startup_errors', 1);
	ini_set('display_errors', 1);
	error_reporting(-1);
}*/


//Auto load classes
LoadClass("class.users");
		

?>