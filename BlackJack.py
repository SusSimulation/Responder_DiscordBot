from __module import *

# Black Jack ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def blackjack(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            if ChannelInUse(ctx).rn() == False:
                ChannelsInUse.append(ctx.channel.id)
                Blackjack = BlackjackGame(ctx.message)
                await Blackjack.StartGame()
            else:
                s = await ctx.channel.send(embed=SimpleEmbed("Sorry!","This channel is already playing a game, wait intill its over.").rn())
                await asyncio.sleep(5)
                await s.delete()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())

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
