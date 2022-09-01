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

    # if the pay load is to big HTTPEXCEPTION
    if error.__class__.__name__ == "HTTPException":
        return

    if error.__class__.__name__ == "CommandInvokeError":
        return
    
    # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
    # Fetch 'me'
    JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
    # Send the error in the dms of JAZZYJAZZ
    await JAZZYJAZZ.send(embed=SimpleEmbed(f"{error}",des=f"({error.__class__.__name__}) Error was raised in {ReturnInfo(ctx).rn()} at { datetime.datetime.now()}").rn())
    # Send the error in the channel
    AddAudit(f"{error} ---- ({error.__class__.__name__}) Error was raised in {ReturnInfo(ctx).rn()} at { datetime.datetime.now()}")
    return