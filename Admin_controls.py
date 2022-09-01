from __module import *

class AdminControls(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    # Sending all of the .py files in the folder to the channel. ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def files(self,ctx):
        try:
            try:
                AddAudit(f"{ctx.author} started Files at {datetime.datetime.now()} in {ctx.channel}")
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            # If the user is in the ADMINS list
            if ctx.author.id in ADMINS:
                # SUper cool embed message sending to the channel.
                await ctx.channel.send(embed=SimpleEmbed(f"Sending files...",des=f"{ctx.author.mention} is sending files...").rn())
                # Sending all of the .py files in the folder to the channel.
                for file in os.listdir(MAINPATH):
                    try:
                        if file.endswith(".py"):
                            await ctx.channel.send(file=discord.File(f'{file}'))
                    except IsADirectoryError:
                        pass
        finally:
            await ctx.channel.send("Done!")

    # Quit the program ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def quit(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $quit at {datetime.datetime.now()} in {ctx.channel}")
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

    # Rebooting the __main__.py file. ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def reboot(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $reboot at {datetime.datetime.now()} in {ctx.channel}")
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

    #Server names ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def servers(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $servers at {datetime.datetime.now()} in {ctx.channel}")
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