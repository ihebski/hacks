#!/bin/bash
## This script is used to monitor/restart several services and notify maintainer in case of failure
# Add it to crontab for regular checks

## Configure script
export smtp="<Smtp-server>:<Port>"
email="<Maintainer Email>"
host=`hostname -f`
 
 
# list of services to be monitored
services=("httpd" "elasticsearch" "kibana")
echo "[+] Start services health check"
 
for service in ${services[*]}; do
 
echo "[*] Check service: $service"
# First check of the process
if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 )) ; then
echo "   [+] Check 1 : $service is running."
else
echo "   [+] restart $service"
systemctl restart $service
subject="$service at $host was restarted"
echo "$service at $host wasn't running and has been started" | mailx -s "$subject" $email
fi
 
# Second check after restart; could fails to be started
if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0  )); then
echo "   [+] Check 2 : $service is running."
else
echo "  [-] Service $service is down."
subject="Alert ! Service $service is down at $host"
echo "Unable to Start $service at $host" | mailx -s "$subject" $email
fi
done
