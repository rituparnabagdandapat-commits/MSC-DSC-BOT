from flask import Flask
from threading import Thread
import os

app = Flask('')
@app.route('/')
def home():
    return "MBS BOT IS ALIVE!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()
