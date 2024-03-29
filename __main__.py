### Before you read this, I want to apologize for my grammer, I am typing fast and have a lot of lines to tag.
import ErrorFilter # Filters some of the frequent errors.
import OnReady # Displays when is ready to use.
from __module import * # Literally everything important, can't run without this.
from Admin_controls import AdminControls # Admin Controls such as, reboot.
from Help import Help # Help Command, displays all of the commands.
from Info import Info # Gives a lot of info on the bot.
from TrustIssues import TrustIssuesGame # The main game, includes $ti and $tic.
from Clear import PurgeChannel
from Moderation import Moderation

if __name__ == "__main__":
    # try these lines so just in case if it fails, before it dies it will print a message to let us know.
    try: 
        # all of the COGS; I thought it would be easier for me to put them in a list.
        COGS = [TrustIssuesGame, AdminControls, Info, Help, PurgeChannel, Moderation]
        # Iterate through all of the COGS.
        for c in COGS: 
            # adding the cog
            responder.add_cog(c(responder))
        # DOnt know what this does but we need it to run the bot. I am guessing it give the bot a identity.
        responder.run(RESPONDERTOKEN)
    # if the code fails
    except Exception as e:
        # print what happend and the error
        print(f"Error on boot: {e.__class__.__name__}: {e}")
        # and then we completly kill the bot, just so we stil dont have the code running.
        quit()
