from __module import *

# quote command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def quote(ctx):
    try:
        NewQuote = Quote(ctx)
        await NewQuote.Send()
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return
