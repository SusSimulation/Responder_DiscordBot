from __module import *

# Sending all of the .py files in the folder to the channel. ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def files(ctx):
    try:
        # if not a dm channel, but a server channel
        if not isinstance(ctx.channel, discord.DMChannel):
            # Delete the message to reduce spam
            await ctx.message.delete()
    except discord.errors.NotFound:
        pass
    # If the user is in the ADMINS[0] list, then the bot will quit.
    if ctx.author.id in ADMINS:
        # SUper cool embed message sending to the channel.
        await ctx.channels.send(embed=SimpleEmbed(f"Sending files...",des=f"{ctx.message.author.mention} is sending files...").rn())
        # Sending all of the .py files in the folder to the channel.
        for file in os.listdir(MAINPATH):
            try:
                if file.endswith(".py"):
                    await ctx.channel.send(file=discord.File(f'{file}'))
            except IsADirectoryError:
                pass