'''
Save subdomains to database
Usage : 
      cat subdomains | python3 save.py
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
import sqlite3
import fileinput
from loguru import logger

app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False

dbname = "bb_record"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbname + '.sqlite'
db = SQLAlchemy(app)

class Target(db.Model):
    __tablename__ = 'Target'
    id = db.Column(db.Text, primary_key=True)
    subdomain = db.Column(db.Text)

    def __init__(self,id,subdomain):
        self.subdomain = subdomain
        self.id = id

db.create_all()

# save only new subdomains
def save(subdomain):
	if db.session.query(Target.id).filter_by(subdomain=line.strip()).scalar() is None :
		subs = Target(str(uuid.uuid4()),subdomain)
		db.session.add(subs)
		db.session.commit()
		logger.log('INFO',f'[+] {subdomain} added to database')
	else:
		logger.log('ERROR',f'[-] {subdomain} already exists')

if __name__ == '__main__':
	with fileinput.input() as f_input:
		for line in f_input:
			save(line.strip())

	
