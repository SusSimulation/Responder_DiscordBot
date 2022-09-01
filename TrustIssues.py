from decimal import DivisionByZero
from __module import *

class TrustIssuesGame(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    # Trust Issues Game ------------------------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def ti(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $ti at {datetime.datetime.now()} in {ctx.channel}")
            if not isinstance(ctx.channel,discord.DMChannel):
                ChannelsInUse.append(ctx.channel.id)
                await TrustIssuesGame(ctx).MainTable()
        except DivisionByZero:
            pass
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            if ctx.channel.id in ChannelsInUse:
                ChannelsInUse.remove(ctx.channel.id)
            return
