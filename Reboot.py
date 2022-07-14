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
    finally:
        exit()