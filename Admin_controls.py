from __module import *

class AdminControls(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
   
    @commands.command(aliases=["kill"])
    async def quit(self,ctx):
        try:
            AddAudit(ctx=ctx,finished=False)
            if ctx.author.id == ADMINS[0]:
                await ctx.channel.send(embed=SimpleEmbed(f"Quitting...",des=f"{ctx.message.author.mention} is quitting the bot...").rn())
                exit()
            else:
                await ctx.channel.send(embed=SimpleEmbed("You're not a admin!").rn())
        finally:
            AddAudit(ctx=ctx,finished=True)
   
    @commands.command(aliases=["reset","restart"])
    async def reboot(self,ctx):
        try:
            AddAudit(ctx=ctx,finished=False)
            if ctx.author.id in ADMINS:
                await ctx.channel.send(embed=SimpleEmbed(f"Rebooting...",des=f"{ctx.message.author.mention} is rebooting the bot...").rn())
                call(["python", f"{MAINPATH}__main__.py"])
            else:
                await ctx.channel.send(embed=SimpleEmbed("You're not a admin!").rn())
                return
        finally:
            AddAudit(ctx=ctx,finished=True)
            exit()
   
    @commands.command(aliases=["guilds_list","guilds","serverlist","server_list"])
    async def servers(self,ctx):
        await responder.wait_until_ready()
        mdel = []
        mdel.append(ctx.message)
        try:
            if ctx.author.id in ADMINS:
                MainEmbed = SimpleEmbed(f"We are in {len([g for g in responder.guilds])}",des="May not be accurate.").rn()
                for guild in responder.guilds:
                    MainEmbed.add_field(name=guild.name,value=str(guild.member_count),inline=True)
                await responder.wait_until_ready()
                await ctx.channel.send(embed=MainEmbed)
            else:
                NotAdmin = await ctx.channel.send(embed=SimpleEmbed("You're not a admin!").rn())
        except Exception as error:
            ErrorMessage = await ctx.channel.send(f"**An error occured on our side. To report any errors copy and send this to our support server** <<< {error} >>> \n__**Thank you for your cooperation.**__")
            SupportServer = await ctx.channel.send("https://discord.gg/h9sdWTrKDy")
        finally:
            for m in mdel:
                await m.delete()
            return
                




                