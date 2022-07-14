from __module import *

# On boot, we/I do this... ------------------------------------------------------------------------------------------------------------------------------
@responder.event
async def on_ready():
    try:
        print("-"*40)
        print(f"Logged in boy's! {MAINPATH}")
        print(f"Logged in as {responder.user.name} with the id of {responder.user.id}")
        print(f"I am in {len([guild for guild in responder.guilds])} guilds!")
        print("-"*40)
        # setting bots status as lisining to $help & $info
        await responder.change_presence(activity=discord.Game(name=f"$help | $info"))
    finally:
        return