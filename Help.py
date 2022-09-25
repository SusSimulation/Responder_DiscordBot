from ast import alias
from __module import *

class Help(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    # Help Command ------------------------------------------------------------------------------------------------------------------------------
    @commands.command(aliases=["aide"])
    @cooldowns(10)
    async def help(self,ctx):
        try:
            # initialize the embed
            Commands_Embed_for_Help_Command = SimpleEmbed("Commands",des=f"{ctx.author.mention}").rn()
            # Add a field for each command
            if French(ctx).rn() == False:
                for i in Commands:
                    UpdatedCommands_Embed_for_Help_Command = Commands_Embed_for_Help_Command.add_field(name=f"{i}",value=f"{Commands[i]}",inline=False)
            else:
                for i in CommandsFR:
                    UpdatedCommands_Embed_for_Help_Command = Commands_Embed_for_Help_Command.add_field(name=f"{i}",value=f"{CommandsFR[i]}",inline=False)
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
                await ctx.message.delete()
            except:
                pass
            return