import discord, os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"GREEN ONLINE {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Bot is ONLINE 🟢")

bot.run(os.getenv("DISCORD_TOKEN"))
