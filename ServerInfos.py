from __module import *

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["infoguilde"])
    async def serverinfo(self, ctx):
        try:
            embed = discord.Embed(title=f"{ctx.guild.name}'s info", description="Here's what I could find.", color=0x00ff00)
            embed.add_field(name="Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=True)
            embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
            embed.add_field(name="Emojis", value=len(ctx.guild.emojis), inline=True)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        finally:
            try:
                await ctx.message.delete()
            except:
                pass

    @commands.command(aliases=["infotexte"])
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        try:
            if channel is None:
                channel = ctx.channel
            embed = discord.Embed(title=f"{channel.name}'s info", description="Here's what I could find.", color=0x00ff00)
            embed.add_field(name="Name", value=channel.name, inline=True)
            embed.add_field(name="ID", value=channel.id, inline=True)
            embed.add_field(name="Position", value=channel.position, inline=True)
            embed.add_field(name="Topic", value=channel.topic, inline=True)
            embed.add_field(name="NSFW", value=channel.nsfw, inline=True)
            embed.add_field(name="Category", value=channel.category, inline=True)
            embed.add_field(name="Type", value=channel.type, inline=True)
            embed.add_field(name="Created at", value=channel.created_at, inline=True)
            embed.set_thumbnail(url=channel.guild.icon_url)
            await ctx.send(embed=embed)
        finally:
            try:
                await ctx.message.delete()
            except:
                pass