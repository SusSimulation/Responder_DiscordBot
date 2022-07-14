from decimal import DivisionByZero
from __module import *

# Trust Issues Game ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def ti(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            if ChannelInUse(ctx).rn() == False:
                ChannelsInUse.append(ctx.channel.id)
                await TrustIssuesGame(ctx).MainTable()
            else:
                s = await ctx.channel.send(embed=SimpleEmbed("Sorry!","This channel is already playing a game, wait intill its over.").rn())
                await asyncio.sleep(5)
                await s.delete()
    except DivisionByZero:
        pass
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        if ctx.channel.id in ChannelsInUse:
            ChannelsInUse.remove(ctx.channel.id)
        return
