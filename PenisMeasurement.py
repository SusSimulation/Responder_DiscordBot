from __module import *

# Penis measurer ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def pp(ctx):
    try:
        NewPP = PenisMeasurer(ctx)
        await NewPP.Send()
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return
