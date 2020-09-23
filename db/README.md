# db

![Build Status](https://pbs.twimg.com/media/EiYn1w3XYAAAlN9?format=jpg&name=large)
# About db
Mini utility to store the list of the enumerated subdomains into an sqlite3 db. [one liner Style ]

Status: **Development**
## Features

* Remove duplicates
* Query database
* Clean results
* Pipe results to store data
## Chaining tools
You can pipe the subdomain tools results into db

> Example :

> subfinder + db
> ![Build Status](https://pbs.twimg.com/media/EiY1Sa1WsAIPSSp?format=jpg&name=large)


# Prod
#### Install Requirements
`sudo pip3 install Flask flask_sqlalchemy loguru uuid`

> Add it as a bash command
```bash
cp db /usr/bin
chmod +x /usr/bin/db
```

# Usage

- Add list of subdomains to database

`cat subdomains.txt | db
`
or 

`echo example.com | db`

- Search for domain

`db <domain.com>`
