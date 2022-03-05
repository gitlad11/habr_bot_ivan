from pkgutil import get_data
from flask import Flask
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time
import schedule
from flask_pymongo import pymongo
from flask import current_app, g
import dns
import parsing

#MongoDB
Connection_DB = 'mongodb+srv://admin:password@cluster0.pcwin.mongodb.net/datab?retryWrites=true&w=majority'
client = pymongo.MongoClient(Connection_DB)
db = client.get_database('datab')



#@app.route('/')
def dibil():
    print('parsing')
    now = datetime.datetime.now()
    time = now.strftime("%m-%d %H:%M")
    
    data = parsing.parsing()

    post = { 'author' : "Ivan_bot@gmail.com", 
              "title" : data['title'],
              "coments" : [],
              'liked' : [],
              "date" : str(time),
              "image" : "https://assets.habr.com/habr-web/img/splashes/splash_2436x1125.png",
              "text" : data['body'] }

    db.posts.insert_one(post)

sched = BackgroundScheduler(daemon=True, timezone="Europe/Berlin")
sched.add_job(dibil,'interval', minutes=15)
sched.start()

#FLASK SERVER 
app = Flask(__name__)

if __name__ == "__main__":
  time.sleep(1)
  print("pending")
  schedule.run_pending()
  app.run(port=4000)


