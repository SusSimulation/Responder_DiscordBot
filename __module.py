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

VERSION = 5.0

intents = discord.Intents.default()
responder = commands.Bot(command_prefix='$',help_command=None,intents=intents)

ADMINS = [800558571129274450,879210381661335592]

ChannelsInUse = []
    

Commands = {
    "$trustissues" : "Main game! Get fully anonymous answers from ANY question in the world! Your imagination is your limit.",
    "$help" : "Bare bones help command and display the commands, and sometimes more. PS; you're kinda using it right now...",
    "$clear":"$clear (amount wanting to clear), command that will delete messages.",
    "$change_language":"Swaps language between English and French."
}
CommandsFR = {
    "$trustissues" : "Jeu principal ! Obtenez des réponses totalement anonymes à N'IMPORTE QUELLE question dans le monde ! Votre imagination est votre limite",
    "$aide" : "Une commande d'aide basique qui affiche les commandes, et parfois plus. PS ; vous êtes en train de l'utiliser en ce moment...",
    "$supprimer" : "$clear (montant à effacer), commande qui effacera les messages",
    "$changerlangue" : "Change la langue entre l'anglais et le français."
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
    def __init__(self,ctx,finished=None):
        self.ctx = ctx
        self.finished = finished
        self.Print()
    def Print(self):
        self.msg = f' {self.ctx.author}/{self.ctx.author.id} typed [{self.ctx.message.content}] in {ReturnInfo(self.ctx).rn()} channel = {self.ctx.channel} at {datetime.datetime.now()} :: Finished = {self.finished}'
        print(f">>> {self.msg}")

# LANGUAGES ---------
class French:
    def __init__(self,ctx):
        self.ctx = ctx
    def rn(self):
        with open(f"{MAINPATH}//Francais.txt","r") as f:
            if str(self.ctx.author.id) in f.read():
                return True
            else:
                return False

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
    
on_cooldown = {}  # A dictionary mapping user IDs to cooldown ends


def cooldowns(seconds):
    def predicate(context):
        if (cooldown_end := on_cooldown.get(context.author.id)) is None or cooldown_end < datetime.datetime.now():  # If there's no cooldown or it's over
            if context.valid and context.invoked_with in (*context.command.aliases, context.command.name):  # If the command is being run as itself (not by help, which runs checks and would end up creating more cooldowns if this didn't exist)
                on_cooldown[context.author.id] = datetime.datetime.now() + datetime.timedelta(seconds=seconds)  # Add the datetime of the cooldown's end to the dictionary
            return True  # And allow the command to run
        else:
            raise commands.CommandOnCooldown(commands.BucketType.user, (cooldown_end - datetime.datetime.now()).seconds)  # Otherwise, raise the cooldown error to say the command is on cooldown

    return commands.check(predicate)