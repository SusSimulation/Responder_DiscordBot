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

    @commands.command()
    async def myid(self,ctx):
        try:
            self.UserIdMessage = await ctx.channel.send(embed=SimpleEmbed(f"{ctx.author.name}'s Id: {ctx.author.id}").rn())
        except:
            await ctx.channel.send(f"Error while sending id of user; {ctx.author}, Sorry for the inconvenience here is your id: {ctx.author.id}")
        finally:
            await ctx.message.delete()
            await asyncio.sleep(10)
            await self.UserIdMessage.delete()