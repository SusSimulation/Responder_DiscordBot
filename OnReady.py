from __module import *
from discord.ext import tasks

@tasks.loop(seconds=1800.0)
async def updatepresence():
    await responder.wait_until_ready()
    choice = f"{len([guild for guild in responder.guilds])} Servers!"
    await responder.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=choice))


# On boot, we/I do this... ------------------------------------------------------------------------------------------------------------------------------
@responder.event
async def on_ready():
    try:
        print("-"*40)
        print(f"Logged in boy's! {MAINPATH}")
        print(f"Logged in as {responder.user.name} with the id of {responder.user.id}")
        print("-"*40)
        await responder.wait_until_ready()
        # Starting the loop
        updatepresence.start()
    finally:
        return