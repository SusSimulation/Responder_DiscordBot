from __module import *

# remove the usless error message; discord.ext.commands.errors.CommandNotFound
@responder.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
        
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed=SimpleEmbed(f"${ctx.command.name} requires argument < {error.param.name} >.").rn())
        return

    if isinstance(error, discord.errors.NotFound):
        return

    if isinstance(error, discord.errors.Forbidden):
        await ctx.channel.send(embed=SimpleEmbed("Unfortunately, I do not have the permission to do what you asked. MissingPermissions"))
        return

    # if the pay load is to big HTTPEXCEPTION

    if error.__class__.__name__ == "CommandInvokeError":
        return
    if error.__class__.__name__ == "MissingPermissions":
        await ctx.channel.send(embed=SimpleEmbed("Unfortunately, I do not have the permission to do what you asked. MissingPermissions"))
        return
    
    if error.__class__.__name__ == "BadArgument":
        await ctx.channel.send(embed=SimpleEmbed(f"Bad argument!").rn())
        return
    
    # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
    # Fetch 'me'
    JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
    # Send the error in the dms of JAZZYJAZZ
    await JAZZYJAZZ.send(embed=SimpleEmbed(f"{error}",des=f"({error.__class__.__name__}) Error was raised in {ReturnInfo(ctx).rn()} at { datetime.datetime.now()}").rn())
    # Send the error in the channel
    return