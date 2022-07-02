from __module import * 


# Rebooting the __main__.py file. ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def reboot(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        if ctx.author.id in ADMINS:
            await ctx.channel.send(embed=SimpleEmbed(f"Rebooting...",des=f"{ctx.message.author.mention} is rebooting the bot...").rn())
            call(["python", f"{MAINPATH}__main__.py"])
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        exit()