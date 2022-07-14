from __module import *

@responder.command()
async def hen(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            if ctx.channel.is_nsfw():
                file = random.choice(os.listdir(f"{MAINPATH}HenFiles"))
                f = await ctx.channel.send(file=discord.File(f"{MAINPATH}HenFiles/{file}"))
            else:
                await ctx.channel.send("This is not a NSFW channel.")
        elif isinstance(ctx.channel,discord.DMChannel) and ctx.author.id == 800558571129274450:
            file = random.choice(os.listdir(f"{MAINPATH}HenFiles"))
            await ctx.channel.send(file=discord.File(f"{MAINPATH}HenFiles/{file}"))
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        await asyncio.sleep(3600) #after an hour, delete the message
        await f.delete()
        return