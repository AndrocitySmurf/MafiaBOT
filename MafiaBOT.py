import os
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import Bot
import asyncio
import random
import discord

bot = commands.Bot(command_prefix = 'mafia')
bot.remove_command('help')
ifstarted = 'false'
assignperiod = 'false'
join = []

@bot.event
async def on_ready():
    print('That\'s how mafia works')

@bot.command()
async def assign(ctx):
    if ifstarted == 'false':
        await ctx.send('**The game has started!**\nType in chat "mafiajoin" (without the quotes) if you wish to participate in this round of MAFIA')
        global ifstarted
        ifstarted = 'true'
    else:
        await ctx.send('A game is in progress!')
        
@bot.command()
async def join(ctx):
    print(ifstarted)
    if assignperiod == 'true':
        join.append(ctx.author.id)
        await ctx.send(f'*{ctx.author.name}* has been entered to play!')
    else:
        await ctx.send('The period to assign roles is over!')

bot.run('NzA1NjQwNDg5NjA0MzUwMDMz.XqupLQ.ZB4pQSOYKHQ--YN_5lI7BN8c6pU')

# user = bot.get_user(32143923849723904)
# await user.send('hello2')
