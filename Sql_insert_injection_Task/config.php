<?php
//config settings app
define("HOST","127.0.0.1");
define("DB_USERNAME","_ur_username_");
define("DB_PASSWORD","_ur_password_");
define("WORKING_DB","insert_sql_injection");

$sqli_connect=new mysqli(HOST,DB_USERNAME,DB_PASSWORD,WORKING_DB);

if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }