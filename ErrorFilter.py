from __module import *

# remove the usless error message; discord.ext.commands.errors.CommandNotFound
@responder.event
async def on_command_error(ctx, error):
    await responder.wait_until_ready()
    if isinstance(error, commands.CommandNotFound):
        return
        
    if isinstance(error, commands.MissingRequiredArgument):
        if French(ctx).rn() == True:
            await ctx.channel.send(embed=SimpleEmbed(f"${ctx.command.name} besoins l'argument < {error.param.name} >.").rn())
        return

    if isinstance(error, discord.errors.NotFound):
        return

    # if the pay load is to big HTTPEXCEPTION

    if error.__class__.__name__ == "CommandInvokeError":
        return
    if isinstance(error, commands.CommandOnCooldown):
        if French(ctx).rn() == True:
            await ctx.author.send(f"{ctx.message.content} est sur le cooldown, vous pouvez l'utiliser en {round(error.retry_after, 4)} secondes.")
        else:
            await ctx.author.send(f"{ctx.message.content} is on cooldown, you can use the command in {round(error.retry_after, 4)} seconds.")
        return
    if error.__class__.__name__ == "MissingPermissions":
        if French(ctx).rn() == True:
            await ctx.channel.send(embed=SimpleEmbed("Malheureusement, vous ou moi n'avons pas la permission de faire ce que vous avez demandé. MissingPermissions").rn())
        else:
            await ctx.channel.send(embed=SimpleEmbed("Unfortunately, I or you do not have the permission to do what you asked. MissingPermissions").rn())
        return
    
    if error.__class__.__name__ == "BadArgument":
        if French(ctx).rn() == True:
            await ctx.channel.send(embed=SimpleEmbed(f"Mauvais argument!").rn())
        else:
            await ctx.channel.send(embed=SimpleEmbed(f"Bad argument!").rn())
        return
    
    # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
    # Fetch 'me'
    JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
    # Send the error in the dms of JAZZYJAZZ
    await JAZZYJAZZ.send(embed=SimpleEmbed(f"{error}",des=f"({error.__class__.__name__}) Error was raised in {ReturnInfo(ctx).rn()} at { datetime.datetime.now()}").rn())
    # Send the error in the channel
    return