Do you want to receive notifications without even opening the Saraha web site? SarahaPy-Notifications provides you with a python script, that solves this purpose.

#About Saraha Notifier

This is a dirty script that helps you to get notifications, alerts about the new messages received on Saraha.com website.
![home_page](http://i.imgur.com/2fSFAjA.png)

#The main idea of the script

When you check around the website, the notification bar doesn't indicate the new MSG (only email notification), but, the /Message page gives you some information about the sum of the received messages. The script fetches the number field and compare it with an old one, then save the new updates.

#How it works ?!
if new updates appear on the website, the script push a notification on the Desktop. 

![notification](http://i.imgur.com/AR4tnI5.png)

else "no update" nothing happen :p !,The script parse the new msg ,every 1 min left 

![](http://i.imgur.com/4PLElEK.png)

#Run the script

You need to include your cookies to run the code .
exemple of cookies and sessions
`	"Cookie":"
_ga=GA1.2.732206321.1486515058; ARRAffinity=f0f176a75411a5516e373b4e86c264f885774d994d116c0ce85d12a8e73a1fbd; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8EwdTF4_2Q5PkRGbKl9YEzBIUAdErq66a9YHAiaiscxqA8sRjIlbIT5IvFfvTzhFn4nfhjohIFA1lTLYVqIiP2UNytZ7qmIwdIZKKchQShTqeh4C2ZMtzPzZFwGOJ09Vu-xxe2kRcjKiPcRkEN6ZMXs; _gat=1; .AspNetCore.Identity.Application=CfDJ8EwdTF4_2Q5PkRGbKl9YEzDyF8Iiw4zjQP0-_fWNHefSmMijsyyQvQoqJqKuSlgAJ9qyHlwNTW1COvv8iou2NBqREjF8kIeXTOqxYl3ucAvVp5Aukq-h_WggDr0rsT5LGYJoPaTHoAXetYE0dYuCjVwQ1xS2Nfixv0_q6W24-o57OHMCRJ9slgjQ6P9irEsbX5v6af1d6Fmk55FCSQYMU5pIN00pY9duF61-lfUjGAO60k84VZJykVAlu8tCdA4e0CSvE6jjd4bwSk3hdADA3tMcO_7hKXNB28yOzGNKr4e2EWEay4YNm5OuPX1CAXFIZvFb4HQEfrLIQsMCPI1AJPJicAC7j07x94tVA2pvxwT3NZzSPfxfpRDQAh1P9yOeyFxpZFlKe6gRi0y_h8TWciJiR2-dlN8fGsUMbEtUKOS3_FCPMjTztKMZLUCmbtv3b_ykhdXU1hsG_srOp3tEvEExxkq1Kg0BLNpuTI-CrLhYdU5dQxDcRQbWANgz1nwcQ3uGWKqTERjCZ7V2zahiI0jzRmoE6jHHYP0b6zY6nPmEHNbz-d9a6Oj4bdvAo33zSXYVmTmF1R_KJuKheN-iZ2o"
`

RUN : 
```
$ git clone https://github.com/ihebski/SarahahPyNotifier
$ cd SarahahPyNotifier
$ python saraha.py
```
#About the project
Saraha.com is scaling so fast. Am not the fan of the website, but I have used it as a social experience to develop a new project called Litsy project based on social experiences and emotions.
#Chrome extension
the chrome extension we'll coming soon
#Support Me 
This software is developed during my free time and I will be glad if somebody will support me.
For another projects and articles visite my blog https://nodeme.blogspot.com/
