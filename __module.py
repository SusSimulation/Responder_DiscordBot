import asyncio
import datetime
import os
from subprocess import call
import time
import random
import discord
import json
import psutil
from discord.ext import commands

TIMEONLINE = time.time()

MAINPATH = str(os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/"
with open(f"{MAINPATH}TOKEN.txt", "r") as f:
    RESPONDERTOKEN = f.read()

VERSION = 4.0

intents = discord.Intents().all()
responder = commands.Bot(command_prefix='$',help_command=None,intents=intents)
ADMINS = [800558571129274450,879210381661335592]

COOLGUILDS = [
1012146008341360721
]

# not in use yet
WelcomeGuilds = []
# Need to extract info from .json file

# add info to .json list.

    

Commands = {
    "$help" : "Bare bones help command and display the commands, and sometimes more. PS; you're kinda using it right now...",
    "$ti and $tic" : "(PS: The difference in $ti and $tic is that $ti only allows 'yes' or no answers, comparing to $tic it allows all types of answers) Trust issues is a game designed for developing trust issues in your fellow friends. Start off by typing a custom question, then watch the bot count all of the responses and let everyone know what they said without knowing who said it.",
    "$myid" : "Ever forget your ID?",
    "$clear":"$clear (amount wanting to clear), command that will delete messages.",
    "$serverinfo" : "Info on the server.",
    "$channelinfo" : "Info on the current channel"
}

class SimpleEmbed:
    def __init__(self,t,des=None):
        self.des = des
        self.t = t
    def rn(self):
        if self.des == None:
            return discord.Embed(title=self.t,color=0xff0000)
        else:
            return discord.Embed(title=self.t,description=self.des,color=0xff0000)

class AddAudit:
    def __init__(self,info=None):
        self.info = info
        self.Print()
    def Print(self):
        self.msg = f' {self.info} '
        print(f">>> {self.msg} <<<")


class ReturnInfo:
    def __init__(self,ctx):
        self.ctx = ctx
    def rn(self):
        try:
            return f"{self.ctx.guild} with the id of {self.ctx.guild.id}"
        except:
            return f"{self.ctx.author} with the id of {self.ctx.author.id}"


class ReturnGuildOrAuthor:
    def __init__(self,ctx):
        self.ctx = ctx
    def rn(self):
        try:
            return self.ctx.guild.id
        except:
            return self.ctx.author.id


class WelcomeGuildsData:
    def __init__(self) -> None:
        self.filepath = f"{MAINPATH}/WelcomeGuilds.txt"

    async def AddId(self,id):
        with open(self.filepath,"w") as f: 
            f.write(f"{id}\n") #!
    async def ReturnList(self):
        with open(self.filepath,"r") as f:
            return [line for line in f]
    async def RemoveId(self,id):
        # Read file.txt
        with open(self.filepath, 'r') as file:
            text = file.read()


        # Delete text and Write
        with open(self.filepath, 'w') as file:
            # Delete
            new_text = text.replace(f'{id}', '')
            # Write
            file.write(new_text) #!
    