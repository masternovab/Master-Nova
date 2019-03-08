import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import praw
import aiohttp
from imgurpython import ImgurClient
from random import choice, shuffle

client = commands.Bot(description="Master Nova", command_prefix=commands.when_mentioned_or("N!" ), pm_help = True)


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)







reddit = praw.Reddit(client_id='G-SK66FZT8at9g',
                     client_secret='DLqIkkdoD0K8xKpxuaMAhRscrS0',
                     user_agent='android:com.G-SK66FZT8at9g.SolarBot:v1.2.3 (by /u/LaidDownRepaer)')

CLIENT_ID = "1fd3ef04daf8cab"
CLIENT_SECRET = "f963e574e8e3c17993c933af4f0522e1dc01e230"
imgur = ImgurClient(CLIENT_ID,CLIENT_SECRET)

GIPHY_API_KEY = "dc6zaTOxFJmzC"

client.remove_command('help')

@client.event
async def on_ready():
	print("Logged in as:")
	print(client.user.name)
	print(client.user.id)
	print("Going To Be Ready")
	print("Ready")
	
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await client.say('<:MastersCheckmark:549986347578818560>. **He is above than my role.**')
        return
    
    try:
        await client.kick(user)
        await client.say(user.name+ '<:MastersCheckMark:550254369614987294> was kicked. Good bye' +user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('<:MastersCheckmark:549986347578818560> You Cant Kick Oof.')
        return
        
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await client.say('<:MastersCheckmark:549986347578818560>. **He is above than my role.**')
        return
    
    try:
        await client.ban(user)
        await client.say(user.name+ '<:MastersCheckMark:550254369614987294> was banned. Good bye' +user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('<:MastersCheckmark:549986347578818560> You Cant ban Oof.')
        return

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await client.say('<:MastersCheckmark:549986347578818560>. **He is above than my role.**')
        return
    
    try:
        await client.unban(user)
        await client.say(user.name+ '<:MastersCheckMark:550254369614987294> was banned. Good bye' +user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('<:MastersCheckmark:549986347578818560> You Cant ban Oof.')
        return

  
 
    
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permission.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="<:MastersCheckMark:550254369614987294> **{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="<:MastersCheckmark:549986347578818560> You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permission.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User UnMuted!", description="<:MastersCheckmark:549986347578818560> success")



@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)

async def unbanall(ctx):
    server=ctx.message.server
    ban_list=await client.get_bans(server)
    await client.say('Unbanning {} members'.format(len(ban_list)))
    for member in ban_list:
        await client.unban(server,member)
        await client.say("<:MastersCheckmark:549986347578818560> Success Unbanned all")

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 

@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name='Access')
    await client.add_roles(member, role)
    embed=discord.Embed(title="<:MastersCheckmark:549986347578818560> User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    await client.say(embed=embed)
    await asyncio.sleep(45*60)
    await client.remove_roles(member, role)


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="{} Is bad little info here:", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="UserName", value=user.name, inline=True)
    embed.add_field(name="UserID", value=user.id, inline=True)
    embed.add_field(name="UserStatus", value=user.status, inline=True)
    embed.add_field(name="User'sHighest role", value=user.top_role)
    embed.add_field(name="UserJoinedAt", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    await client.say("<:MastersCheckmark:549986347578818560> Info About user is above")

@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)
    await client.say("<:MastersCheckmark:549986347578818560> Successfuly did it yay We changed the nickname.")
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
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
        await client.delete_messages(mgs)      
        await client.say("<:MastersCheckmark:549986347578818560> Successfuly deleted messages")    
 
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
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
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__ServerOwner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ServeriD__', value = str(server.id))
    join.add_field(name = '__SeverMember Count__', value = str(server.member_count));
    join.add_field(name = '__Servers Text/Voice Channels__', value = str(channels));
    join.add_field(name = '__Server Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='ServerCreatedAt: %s'%time);

    return await client.say(embed = join);
    
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
	result = "The roles are:"
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)
    
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await client.delete_message(ctx.message)
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
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message)
     
@client.command(pass_context = True)
async def ownerinfo(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'OwnerName:',value ='XxKingNovaXx#0416',inline = False)
    embed.add_field(name = 'OwnerId:',value ='477463812786618388',inline = False)
    embed.add_field(name = 'Name+Id:',value ='XxKingNovaXx#0416 <=====> 477463812786618388',inline = False)
    await client.say(embed=embed)                 

@client.command(pass_context = True)
async def botinfo(ctx, *args):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'BotName:',value ='Master Nova#3349',inline = False)
    embed.add_field(name = 'BotId:',value ='520550412219318272',inline = False)    
    embed.add_field(name = 'BotName + Coding:',value ='Master Nova#3349 <======>520550412219318272',inline = False)  
    embed.set_footer(name = 'The Support Server',value = 'https://discord.gg/ThJCx6y',inline = False)
    embed.set_footer(name = 'Invite Me',value = 'https://discordapp.com/api/oauth2/authorize?client_id=520550412219318272&permissions=8&scope=bot',inline = False)

@client.command(pass_context=True)
async def remind(ctx, time=None, *,remind=None):
    time =int(time)
    time = time * 60
    output = time/60
    await client.say("I will remind {} after {} minutes for {}".format(ctx.message.author.name, output, remind))
    await asyncio.sleep(time)
    await client.say("Reminder: {} by {}".format(remind, ctx.message.author.mention))
    await client.send_message(ctx.message.author, "Reminder: {}".format(remind))
                  


@client.event
async def on_message(message):
    user_add_xp(message.author.id, 2)
    await client.process_commands(message) 
def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


@client.event
async def on_member_join(member):
    with open("users.json", "r") as f:
        users = json.load(f)

        await update_data(users, member)

        with open("users.json", "w") as f:
            json.dump(users, f)

@client.command(pass_context = True)
async def ping(ctx):


    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    message = "Pong!"
    await client.say('{}ms'.format(round((t2-t1)*1000)))


@client.command(pass_context =False)
async def flipcoin(playerChoice):
    outcomes = ['heads', 'tails']
    botChoice = random.choice(outcomes)
    
    playerChoice = playerChoice.lower()
    
    if botChoice == playerChoice:
    	
    	await client.say("It was " + playerChoice + " Congratulations")
    	
    elif botChoice == "heads" and playerChoice == "tails":
    		
    		await client.say("It was" + botChoice + "Fool")
    		
    elif botChoice == "tails" and playerChoice == "heads":
    			
    			await client.say("It was" + botChoice + "Lol Learn and watch")


          
@client.command(pass_context=True)
async def meme(ctx):
     async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Random memes 😂', description='The Best Memes', color=0x1100ce)
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)


@commands.has_permissions(manage_server =True)
@client.command(pass_context =True)
async def update(ctx, msg: str = None):
           server = client.get_server("528115053736493086")
           chan =  client.get_channel("530021036205277195")
           embed = discord.Embed(title=f"Bot Updates", description = "__**New Updates**__", color=0xC72323)
           embed.add_field(name ="Below This message are the Updates", value =msg)
           await client.send_message(chan, embed = embed)

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
async def howgay(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    gays= ["1% gay", "Never been a gay", "100% gay", "Half gay :thinking:", "10% gay", "99.75% gay", "50%gay", " you are gay not my poor son"]
    randomizer = random.choice(gays)
    if user == ctx.message.author:
        embed = discord.Embed(title="Go ask yourself if you are still a gay", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7dfff2)
        embed.add_field(name=f"{user.name}'s gay check results", value=f"{randomizer}")
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓    vav vav virus                ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓           vav vav virus     ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓      virus     ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓  coding virus    ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  us    ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ s  ] - {}-virus.exe Finishing.``'.format(hack))
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
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("Channel locked by: {}".format(ctx.message.author))

@client.command(pass_context = True)
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await bot.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("This Channel was unlocked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You noob you do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("This Channel was unlocked by: {}".format(ctx.message.author))

@client.command(pass_context=True)
async def eightball(ctx, *, question: str):
    answer = [":8ball: It is certain.", ":8ball: It is decidedly so.", ":8ball: Without a doubt.", ":8ball:Yes definitely.", ":8ball: You may rely on it.", ":8ball: As I see it, yes.", ":8ball: Most likely.", ":8ball:Outlook good.", ":8ball: Yes.", ":8ball:Signs point to yes.", ":8ball: Reply hazy, try again.", ":8ball: Ask again later.", ":8ball: Better not tell you now.", ":8ball: Cannot predict now.", ":8ball:Concentrate and ask again.", ":8ball: Don't count on it.", ":8ball: My reply is no.", ":8ball: My sources say no.", ":8ball:Outlook not so good.", ":8ball: Very doubtful."]
    randomizer = random.choice(answer)
    embed = discord.Embed(title=question, description=f"{randomizer}", color=0xC72323)
    await client.say(embed=embed)

@commands.has_permissions(manage_channels=True)
@client.command(pass_context=True)
async def setupwelcomer(ctx, channel, message):
	await client.create_channel(':tada: MasterNovaWelcome')
	await client.send_message.channel('Succesfuly made/setup welcomer.')


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == ':tada: MasterNovaWelcome':
           embed = discord.Embed(color=0xC72323)
           embed.set_author(name="🎉 Member has joined 🎉")
           embed.description = f'**Welcome {member.name}#{member.discriminator}   to {member.server.name}**\n\nPlease respect each other and follow the rules.'
           embed.set_thumbnail(url=member.avatar_url)
           embed.timestamp = datetime.datetime.utcnow()
           embed.set_footer(text='We now have {} members'.format(str(member.server.member_count)))
           await client.send_message(channel, embed=embed) 

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == ':tada: MasterNovaWelcome':
           embed = discord.Embed(color=0xC72323)
           embed.set_author(name = 'User has left')
           embed.description=f' {member.name}#{member.discriminator} has left {member.server.name} server! We hope to see you again in the server.'
           embed.set_thumbnail(url=member.avatar_url)
           embed.timestamp = datetime.datetime.utcnow()
           embed.set_footer(text='We now have {} members'.format(str(member.server.member_count)))
           await client.send_message(channel, embed=embed)

@client.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(result)

@client.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))

@client.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await client.say(content)

@client.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await client.say('{0.name} joined in {0.joined_at}'.format(member))


@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "a tweet was made by **{user.name}** ".format(usernamename, txt)
            await client.say(embed=embed)

@client.command(pass_context=True)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await client.say('Use it like ``N!rps rock or scissors or paper`` anyone of them to make this command work properly')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)

@client.command(pass_context=True)
async def invites(ctx):
    total_uses=0
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    server = ctx.message.channel.server
    invites = await client.invites_from(server)
    invlb = f'Invites of {ctx.message.server.name}\n'
    for invite in invites:
      total_uses += invite.uses
      invlb += f'User: {invite.inviter.name}\nInvites: {invite.uses}\n'
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Invites List',value=invlb)
    embed.add_field(name='Total Invites',value=total_uses)
    embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await client.say(embed=embed)

@client.command(pass_context = True)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
	
@client.command(pass_context = True)
async def announce(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('Invalid args. Use this command like ``N!announce #channel text here``')
        return
    else:
        if member.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
            await client.send_message(channel, embed=embed)
            await client.delete_message(ctx.message)
	
@client.command(pass_context = True)
async def delchannel(ctx, channel: discord.Channel=None):
    if channel is None:
        await client.delete_channel(ctx.message.channel)
        await client.send_message(ctx.message.author, "{} channel has been deleted in {}".format(ctx.message.channel.name, ctx.message.server.name))
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            await client.delete_channel(channel)
            await client.say("{} channel has been deleted.".format(channel.name))


@client.command(pass_context = True)
async def addchannel(ctx, channel: str=None):
    server = ctx.message.server
    if channel is None:
        await client.say("Please specify a channel name")
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            everyone_perms = discord.PermissionOverwrite(send_messages=None, read_messages=None)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            await client.create_channel(server, channel, everyone)
            await client.say("{} channel has been created.".format(channel))
	
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
         
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description="**{user.name}'s** avatar", color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)        
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)
	
@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

   
@client.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
   if user is None or msg is None:
       await client.say('Invalid args. Use this command like: ``N!dm @user message``')
   if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
   else:
       await client.send_message(user, msg)
       await client.delete_message(ctx.message)          
       await client.say("Success! Your DM has made it! :white_check_mark: ")

@client.command(pass_context = True)
async def addrole(ctx,*, role:str=None):
    user = ctx.message.author
    if user.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
		
@client.command(pass_context = True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
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
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("Use this command like ``N!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if value is None:
        await client.say("Use this command like ``N!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await client.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await client.say("{} role colour has been edited.".format(role))
        
@client.command(pass_context = True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")
        

        
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = '``Our Help Server Link`` ',value ='https://discord.gg/ThJCx6y',inline = False)
    embed.add_field(name = '``N!modhelp`` ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
    embed.add_field(name = '``N!generalhelp`` ',value ='Explaines all the commands which are usable by everyone.',inline = False)
    await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs For Information')

@client.command(pass_context = True)
async def modhelp(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'N!say(Admin permission required) ',value ='Use it like ``N!say <text>``',inline = False)
    embed.add_field(name = 'N!kick(kick members permission required) ',value ='Use it like ``N!kick <User>``',inline = False)
    embed.add_field(name = 'N!ban(ban memb permission required) ',value ='Use it like ``N!ban <user>``',inline = False)
    embed.add_field(name = 'N!unban(ban memb permission required) ',value ='Use it like ``N!unban <user>``',inline = False)
    embed.add_field(name = 'N!warm(Admin permission required) ',value ='Use it like ``N!warn <user> <text>``',inline = False)
    embed.add_field(name = 'N!warnings(Admin permission required) ',value ='Use it like ``N!warnings <user>``',inline = False)
    embed.add_field(name = 'N!mute(Admin permission required) ',value ='Use it like ``N!mute <user>``',inline = False)
    embed.add_field(name = 'N!unmute(Admin permission required) ',value ='Use it like ``N!unmute <user>``',inline = False)
    embed.add_field(name = 'N!unbanall(Admin permission required) ',value ='Use it like ``N!unbanall``',inline = False)
    embed.add_field(name = 'N!userinfo(Admin permission required) ',value ='Use it like ``N!userinfo <user>``',inline = False)
    embed.add_field(name = 'N!serverinfo(Admin permission required) ',value ='Use it like ``N!serverinfo``',inline = False)
    embed.add_field(name = 'N!poll(Admin permission required) ',value ='Use it like ``N!poll <opt 1 then 2 - 10>``Must Be more than 1 opts',inline = False)
    embed.add_field(name = 'N!say(Admin permission required) ',value ='Use it like ``N!say <bow bow>``',inline = False)
    embed.add_field(name = 'N!embed(Admin permission required) ',value ='Use it like ``N!emebed <msg Like Bow Bow >``',inline = False)
    embed.add_field(name = 'N!setnick(Admin permission required) ',value ='Use it like ``N!setnick <user> <name>``',inline = False)
    embed.add_field(name = 'N!bans(Admin permission required) ',value ='Use it like ``N!bans``',inline = False)
    embed.add_field(name = 'N!clear(Admin permission required) ',value ='Use it like ``N!clear <amount>1-100``',inline = False)
    embed.add_field(name = 'N!roles(Admin permission required) ',value ='Use it like ``N!roles``',inline = False)
    embed.add_field(name = 'N!membercount(Admin permission required) ',value ='Use it like ``N!membercount``',inline = False)
    embed.add_field(name = 'N!lock(Admin permission required) ',value ='Use it like ``N!lock <channelname>``',inline = False)
    embed.add_field(name = 'N!mute(Admin permission required) ',value ='Use it like ``N!unlock <channelname>``',inline = False)
    embed.add_field(name = 'N!setupwelcomer(Admin permission required) ',value ='Use it like ``N!setupwelcomer``',inline = False)
    embed.add_field(name = 'N!rolecolour(Admin permission required) ',value ='Use it like ``N!rolecolour <role>``',inline = False)
    embed.add_field(name = 'N!roleinfo(Admin permission required) ',value ='Use it like ``N!roleinfo <role>``',inline = False)
    embed.add_field(name = 'N!dm(Admin permission required) ',value ='Use it like ``N!dm <user> <msg>``',inline = False)
    dmmessage = await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs For Information')        
                    
@client.command(pass_context = True)
async def generalhelp(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'N!guess',value ='Use it like ``N!guess <it guesses a number>``',inline = False) 
    embed.add_field(name = 'N!remind',value ='Use it like ``N!remind <time> <reason>``',inline = False)                 
    embed.add_field(name = 'N!ping',value ='Use it like ``N!ping``',inline = False)
    embed.add_field(name = 'N!flipcoin',value ='Use it like ``N!flipcoin``',inline = False)  
    embed.add_field(name = 'N!avatar',value ='Use it like ``N!avatar``',inline = False)    
    embed.add_field(name = 'N!invites',value ='Use it like ``N!invites``',inline = False) 
    embed.add_field(name = 'N!rps',value ='Use it like ``N!rps <rock,paper or seicor> forgot spelling``',inline = False)  
    embed.add_field(name = 'N!roll',value ='Use it like ``N!roll``',inline = False)     
    embed.add_field(name = 'N!repeat',value ='Use it like ``N!repeat``',inline = False)
    embed.add_field(name = 'N!choose',value ='Use it like ``N!choose``',inline = False) 
    embed.add_field(name = 'N!eightball',value ='Use it like ``N!eightball``',inline = False)   
    embed.add_field(name = 'N!ownerinfo',value ='Use it like ``N!ownerinfo``',inline = False)    
    embed.add_field(name = 'N!meme',value ='Use it like ``N!meme``',inline = False)
    embed.add_field(name = 'N!virus',value ='Use it like ``N!virus``',inline = False)   
    embed.add_field(name = 'N!tweet',value ='Use it like ``N!tweet``',inline = False)   
    embed.add_field(name = 'N!howgay',value ='Use it like ``N!howgay``',inline = False)   
    embed.add_field(name = 'N!virgin',value ='Use it like ``N!virgin``',inline = False)  
    dmmessage = await client.send_message(author,embed=embed)
    await client.say('📨 Check dms for  help')   
    
client.run(os.getenv("Token"))                                                                       
