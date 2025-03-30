import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def bonjour(ctx):
  await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def quoi(ctx):
  await ctx.send("Feur !")

@bot.command()
async def extensionduterritoire(ctx):
  await ctx.send(random.choice(["Sphère de l'espace infini🤞 !", "Autel démoniaque🙏 !", "Jardin des ombres🤜🤛 !", "Orbe d'isolement🤙 !"]))

@bot.command()
async def absolutecinema(ctx):
  await ctx.send("https://tenor.com/view/gojo-absolute-cinema-gif-8932131737123141805")
  

token = os.environ['TOKEN_BOT_DISCORD']
bot.run(token)