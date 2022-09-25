from __module import *

class StupidExtraStuff(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        try:
            self.PongMessage = await ctx.channel.send(embed=SimpleEmbed(f"Pong! {self.client.latency * 1000}ms").rn())
        finally:
            await ctx.message.delete()
            await asyncio.sleep(10)
            await self.PongMessage.delete()

    @commands.command(aliases=["id"])
    async def myid(self,ctx):
        try:
            self.UserIdMessage = await ctx.channel.send(embed=SimpleEmbed(f"{ctx.author.name}'s Id: {ctx.author.id}").rn())
        except:
            if French(ctx).rn() == True:
                await ctx.channel.send(f"Erreur.")
            else:
                await ctx.channel.send(f"Error.")
        finally:
            await ctx.message.delete()
            await asyncio.sleep(10)
            await self.UserIdMessage.delete()