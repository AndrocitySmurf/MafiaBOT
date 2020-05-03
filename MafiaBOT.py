import os
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import Bot
import asyncio
import random
import discord

bot = commands.Bot(command_prefix = 'mafia')
bot.remove_command('help')
started = False
assignperiod = False
joinlist = []
joinlistname = ['testuser1', 'testuser2', 'testuser3', 'testuser4', 'testuser5', 'testuser6', 'testuser7', 'testuser8']
temp = []
mafias = []
doctor = []
detective = []

@bot.event
async def on_ready():
    print('That\'s how mafia works')

@bot.command()
@has_role('Moderator')
async def start(ctx):
    global assignperiod
    global started
    if started == False:
        await ctx.send('**The game has started!**\n @everyone type in chat "mafiajoin" (without the quotes) if you wish to participate in this game of MAFIA\nYou will have **5 hours** to join!')
        assignperiod = True
        await asyncio.sleep(3600)
        await ctx.send('**4 more hours until the window to join closes!\nUse "mafiajoin" (without the quotes) if you want to enter!')
        await asyncio.sleep(3600)
        await ctx.send('**3 more hours until the window to join closes!\nUse "mafiajoin" (without the quotes) if you want to enter!')
        await asyncio.sleep(3600)
        await ctx.send('**2 more hours until the window to join closes!\nUse "mafiajoin" (without the quotes) if you want to enter!')
        await asyncio.sleep(3600)
        await ctx.send('@everyone **1 more hour until the window to join closes!\nUse "mafiajoin" (without the quotes) if you want to enter!')
        await asyncio.sleep(3600)
        await ctx.send('The window to join has closed. LET THE GAMES BEGIN!')
        started = True
        assignperiod = False
        temp = random.sample(joinlist, 4)
        mafias = temp[:2]
        detective = temp[2]
        doctor = temp[3]
        print(mafias + ' Mafias')
        print(detective + ' Detective')
        print(doctor + ' Doctor')
    else:
        await ctx.send('A game is in progress!')

@bot.command()
async def join(ctx):
    if assignperiod == True and ctx.author.id not in joinlist:
        userid = ctx.author.id
        username = ctx.author.name
        joinlist.append(userid)
        joinlistname.append(username)
        await ctx.send(f'*{username}* has been entered to play!')
        member = ctx.message.author
        role_id = 706238872606212159
        role = discord.utils.get(member.guild.roles, id = role_id)
        await member.add_roles(role)
    elif assignperiod == True and ctx.author.id in joinlist:
        await ctx.send('You are already registered for this game!')
    else:
        await ctx.send('The period to assign roles is over!')

@bot.command()
async def list(ctx):
    await ctx.send(f'Current users playing: (**{len(joinlistname)}** in total):')
    for username in joinlistname:
        await ctx.send(username)

@bot.command()
@has_role('Moderator')
async def modlist(ctx):
    for username in mafias:
        await ctx.send(username + ' - Mafia')
    await ctx.send(detective + ' - Detective')
    await ctx.send(doctor + ' - Doctor')

@bot.command()
@has_role(706240715398840360)
async def kill(ctx, member : discord.Member):
    member = member
    role = discord.utils.get(member.guild.roles, name = 'alive')
    await member.remove_roles(role)
    role2 = discord.utils.get(member.guild.roles, name = 'dead')
    await member.add_roles(role2)

@bot.command()
@has_role(706240715398840360)
async def confirm(ctx):
    for user in mafias:
        mafiauser = bot.get_user(user)
        await mafiauser.send('You have been selected as the mafia!\nPlease type \"mafiaconfirm\" (without the quotes) to conifrm your position as mafia!')

bot.run('NzA1NjQwNDg5NjA0MzUwMDMz.Xqyfdg.kh-I_g2HYYiQXiANZgkiOyYtlOM')

# user = bot.get_user(32143923849723904)
# await user.send('hello2')
