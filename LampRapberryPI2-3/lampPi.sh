"
Lamp for RPI 2/3 
This script helps u to install the full lamp on ur RPI 2/3 
by Sold1er 
Email:ihebbensalem.dev@gmail.com
"
#Update the system if u need to upgrade remove #
sudo aptitude update
#sudo aptitude upgrade

#_______________________Install apache 2
sudo aptitude install apache2

#Change the persmissions
sudo chown -R pi:www-data /var/www/html/
sudo chmod -R 770 /var/www/html/

#_______________________Install php5
sudo aptitude install php5

#Change the default index.html to index.php :to test the server
#echo "<?php phpinfo(); ?>" > /var/www/html/index.php

#MysqlServer ,You can user root as password for the default login,then change it later
sudo aptitude install mysql-server php5-mysql
#mysql --user=root --password=root

#______________________Install Phpmyadmin 
sudo aptitude install phpmyadmin
