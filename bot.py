from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "MBS BOT IS ALIVE!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

# At the very bottom of your file
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))  # or TOKEN
