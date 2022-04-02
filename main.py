import os
import discord

#import token from consts.py
from consts import DISCORD_TOKEN


#import logging function
import logging
logging.basicConfig(level=logging.INFO)

#constants for bot prefix
TOKEN = DISCORD_TOKEN
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

#play youtube audio from user search
@bot.command(name='play')
async def play(ctx, *, query):
    url = getURL(query)
    voice = get(bot.voice_clients, guild=ctx.guild)

    yt = YouTube(url)
    voice.play(yt)


#get url from first youtube result from user search
def getURL(query):
    query = query.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find(attrs={'class': 'yt-uix-tile-link'})
    return 'https://www.youtube.com' + results['href']



bot.run(TOKEN)
