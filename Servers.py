from __module import *

#Server names ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def servers(ctx):
    try:
        if ctx.author.id in ADMINS:
            # Creating an regular embed for the server names.
            Servers_Embed = discord.Embed(title=f"Servers",des=f"{ctx.message.author.mention} is sending the server names...",color=0x00ff00)
            # Iterating through all of the servers.
            for server in responder.guilds:
                Servers_Embed.add_field(name=server.name,value=server.id,inline=True)
            # Sending the embed to the channel.
            await ctx.channel.send(embed=Servers_Embed)
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return