# PHP basic architecture 
![](http://i.imgur.com/jN1EvBH.png)

app architecture 
* includes  <br />-->classes (define all the classess of the app) <br />
          -->config.php (define all settings of the app) <br />
          -->bootstrap.php (inludes all classes and config file) <br />
	  -->functions (Dir Including Common functions that will be used whole site) <br />

* themes <br />-->CSS<br />
       -->JS <br/>
* images
* API (define libraries or SDK)
* templates (global layout of the app)


# How it works

for any new file always include bootstrap.php<br />
`require (dirname(__FILE__) . '/includes/bootstrap.php');`

for any class ,no need to connect to db ,always start the new methode with global $db
exemple: <br />
``` php
function printUsers() //print all users on db
	{
		global $db;
		return $db->get('users'); // we use a prebuilt function from the MysqlDB class check out the documentation
	}
```
We use a prebuilt database class for fast implementation of function check out the documentation 
[https://github.com/joshcam/PHP-MySQLi-Database-Class](https://github.com/joshcam/PHP-MySQLi-Database-Class)
# themes 
the theme path is defined as global vraible path in the config.php (default css,js are bootstrap files)<br />
to load any CSS file use render_stylesheet()
``` php
<?php render_stylesheet("bootstrap.min.css"); ?> 

```


<br />Load any JS file use render_javascript() <br />

``` php
<?php render_javascript("bootstrap.min.js"); ?> 
```



# Templates
In this Dir you can define the default structure of the page 
header,footer,content .The default page is layout.php with css/js links.
# Installation guide (for noobs)
please check the wiki guide of the project (https://github.com/ihebBenSalem/StartNewPhpAppCoreBasic/wiki)
# Support ME
This software is developed during my free time and I will be glad if somebody will support me.<br />
For another projects and articles visite my blog [https://nodeme.blogspot.com/](https://nodeme.blogspot.com/)




       
