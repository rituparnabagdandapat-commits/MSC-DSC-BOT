import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# 1. CREATE BOT FIRST!
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. FLASK STUFF
app = Flask('')
@app.route('/')
def home():
    return "MBS BOT IS ALIVE"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

# 3. YOUR BOT COMMANDS HERE
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 4. RUN AT VERY BOTTOM - LAST 2 LINES!
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
