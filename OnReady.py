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
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised while logging in."))
        exit()
    finally:
        return