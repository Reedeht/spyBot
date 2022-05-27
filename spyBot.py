import discord
from discord.ext import commands
import sqlite3

##################################

#####     Easy Edit Menu     #####

##################################

prefix = "!" # Enter Prefix Here
owners = [394811838287577089, 0] # your discord ID, or other people you want to be able to edit the data (Spies etc)
viewers = [394811838287577089, 0] # every person that can view the data (Empire members)
token = "" # your bots token, from discord.
empire = "" # Your empire name.
globalViwer = False # set to True if you want everyone in any empire to be able to view the data.

##################################

#####     Easy Edit Menu     #####

##################################


dataBase = sqlite3.connect("spy.sqlite")# Data base
cursor = dataBase.cursor() #Cursor

# DISCORD LAUNCHER INFORMATION

client = commands.Bot(command_prefix=(prefix), case_insensitive=True)
client.remove_command("help")

# HELP MENU
@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.gold())
    embed.add_field(name="Spy Bot", value=f"United Nations, Public Spy Support Bot, created by Developers for Players with :heart:\n\nThis Bot is operated by: {empire}", inline=False)
    embed.add_field(name="`Viewer Permissions`", value=f"{prefix}lookup <id>, drops all the information on a specific person.")
    embed.add_field(name="`Owner Permissions`", value=f"{prefix}register <id>, registers a new user ID.\n{prefix}update <id>, Updates data on a specific user", inline=False)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"{empire} | {prefix}help"))

@client.command()
async def update(ctx):
    if ctx.message.author.id in owners:
        text = ctx.message.content[len(ctx.prefix) + len(ctx.invoked_with):]
    else:
        await ctx.send("You do not have permission to use this interaction.")
        return
    if text == "":
        await ctx.send("```data```\n\n\nid\narmy\nrecruit\nairship\nairPack\nbulletPack\nartillery\nartilleryPack\nshield\naa\ntrench\nweaponDamage\nrecruitTime\nbarracks")
        await ctx.send(f"Edit Guide:\n\n**Note**: This Database is __live__, changes cannot be overhauled.\n\nType the following:\n`{prefix}update UPDATE data set <type of data> = <variable> WHERE id = <user of id>\nUser ID = Discord User ID, i.e 394811838287577089\nType of Data like, Airship, Artillery etc. enter as shown in above message.\nVariable, the amount you have found, such as 2 for 2 hours of recruit time or shield time.")
    else:
        try:
            cursor.execute(f"""{text}""")
        except:
            await ctx.send("Unable to edit")
        dataBase.commit()
        await ctx.send(f"{text}\nHas been executed!")

@client.command()
async def register(ctx):
    if ctx.message.author.id in owners:
        text = ctx.message.content[len(ctx.prefix) + len(ctx.invoked_with):]
    else:
        await ctx.send("You do not have permission to use this interaction.")
        return
    cursor.execute(f"INSERT INTO data(id) VALUES ({text})")
    dataBase.commit()
    await ctx.send(f"Added {text} into the Register")

@client.command()
async def lookup(ctx):
    if globalViwer == True:
        text = ctx.message.content[len(ctx.prefix) + len(ctx.invoked_with):]
    else:
        if ctx.message.author.id in viewers:
            text = ctx.message.content[len(ctx.prefix) + len(ctx.invoked_with):]
        else:
            await ctx.send("You do not have permission to use this interaction.")
            return

    cursor.execute(f"SELECT army FROM main WHERE id = {text}")
    var = cursor.fetchone()
    if var == None:
        await ctx.send("Sadly, we do not have data on this user yet!")
        return
    var = str(var)
    var = var[1:-2]
    army = int(var)
    cursor.execute(f"SELECT recruit FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    recruit = int(var)
    cursor.execute(f"SELECT airship FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    airship = int(var)
    cursor.execute(f"SELECT airPack FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    airPack = int(var)
    cursor.execute(f"SELECT bulletPack FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    bulletPack = int(var)
    cursor.execute(f"SELECT artillery FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    artillery = int(var)
    cursor.execute(f"SELECT artilleryPack FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    artilleryPack = int(var)
    cursor.execute(f"SELECT shield FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    shield = int(var)
    cursor.execute(f"SELECT aa FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    aa = int(var)
    cursor.execute(f"SELECT trench FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    trench = int(var)
    cursor.execute(f"SELECT weaponDamage FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    weaponDamage = int(var)
    cursor.execute(f"SELECT recruitTime FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    recruitTime = int(var)
    cursor.execute(f"SELECT barracks FROM main WHERE id = {text}")
    var = cursor.fetchone()
    var = str(var)
    var = var[1:-2]
    barracks = int(var)
    embed = discord.Embed(colour=discord.Colour.gold())
    embed.add_field(name="Data Collected!", value=f"Army: {army}\nRecruit: {recruit}\nAirship: {airship}\nAir Pack: {airPack}\nBullet Pack: {bulletPack}\nArtillery: {artillery}\nArtillery Pack: {artilleryPack}\nShield: {shield}\nAnti-Air: {aa}\nTrench: {trench}\nWeapon Damage: {weaponDamage}\nRecruit Time: {recruitTime}\nBarracks: {barracks}")
    await ctx.send(embed=embed)

client.run(token)
