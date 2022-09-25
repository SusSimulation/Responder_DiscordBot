from __module import *

class PurgeChannel(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.command(aliases= ['purge','delete',"supprimer"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=0):
        try:
            await ctx.channel.purge(limit=amount+1)
        except:
            if French(ctx).rn() == True:
                await ctx.channel.send("Numéro non valide.")
            else:
                await ctx.channel.send("Invalid number.")
        finally:
            if French(ctx).rn() == True:
                a = await ctx.channel.send(embed=SimpleEmbed(f"Fin!").rn())
            else:
                a = await ctx.channel.send(embed=SimpleEmbed(f"Done!").rn())
            await asyncio.sleep(10)
            await a.delete()