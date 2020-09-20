#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
import sqlite3
import fileinput
from loguru import logger
import sys

app = Flask(__name__)

# Change the default db path
dbname = "bb_record"
dbpath = "/tmp"

# SQLAlchemy config/Disable warnings for a clean output $_$
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbpath}/{dbname}.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
stats = logger.level("STATS", no=38, color="<yellow>", icon="📈")

# Model -> could be changed later on
class Target(db.Model):
    __tablename__ = 'Target'
    id = db.Column(db.Text, primary_key=True)
    subdomain = db.Column(db.Text)

    def __init__(self,id,subdomain):
        self.subdomain = subdomain
        self.id = id
db.create_all()


def save(subdomain):
	if db.session.query(Target.id).filter_by(subdomain=subdomain).scalar() is None :
		subs = Target(str(uuid.uuid4()),subdomain)
		db.session.add(subs)
		db.session.commit()
		logger.log('INFO',f'[+] {subdomain} added to database')
	else:
		logger.log('ERROR',f'[-] {subdomain} already exists')

def search(subdomain):
	sub = db.session.query(Target).filter(Target.subdomain.like(f"%{subdomain}%")).all()
	if sub :
		for row in sub:
			logger.log('INFO',row.subdomain)
		logger.log("STATS", f'We have found {len(sub)} subdomain ! Happy Hacking $_$')
	else:
		logger.log('WARNING',f'[-] {subdomain} NOT FOUND.')


def main():
	# use stdin if it's full                                                        
	if not sys.stdin.isatty():
	    for subdomains in sys.stdin:
	    	save(subdomains.strip())
	# read subdomain as argument                                            
	else:
		if len(sys.argv) > 1:
			search(sys.argv[1])
		else:
			print("Usage:\n     Store new subdomains : cat targets | python3 db.py \n     Search subdomains: python3 db.py <domain>")

if __name__ == '__main__':
	main()

	
