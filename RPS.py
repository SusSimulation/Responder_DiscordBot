from __module import *

# rock paper scissors ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def rps(ctx):
    try:
        NewRPS = RPS(ctx)
        await NewRPS.UserTurn()
        await NewRPS.BotTurn()
        await NewRPS.Winner()
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return