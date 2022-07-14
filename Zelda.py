from numpy import isin
from __module import *

@responder.command()
async def zeldass(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            if ctx.channel.is_nsfw():
                file = random.choice(os.listdir(f"{MAINPATH}ZeldaFiles"))
                f = await ctx.channel.send(file=discord.File(f"{MAINPATH}ZeldaFiles/{file}"))
            else:
                await ctx.channel.send("This is not a NSFW channel.")
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        await asyncio.sleep(3600)
        await f.delete()
        return