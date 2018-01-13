# -*- coding: utf-8 -*-
# Use Python 3
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import telepot
import sys
reload(sys) 
sys.setdefaultencoding('UTF8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

    
@app.route('/')
def hello():
    return 'strix bot'
def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 if content_type == 'text':
    command = msg['text']
    user = User(command, command)
    db.session.add(user)
    db.session.commit()
    bot.sendMessage(chat_id, text= command)

    
    
bot = telepot.Bot('375977039:AAFOsgDE7kv9K9hRCHA1UOofhGjbxSXv4LA')
bot.message_loop(handle)
print ('straxic0o0o0o0o0o0o0o0o0')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
