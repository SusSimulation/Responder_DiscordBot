from __module import *

class PurgeChannel(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.command(aliases= ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=0):
        try:
            await ctx.channel.purge(limit=amount+1)
        except:
            await ctx.channel.send("Invaild number.")
        finally:
            a = await ctx.channel.send(embed=SimpleEmbed(f"Done!").rn())
            await asyncio.sleep(10)
            await a.delete()