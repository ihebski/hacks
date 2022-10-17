#About Pwnerrank Notifier

This is a dirty script that helps you to get notification about the new tasks uploaded to Pwnerrank CTF plateform.

![home_page](http://i.imgur.com/w8bsGfS.png)

#The main idea of the script

When you check around the web site ,the notification bar not indicate the new uploaded tasks,but ,the /categories/ page gives you some information about the new added tasks .The script fetch every time it is executed the number field and compare it to an old one ,then save the new updates to old.db .

#How it works ?!
if new updates appears in the web site ,the script push a notification with the name of the category and the number of the added tasks.

![notification](http://i.imgur.com/tnhjRCY.png)

else "no update" msg shown on the terminal

![](http://i.imgur.com/90gh2VW.png)

#Run the script

You need to include your cookies to run the code .
exemple of cookies and sessions
`cmdCurl='curl --cookie "csrftoken=BLABLABLA; sessionid=BLABLABLA" http://www.pwnerrank.com/categories/ | grep "<small>" >>pwnerrank.com'
`

RUN : 
```
$ git clone https://github.com/ihebBenSalem/pwnerrank_Notifier.git
$ cd pwnerrank_Notifier
$ python notifier.py
```
#Recommendation
You can use `Worker` to run the script every 1 h and get the new updates . 
#Say thank you
Big thanks to Mr .Fahmi ben Khlifa CEO of Tunisian white hat security who have inspired me to write this code 
