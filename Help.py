from __module import *

class Help(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    # Help Command ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def help(self,ctx):
        try:
            AddAudit(f"{ctx.author} started Help at {datetime.datetime.now()} in {ctx.channel}")
            # initialize the embed
            Commands_Embed_for_Help_Command = SimpleEmbed("Commands",des=f"{responder.user.name} has been online for {str(datetime.timedelta(seconds=int(round(time.time()-TIMEONLINE))))}.\nRequested by: {ctx.author.mention}\nGames can only be called once at a time in a chat channel ( It can cause errors! )").rn()
            # Add a field for each command
            for i in Commands:
                UpdatedCommands_Embed_for_Help_Command = Commands_Embed_for_Help_Command.add_field(name=f"{i}",value=f"{Commands[i]}",inline=False)
            # Send the embed
            HelpCommandEmbed = await ctx.channel.send(embed=UpdatedCommands_Embed_for_Help_Command)
            # Adding reaction for easy deleting of the embeded message.
            await HelpCommandEmbed.add_reaction("❌")
            try:
                # Waiting for user to react with the ❌ emoji.
                await responder.wait_for("reaction_add",timeout=20,check=lambda reaction,user: reaction.emoji == "❌" and user == ctx.author and HelpCommandEmbed == reaction.message)
                # When user does react with the ❌ emoji, the embeded message will be deleted.
                await HelpCommandEmbed.delete()
            except asyncio.TimeoutError:
                # If the user does not react with the ❌ emoji, the reaction will be removed from the embed.
                await HelpCommandEmbed.remove_reaction("❌",responder.user)
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            return