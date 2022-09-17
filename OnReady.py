from __module import *
from discord.ext import tasks

@tasks.loop(seconds=1800.0)
async def updatepresence():
    """Will loop every 3600 seconds and change the bots presence"""
    total_members = []

    for guild in responder.guilds:
        for u in guild.members:
            total_members.append(u)

    # Number of total members the bot is `serving` in all guilds, without duplicates
    total_members_count = len(total_members)
    choice = [f"{len([guild for guild in responder.guilds])} Servers!",f"{total_members_count} Users!"][random.randint(0,1)]
    await responder.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name=choice))


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