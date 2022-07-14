from __module import *

# Quit the program ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def quit(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        # If the user is in the ADMINS[0] list, then the bot will quit.
        if ctx.author.id == ADMINS[0]:
            # SUper cool embed message sending to the channel.
            await ctx.channel.send(embed=SimpleEmbed(f"Quitting...",des=f"{ctx.message.author.mention} is quitting the bot...").rn())
            exit()
    finally:
        exit()