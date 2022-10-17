#!/bin/bash

#Name of your CTF.
#Do not use spaces in the name.
#This isn't the name people will see when they visit the site.
#You can change that later.
#If you're unsure, do not change this name. :)
CTF_NAME="CTFd"

#Gonna need it.
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root." 
   exit 1
fi

#Perform updates and upgrades (upgrade isn't that important).
apt-get -y update;
#apt-get -y upgrade;

#Setup CTFd home.
mkdir /home/CTFd;
cd /home/CTFd;

#Get CTFd.
git clone https://github.com/CTFd/CTFd.git;
cd CTFd;
./prepare.sh;

#Uncomment if you want to edit the config file.
#vim CTFd/config.py;

#Install nginx.
apt-get -y install nginx;
ufw allow 'Nginx Full';
ufw allow 'Nginx HTTP';
ufw allow 'Nginx HTTPS';

#Install uwsgi.
apt-get -y install uwsgi;
apt-get -y install uwsgi-plugin-python;

#Write config for uwsgi.
cd /etc/uwsgi/apps-available/;
UWSGI_APP="
[uwsgi]
chmod-socket = 777\n
chdir = /home/CTFd/CTFd/\n
mount = /=wsgi.py\n
plugin = python\n
module = wsgi\n
master = true\n
processes = 1\n
threads = 1\n
vacuum = true\n
manage-script-name = true\n
wsgi-file = wsgi.py\n
callable = app\n
die-on-term = true\n
uid = www-data\n
gid = www-data\n";
echo -e $UWSGI_APP > CTFd;
ln -s /etc/uwsgi/apps-available/CTFd /etc/uwsgi/apps-enabled/CTFd;

#Write nginx config.
cd /etc/nginx/sites-available/;
NGINX_CONFIG="
server {\n
\tlisten 80;\n
\tserver_name $CTF_NAME;\n
\tlocation = /favicon.ico { access_log off; log_not_found off; }\n
location /static/ {\n
\troot /home/CTFd/CTFd/CTFd;\n
}\n
\tlocation / {\n
\tinclude uwsgi_params;\n
\tuwsgi_pass unix:/tmp/$CTF_NAME.sock;\n
\t}\n
}\n";
echo -e $NGINX_CONFIG > CTFd;
rm ../sites-enabled/default;
ln -s /etc/nginx/sites-available/CTFd /etc/nginx/sites-enabled/default;

#Write activation script.
cd /home/CTFd/CTFd/;
echo -e "cd /home/CTFd/CTFd/" > start.sh;
echo -e "nohup uwsgi_python27 -s /tmp/$CTF_NAME.sock -w \"CTFd:create_app()\"&" >> start.sh;
echo -e "service nginx start" >> start.sh;
echo -e "sudo chmod 777 /tmp/$CTF_NAME.sock" >> start.sh;

#Write de-activation script.
echo -e "ps -ef | grep uwsgi_python27 | grep -v grep | awk '{print $2}' | xargs kill" > stop.sh;
echo -e "service nginx stop" >> stop.sh;

chmod +x start.sh;
chmod +x stop.sh;

#Setup persistence (run at boot).
cd /etc/cron.d/;
echo -e "SHELL=/bin/sh" > $CTF_NAME;
echo -e "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin" >> $CTF_NAME;
echo -e "@reboot   root    /home/CTFd/CTFd/start.sh" >> $CTF_NAME;

reboot;

#Please allow up to 10 minutes after reboot to allow nginx, uwsgi, and CTFd to initialise for the first time.