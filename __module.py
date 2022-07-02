import asyncio
import os
import random
import shutil
from discord.ext import commands
import discord
import time

# MAIN VARIABLES
MAINPATH = str(os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/"
with open(f"{MAINPATH}TOKEN.txt", "r") as f:
    RESPONDERTOKEN = f.read()
BOTID = 978821592668864583
VERSION = 4.0

# MAIN DISCORD BOT
responder = commands.Bot(command_prefix='$',help_command=None)

# Lists
Banned_ids = [

]
ADMINS = [
    800558571129274450, # Jazzyjazz
    839323330297331743, # AMELIA
    879210381661335592
]

COOLGUILDS = [
    973319206714081374
] #992058629517742080

Commands = {
    "$help":"Bare bones help command, displays all of the commands, and sometimes more then that. PS; your kinda using it right now...",
    "$ti": "Trust issues game; A game where you ask a question and get multiple fully anonymous awnsers, it will show the statistics of the question and how much percent said 'yes' or 'no'.",
    "$photo": "Sends a random photo, only works in a few servers.",
    "$add": "Adds a photo to the command; $photo",
    "$blackjack": "A game where you play blackjack, start the game by typing $blackjack then deal yourself in by typing 'deal' to start type; 'start' and then the game starts.",
    "$quote": "As you might think, this will send a random quote.",
    "$8ball": "Fortune telling game, type $8ball and then a question, it will give you a answer.",
    "$rps": "Rock paper scissors game, type $rps and then rock, paper or scissors, it will give you a answer.",
    "$survey": "A survey game, type $survey and then a question, it will give you all of the stats on the survey.",
    "$pp":"Measures your pp.",
    "$info":"Gives you info about the bot. ( Way better then $help )"
}

eightball_answers = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

class SimpleEmbed:
    def __init__(self,t,des=None):
        self.des = des
        self.t = t
    def rn(self):
        if self.des == None:
            return discord.Embed(title=self.t,color=0xdc00ff)
        else:
            return discord.Embed(title=self.t,description=self.des,color=0xdc00ff)

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
            return self.author.id

### TRUST ISSUES GAME CLASS
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
        Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("How many people are playing? ( 10 is the max )",des="To play; react to the thumbs up emoji attached to this message. To start the game react to the flag.").rn())
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("🏁")
        try:
            for _ in range(10):
                reaction, user = await responder.wait_for('reaction_add', timeout = 100,check=lambda reaction,user: reaction.emoji == "👍" and user.id != BOTID and user.id not in self.players and reaction.message.channel.id == self.msg.channel.id or user.id != BOTID and user.id in self.players and reaction.message.channel.id == self.msg.channel.id)
                
                if str(reaction.emoji) == "👍":
                    self.players.append(user.id)
                    await reaction.message.remove_reaction(reaction.emoji,user)

                elif str(reaction.emoji) == "🏁":
                    await reaction.message.remove_reaction(reaction.emoji,user)
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
                return m.author.id == player and m.author.id != BOTID and m.content.lower() in ["no","yes"] and m.channel.id == fuser.dm_channel.id
            try:
                m = await responder.wait_for('message',timeout=30,check=check)
                
                if m.content == "yes":
                    self.yes += 1

                elif m.content == "no":
                    self.no += 1

                await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
            except asyncio.TimeoutError:
                await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't awnser in time").rn())
        Stats_Embed = discord.Embed(title="Stats",color=0xdc00ff)
        Stats_Embed.add_field(name="People who said 'yes'",value=self.yes,inline=False)
        Stats_Embed.add_field(name="People who said 'no'",value=self.no,inline=False)
        Stats_Embed.add_field(name="percentage of people who said 'yes'",value=f"{self.yes/(self.yes+self.no)*100}%",inline=False)
        Stats_Embed.add_field(name="percentage of people who said 'no'",value=f"{self.no/(self.yes+self.no)*100}%",inline=False)
        await self.msg.channel.send(embed=Stats_Embed)

### SEND PHOTO FOR $PHOTO
class PersonalPhotoExport:
    def __init__(self,msg) -> None:
        self.msg = msg

    async def SendRandomPhoto(self):
        try:
            a = await self.msg.channel.send( file=discord.File( f"{MAINPATH}$photo//{random.choice( os.listdir(f'{MAINPATH}$photo' ) )}") )
        finally:
            await asyncio.sleep(3600)
            await a.delete()


### SAVE FOR $PHOTO
class PersonalPhotoImport:
    def __init__(self,msg) -> None:
        try:
            self.msg = msg
            self.name = "12345678910qwertyuiopafghjklzcvbnm_QWERTYUIOPASDFGHJKLZXCVBNM__"
        except Exception as e:
            pass

    async def SavePhoto(self):
        try:
            pspembed = discord.Embed(title="Please Send a photo.", color=0xdc00ff)
            await self.msg.channel.send(embed=pspembed)

            self.file = await responder.wait_for("message",timeout=60,check=lambda msg: msg.author.id != responder.user.id and msg.author.id == self.msg.author.id)
            for attachment in self.file.attachments:
                await attachment.save(attachment.filename)
                self.newname = ''.join(random.sample(self.name,len(self.name)))
                os.rename(f"{MAINPATH}{attachment.filename}",f"{MAINPATH}{self.newname}.png")
                shutil.move(f"{MAINPATH}{self.newname}.png",f"{MAINPATH}$photo")
            siembed = SimpleEmbed(f"Sucessfully imported! Items saved to {MAINPATH}$photo")
            await self.msg.channel.send(embed = siembed.rn())

        except asyncio.TimeoutError:
            pass
        except Exception as e:
            usiembed = discord.Embed(title=f"unsucessfull, did not import.",desciption=f"{e}",color=0xdc00ff)
            await self.msg.channel.send(embed=usiembed.rn())
        finally:
            await asyncio.sleep(10)
            await self.file.delete()

class BlackjackGame:
    def __init__(self,msg):

        self.msg = msg
        self.cards = [2]*4+[3]*4+[4]*4+[5]*4+[6]*4+[7]*4+[8]*4+[9]*4+[10]*4+[10]*4+[10]*4+[10]*4+[1]*4
        self.finished_players = []
        self.decks = []


    async def StartGame(self):
        # Shuffle deck
        random.shuffle(self.cards)

        ## Dealing phase
        # Create decks
        for i in range(20):
            try:
                newembed = discord.Embed(title=f"Blackjack",description=f"Type 'deal' to play, to start early type 'start'.", color=0xdc00ff)
                await self.msg.channel.send(embed=newembed)
                self.dealing_in = await responder.wait_for("message",timeout=25,check=lambda msg: (str(msg.author.id) not in str(self.decks) and msg.channel.id == self.msg.channel.id and msg.author.id != responder.user.id and msg.content.lower() == "deal") or (msg.channel.id == self.msg.channel.id and msg.author.id != responder.user.id and msg.content.lower() == "start" and msg.author.id == self.msg.author.id and str(msg.author.id) in str(self.decks)))
                if self.dealing_in.content.lower() == "start":
                    break
                elif self.dealing_in.content.lower() == "deal":
                    card = random.choice(self.cards)
                    self.cards.remove(card)
                    self.decks.append([self.dealing_in.author.id, card])
                    card = random.choice(self.cards)
                    self.cards.remove(card)
                    self.decks[i].append(card)

                    newembed = discord.Embed(title=f"Cards", color=0xdc00ff)
                    for j,card in enumerate(self.decks[i]):
                        if card == self.dealing_in.author.id:
                            continue
                        newembed.add_field(name=f"{card}",value="___",inline=True)
                    user = await responder.fetch_user(self.dealing_in.author.id)
                    await user.send(embed=newembed)
                    
                    await self.msg.channel.send(f"{user.mention} has been dealt a {card} and ???")
            except asyncio.TimeoutError:
                break
        # Start game
        for j,player_i in enumerate(self.decks):
            while True:
                try:
                    user = await responder.fetch_user(player_i[0])
                    newembed = discord.Embed(title=f"Hit or Stay?",description = f"{user.mention}", color=0xdc00ff)
                    await self.msg.channel.send(embed=newembed)
                    self.hit_or_stay = await responder.wait_for("message",timeout=35,check = lambda msg: msg.channel.id == self.msg.channel.id and msg.author.id == player_i[0] and msg.content.lower() in ["hit","stay"])
                    if self.hit_or_stay.content.lower() == "hit":
                        card = random.choice(self.cards)
                        self.cards.remove(card)
                        self.decks[j].append(card)
                        newembed = discord.Embed(title=f"Cards", color=0xdc00ff)
                        for card in self.decks[j]:
                            if card == self.dealing_in.author.id:
                                continue
                            newembed.add_field(name=f"{card}",value="___",inline=True)
                        await user.send(embed=newembed)
                        await self.msg.channel.send(f"{user.mention} has been dealt a ( {card} )")
                        if sum(self.decks[j][1:]) > 21:
                            await self.msg.channel.send(f"{user.mention} has busted!")
                            break
                    if self.hit_or_stay.content.lower() == "stay":
                        self.finished_players.append(self.decks[j])
                        break
                except asyncio.TimeoutError:
                    break
        # Calculate score
        newembed = discord.Embed(title=f"People:", color=0xdc00ff)
        for player in self.finished_players:
            user = await responder.fetch_user(player[0])
            newembed.add_field(name=f"Sum = {sum(player[1:])}",value=f"{user.mention}",inline=True)
        await self.msg.channel.send(embed=newembed)

class Quote:
    def __init__(self,msg) -> None:
        self.msg = msg
        with open(f"{MAINPATH}q.txt") as quotes:
            self.quote = random.choice(quotes.readlines())
    async def Send(self):
        try:
            self.quote_embed = discord.Embed(title=f"{self.quote}",color=0xdc00ff)
            await self.msg.channel.send(embed=self.quote_embed)
        except:
            await self.msg.channel.send(f"{self.quote}")

class EightBall:
    def __init__(self,msg) -> None:
        self.msg = msg

    async def Send(self):
        await self.msg.channel.send(f"What is your question? ")
        self.question = await responder.wait_for("message",timeout=50,check=lambda msg: msg.author.id != responder.user.id)
        await self.msg.channel.send(f"{random.choice(eightball_answers)}")


class RPS:
    def __init__(self,msg) -> None:
        self.msg = msg
    
    async def UserTurn(self):
        await self.msg.channel.send(f"Rock, Paper, or Scissors?")
        self.user_choice = await responder.wait_for("message",timeout=50,check=lambda msg: msg.author.id != responder.user.id and msg.content.lower() in ["rock","paper","scissors"])
        self.user_choice = self.user_choice.content.lower()
        return self.user_choice

    async def BotTurn(self):
        await self.msg.channel.send(f"Bot's turn!")
        self.bot_choice = random.choice(["rock","paper","scissors"])
        await self.msg.channel.send(f"I chose {self.bot_choice}")
        return self.bot_choice

    async def Winner(self):
        if self.user_choice == "rock" and self.bot_choice == "scissors":
            await self.msg.channel.send(f"You win!")
        elif self.user_choice == "rock" and self.bot_choice == "paper":
            await self.msg.channel.send(f"I win!")
        elif self.user_choice == "paper" and self.bot_choice == "rock":
            await self.msg.channel.send(f"You win!")
        elif self.user_choice == "paper" and self.bot_choice == "scissors":
            await self.msg.channel.send(f"I win!")
        elif self.user_choice == "scissors" and self.bot_choice == "paper":
            await self.msg.channel.send(f"You win!")
        elif self.user_choice == "scissors" and self.bot_choice == "rock":
            await self.msg.channel.send(f"I win!")
        elif self.user_choice == self.bot_choice:
            await self.msg.channel.send(f"It's a tie!")

class Survey:
    def __init__(self,msg) -> None:
        self.msg = msg
        self.already_awsnered = []
        self.awnsers = []
        self.question = None
    
    async def Question(self):
        self.whatisyourquestionembed = discord.Embed(title="What is your question?",description="Type your question in this question.",color=0xdc00ff)
        self.e = await self.msg.channel.send(embed=self.whatisyourquestionembed)
        self.am = await responder.wait_for("message",timeout=50,check=lambda msg: msg.author.id != responder.user.id and msg.author.id == self.msg.author.id)

    async def Answer(self):
        await self.am.delete()
        await self.e.delete()
        try:
            while True:
                self.whatisyourawnserembed = discord.Embed(title=f"{self.am.content}",description=f"Type your answer in this channel. yes or no? ({len(self.awnsers)} awnsers so far...) Survey will end after 500 seconds.",color=0xdc00ff)
                self.e = await self.msg.channel.send(embed=self.whatisyourawnserembed)
                self.answer = await responder.wait_for("message",timeout=500,check=lambda msg: msg.author.id != responder.user.id and msg.content.lower() in ["yes","no"] and msg.author.id not in self.already_awsnered)
                self.already_awsnered.append(self.answer.author.id)
                self.awnsers.append(self.answer.content.lower())
                await self.answer.delete()
                await self.e.delete()
        except asyncio.TimeoutError:
            return self.answer

    async def Stats(self):
        self.agree = self.awnsers.count("yes")
        self.disagree = self.awnsers.count("no")
        if self.agree != 0 or self.disagree != 0:
            self.total = self.agree + self.disagree
            self.agree_percent = round(self.agree/self.total*100,2)
            self.disagree_percent = round(self.disagree/self.total*100,2)
            self.stats_embed = discord.Embed(title=f"Survey Results",color=0xdc00ff)
            self.stats_embed.add_field(name="Agree",value=f"{self.agree} ({self.agree_percent}%)",inline=False)
            self.stats_embed.add_field(name="Disagree",value=f"{self.disagree} ({self.disagree_percent}%)",inline=False)
            self.stats_embed.add_field(name="Total",value=f"{self.total}",inline=False)
            await self.msg.channel.send(embed=self.stats_embed)

class PenisMeasurer:
    def __init__(self,msg) -> None:
        self.msg = msg
        self.l = random.randint(1,10)
        if self.msg.author.id in ADMINS:
            self.l = random.randint(10,20)
    async def Send(self):
        self.ppsizeembed = discord.Embed(title=f"{self.msg.author}'s penis size",description="8{}D".format("="*self.l),color=0xdc00ff)
        await self.msg.channel.send(embed=self.ppsizeembed)

class MusicPlayer:
    def __init__(self,msg):
        print("yes")
        self.msg = msg
    
    async def Join(self):
        voice_channel = self.msg.message.author.voice.channel
        self.channel = None
        if voice_channel != None:
            self.channel = voice_channel.name
            self.vc = await voice_channel.connect()
            # play music

