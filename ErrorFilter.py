from __module import *

# remove the usless error message; discord.ext.commands.errors.CommandNotFound
@responder.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed=SimpleEmbed(f"${ctx.command.name} requires argument < {error.param.name} >.").rn())
        return
    raise error