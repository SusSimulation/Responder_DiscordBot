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

intents = discord.Intents().all()
# MAIN DISCORD BOT
responder = commands.Bot(command_prefix='$',help_command=None,intents=intents)

ADMINS = [800558571129274450,879210381661335592]

COOLGUILDS = [
1012146008341360721
]

ChannelsInUse = []

Commands = {
    "$help" : "Bare bones help command and display the commands, and sometimes more. PS; you're kinda using it right now...",
    "$ti" : "(PS: The difference in $ti and $tic is that $ti only allows 'yes' or no answers, comparing to $tic it allows all types of answers) Trust issues is a game designed for developing trust issues in your fellow friends. Start off by typing a custom question, then watch the bot count all of the responses and let everyone know what they said without knowing who said it.",
    "$tic" : 'Trust issues is a game designed for developing trust issues in your fellow friends. Start off by typing a custom question, then watch the bot count all of the responses and let everyone know what they said without knowing who said it.',
    "$myid" : "Ever forget your ID?",
    "$serverinfo" : "Info on the server.",
    "$channelinfo" : "Info on the current channel",
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
class TrustIssuesGameC:
    def __init__(self,msg):
        self.msg = msg
        self.question = None
        self.answers = []
        self.yes = 0
        self.no = 0
        self.players = []
        self.delmsg = []
    
    async def MainTable(self):
        if await self.GetPeople() != False:
            if await self.GetQuestion() != False:
                await self.Results()
        

    async def GetPeople(self):
        Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("How many people are playing? ( 10 is the max )",des="To play, react to the thumbs-up emoji attached to this message. To start the game, react to the flag. You may need to re-react to the reaction. The person who initially started the game won't need to react to the emoji.").rn())
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("🏁")

        try:
            self.players.append(self.msg.author.id)
            starterjoined = await self.msg.channel.send(f"{self.msg.author.name} started and joined the game.")
            self.delmsg.append(starterjoined)
            for _ in range(10):
                reaction, user = await responder.wait_for('reaction_add', timeout = 100,check=lambda reaction,user: reaction.emoji == "👍" and user.id != responder.user.id and user.id not in self.players and reaction.message.channel.id == self.msg.channel.id or user.id in self.players and reaction.message.channel.id == self.msg.channel.id and reaction.emoji == "🏁" and self.msg.author.id == user.id)
                
                if str(reaction.emoji) == "👍":
                    self.players.append(user.id)

                elif str(reaction.emoji) == "🏁":
                    break

                joinedthegamemsg = await self.msg.channel.send(f"{user.name} joined.")
                self.delmsg.append(joinedthegamemsg)
            if len(self.players) <= 0:
                await self.msg.channel.send("No one has joined the game.")
                return False

            self.playerjoined = await self.msg.channel.send(f"{len(self.players)} people have joined the game.")
            return True
        except asyncio.TimeoutError:
            await self.msg.channel.send("Game timed out, super sadly...")
            return False
        

    async def GetQuestion(self):
        self.questionembed = await self.msg.channel.send(embed=SimpleEmbed("What is your question?",des="Type your question in this text channel.").rn())
        self.delmsg.append(self.questionembed)
        try:
            self.q = await responder.wait_for('message',timeout=100,check=lambda message:message.author.id == self.msg.author.id and message.channel.id == self.msg.channel.id and message.content != "")
            self.question = self.q.content
            self.delmsg.append(self.q)
            self.delmsg.append(self.playerjoined)
            return True
        except asyncio.TimeoutError:
            return False

    async def Results(self):
        questionembedtwo = await self.msg.channel.send(embed=SimpleEmbed("Question:",des=self.question).rn())
        self.delmsg.append(questionembedtwo)
        for i, player in enumerate(self.players):
            fuser = await responder.fetch_user(player)
            turndisplayembed = await self.msg.channel.send(embed=SimpleEmbed(f"Turn {i+1}",des=f"Waiting on {fuser.mention}, their turn will be skipped in 30 seconds.").rn())
            self.delmsg.append(turndisplayembed)
            await fuser.send(embed= SimpleEmbed("Type your answer cooresponding to the question below.",des=f"Question: {self.question}").rn() )
            def check(m):
                return m.author.id == player and m.author.id != responder.user.id and m.channel.id == fuser.dm_channel.id
            try:
                m = await responder.wait_for('message',timeout=30,check=check)
                
                self.answers.append(m.content)
                
                await fuser.send(embed=SimpleEmbed("Your answer has been received!").rn())

                hasansweredembed = await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
                self.delmsg.append(hasansweredembed)
            except asyncio.TimeoutError:
                hasnotansweredembed =await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't answer in time").rn())
                self.delmsg.append(hasnotansweredembed)
        if not len(self.answers) == 0:
            Stats_Embed = discord.Embed(title="Stats",description=f"Question = {self.question}",color=0xff0000)
            for response in self.answers:
                Stats_Embed.add_field(name="Anonymous",value=response,inline=True)
            await self.msg.channel.send(embed=Stats_Embed)
        else:
            Stats_Embed = discord.Embed(title="No one finished the game.",description=f"question = {self.question}",color=0xff0000)
            await asyncio.sleep(10)
        for l in self.delmsg:
            await l.delete()


class TrustIssuesGameC_OLD_ONE:
    def __init__(self,msg):
        self.msg = msg
        self.question = None
        self.answers = []
        self.yes = 0
        self.no = 0
        self.players = []
        self.delmsg = []
    
    async def MainTable(self):
        if await self.GetPeople() != False:
            if await self.GetQuestion() != False:
                await self.Results()
        

    
    async def GetPeople(self):
        Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("How many people are playing? ( 10 is the max )",des="To play, react to the thumbs-up emoji attached to this message. To start the game, react to the flag. You may need to re-react to the reaction. The person who initially started the game won't need to react to the emoji.").rn())
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("🏁")

        try:
            self.players.append(self.msg.author.id)
            starterjoined = await self.msg.channel.send(f"{self.msg.author.name} started and joined the game.")
            self.delmsg.append(starterjoined)
            for _ in range(10):
                reaction, user = await responder.wait_for('reaction_add', timeout = 100,check=lambda reaction,user: reaction.emoji == "👍" and user.id != responder.user.id and user.id not in self.players and reaction.message.channel.id == self.msg.channel.id or user.id in self.players and reaction.message.channel.id == self.msg.channel.id and reaction.emoji == "🏁" and self.msg.author.id == user.id)
                
                if str(reaction.emoji) == "👍":
                    self.players.append(user.id)

                elif str(reaction.emoji) == "🏁":
                    break

                joinedthegamemsg = await self.msg.channel.send(f"{user.name} joined.")
                self.delmsg.append(joinedthegamemsg)
            if len(self.players) <= 0:
                await self.msg.channel.send("No one has joined the game.")
                return False

            self.playerjoined = await self.msg.channel.send(f"{len(self.players)} people have joined the game.")
            return True
        except asyncio.TimeoutError:
            await self.msg.channel.send("Game timed out, super sadly...")
            return False
        

    async def GetQuestion(self):
        self.questionembed = await self.msg.channel.send(embed=SimpleEmbed("What is your question?",des="Type your question in this text channel.").rn())
        self.delmsg.append(self.questionembed)
        try:
            self.q = await responder.wait_for('message',timeout=100,check=lambda message:message.author.id == self.msg.author.id and message.channel.id == self.msg.channel.id and message.content != "")
            self.question = self.q.content
            self.delmsg.append(self.q)
            self.delmsg.append(self.playerjoined)
            return True
        except asyncio.TimeoutError:
            return False

    async def Results(self):
        questionembedtwo = await self.msg.channel.send(embed=SimpleEmbed("Question:",des=self.question).rn())
        self.delmsg.append(questionembedtwo)
        for i, player in enumerate(self.players):
            fuser = await responder.fetch_user(player)
            turndisplayembed = await self.msg.channel.send(embed=SimpleEmbed(f"Turn {i+1}",des=f"Waiting on {fuser.mention}, their turn will be skipped in 30 seconds.").rn())
            self.delmsg.append(turndisplayembed)
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

                hasansweredembed = await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
                self.delmsg.append(hasansweredembed)
            except asyncio.TimeoutError:
                hasnotansweredembed =await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't answer in time").rn())
                self.delmsg.append(hasnotansweredembed)
        if not self.yes+self.no == 0:
            Stats_Embed = discord.Embed(title="Stats",description=f"Question = {self.question}",color=0xff0000)
            Stats_Embed.add_field(name=f"{self.yes//(self.yes+self.no)*100}% said 'yes'",value=f"{self.yes}",inline=True)
            Stats_Embed.add_field(name=f"{self.no//(self.yes+self.no)*100}% said 'no'",value=f"{self.no} ",inline=True)
            await self.msg.channel.send(embed=Stats_Embed)
        else:
            Stats_Embed = discord.Embed(title="No one finished the game.",description=f"question = {self.question}",color=0xff0000)
            await asyncio.sleep(10)
        for l in self.delmsg:
            await l.delete()


