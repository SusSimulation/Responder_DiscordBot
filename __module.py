import asyncio
import datetime
import os
import random
import shutil
import time
from subprocess import call

import discord
import psutil
from discord.ext import commands

# Not the time online, its the start time of the bot.
TIMEONLINE = time.time()

# MAIN VARIABLES
MAINPATH = str(os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/"
with open(f"{MAINPATH}TOKEN.txt", "r") as f:
    RESPONDERTOKEN = f.read()
VERSION = 4.0

# MAIN DISCORD BOT
responder = commands.Bot(command_prefix='$',help_command=None)


ADMINS = [800558571129274450]

COOLGUILDS = [
1012146008341360721,
ADMINS[0]
]

ChannelsInUse = []

Commands = {
    "$help":"Bare bones help command, displays all of the commands, and sometimes more then that. PS; your kinda using it right now...",
    "$ti": "Trust issues game; A game where you ask a question and get multiple fully anonymous anwsers, it will show the statistics of the question and how much percent said 'yes' or 'no'. ( FAN FAVORITE GAME )",
    "$info":"Gives you info about the bot. ( Way better then $help )"
}


### RETURNING OBJECTS ### ------------------------------------------------------------------------------------------------------------------------------
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
        print("-"*(len(self.msg)+2))
        print(f"|{self.msg}|")
        print("-"*(len(self.msg)+2))


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

### TRUST ISSUES GAME CLASS --------------------------------------------------------------------------------------------------------------------
class TrustIssuesGame:
    def __init__(self,msg):
        self.msg = msg
        self.question = None
        self.answers = []
        self.yes = 0
        self.no = 0
        self.players = []
    
    async def MainTable(self):
        if await self.GetPeople() != False:
            if await self.GetQuestion() != False:
                await self.Results()

    
    async def GetPeople(self):
        Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("How many people are playing? ( 10 is the max )",des="To play; react to the thumbs up emoji attached to this message. To start the game react to the flag. You may need to re-react to the reaction. The person who initially started the game wont need to react to the emoji.").rn())
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("🏁")

        try:
            self.players.append(self.msg.author.id)
            await self.msg.channel.send(f"{self.msg.author.name} has joined the game.")
            for _ in range(10):
                reaction, user = await responder.wait_for('reaction_add', timeout = 100,check=lambda reaction,user: reaction.emoji == "👍" and user.id != BOTID and user.id not in self.players and reaction.message.channel.id == self.msg.channel.id or user.id in self.players and reaction.message.channel.id == self.msg.channel.id and reaction.emoji == "🏁" and self.msg.author.id == user.id)
                
                if str(reaction.emoji) == "👍":
                    self.players.append(user.id)

                elif str(reaction.emoji) == "🏁":
                    break

                await self.msg.channel.send(f"{user.name} has joined the game.")
            if len(self.players) <= 0:
                await self.msg.channel.send("No one has joined the game.")
                return False

            await self.msg.channel.send(f"{len(self.players)} people have joined the game.")
            return True
        except asyncio.TimeoutError:
            await self.msg.channel.send("Game timed out, super sadly...")
            return False

    async def GetQuestion(self):
        await self.msg.channel.send(embed=SimpleEmbed("What is your question?",des="Type your question in this channel.").rn())
        try:
            self.q = await responder.wait_for('message',timeout=100,check=lambda message:message.author.id == self.msg.author.id and message.channel.id == self.msg.channel.id and message.content != "")
            self.question = self.q.content
            return True
        except asyncio.TimeoutError:
            return False

    async def Results(self):
        await self.msg.channel.send(embed=SimpleEmbed("Question:",des=self.question).rn())
        for i, player in enumerate(self.players):
            fuser = await responder.fetch_user(player)
            await self.msg.channel.send(embed=SimpleEmbed(f"Turn {i+1}",des=f"Waiting on {fuser.mention}, their turn will be skipped in 30 seconds.").rn())
            await fuser.send(embed= SimpleEmbed("Type 'yes' or 'no'",des=f"Question: {self.question}").rn() )
            def check(m):
                return m.author.id == player and m.author.id != responder.user.id and m.content.lower() in ["no","yes"] and m.channel.id == fuser.dm_channel.id
            try:
                m = await responder.wait_for('message',timeout=30,check=check)
                
                if m.content.lower() == "yes":
                    self.yes += 1

                elif m.content.lower() == "no":
                    self.no += 1
                await fuser.send(embed=SimpleEmbed("Your answer has been received!").rn())
                AddAudit(f"{fuser.name} has answered with {m.content}")

                await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
            except asyncio.TimeoutError:
                await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't awnser in time").rn())
        Stats_Embed = discord.Embed(title="Stats",color=0xdc00ff)
        Stats_Embed.add_field(name="People who said 'yes'",value=self.yes,inline=False)
        Stats_Embed.add_field(name="People who said 'no'",value=self.no,inline=False)
        Stats_Embed.add_field(name="percentage of people who said 'yes'",value=f"{self.yes//(self.yes+self.no)*100}%",inline=False)
        Stats_Embed.add_field(name="percentage of people who said 'no'",value=f"{self.no//(self.yes+self.no)*100}%",inline=False)
        await self.msg.channel.send(embed=Stats_Embed)


