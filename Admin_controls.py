from __module import *

class AdminControls(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
   
    @commands.command(aliases=["kill"])
    async def quit(self,ctx):
        try:
            if ctx.author.id == ADMINS[0]:
                await ctx.channel.send(embed=SimpleEmbed(f"Quitting...",des=f"{ctx.message.author.mention} is quitting the bot...").rn())
                exit()
            else:
                await ctx.channel.send(embed=SimpleEmbed("You're not a admin!").rn())
        finally:
            return
   
    @commands.command(aliases=["reset","restart"])
    async def reboot(self,ctx):
        try:
            if ctx.author.id in ADMINS:
                await ctx.channel.send(embed=SimpleEmbed(f"Rebooting...",des=f"{ctx.message.author.mention} is rebooting the bot...").rn())
                call(["python", f"{MAINPATH}__main__.py"])
            else:
                await ctx.channel.send(embed=SimpleEmbed("You're not a admin!").rn())
                return
        finally:
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

    @commands.command(aliases=["usersearch","find"])
    async def searchuser(self,ctx,userid):
        try:
            if ctx.author.id in ADMINS:
                for guild in responder.guilds:
                    for member in guild.members:
                        if member.id == int(userid):
                            await ctx.channel.send(f"User found! name = {member}, id = {member.id}, guild = {guild}, guild members = {guild.member_count}, guild id = {guild.id}")
                            return
                await ctx.channel.send("User not found.")
            else:
                pass
        except:
            pass
        finally:
            await ctx.message.delete()

    @commands.command(aliases=["most_members"])
    async def biggest_server(self,ctx):
        try:
            if ctx.author.id in ADMINS:
                guild_member_count = []
                for guild in responder.guilds:
                    guild_member_count.append([guild.member_count,guild.name])
                guild_member_count.sort(reverse=True)
                await ctx.channel.send(f"the top four server's are:\n{guild_member_count[0]}\n{guild_member_count[1]}\n{guild_member_count[2]}\n{guild_member_count[3]}")
            else:
                return
        finally:
            await ctx.message.delete()



                