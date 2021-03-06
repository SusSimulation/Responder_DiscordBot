from __module import *

# Info about server and bot ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def info(ctx):
    try:
        embed = discord.Embed(title=f"Info",description=f"Requested by: {ctx.author.mention}\nIf you find any bugs, please report them and Jazzyjazz404#8538 will give you admin access.", color=0xdc00ff)
        embed.add_field(name="Current Time",value=f"{datetime.datetime.now()}",inline=False)
        embed.add_field(name="CPU Usage",value=f"{psutil.cpu_percent()}%",inline=False)
        embed.add_field(name="RAM Usage",value=f"{psutil.virtual_memory().percent}%",inline=False)
        embed.add_field(name="Disk Usage",value=f"{psutil.disk_usage('/').percent}%",inline=False)
        embed.add_field(name="psutil.users",value=f"{len(psutil.users())}",inline=False)
        embed.add_field(name="Ping",value=f"{round(responder.latency * 1000)}ms",inline=False)
        total, used, free = shutil.disk_usage("/")
        embed.add_field(name="Total Storage",value=f"Total: %d GiB" % (total // (2**30)))
        embed.add_field(name="Used Storage",value=f"Used: %d GiB" % (used // (2**30)))
        embed.add_field(name="Free Storage",value=f"Free: %d GiB" % (free // (2**30)))
        embed.add_field(name="Uptime",value=str(datetime.timedelta(seconds=int(round(time.time()-TIMEONLINE)))),inline=False)
        embed.add_field(name="Version",value=f"{VERSION}",inline=False)
        embed.add_field(name="Guilds",value=f"{len([guild for guild in responder.guilds])}",inline=False)
        e = await ctx.channel.send(embed=embed)
        await e.add_reaction("❌")
        try:
            # Waiting for user to react with the ❌ emoji.
            await responder.wait_for("reaction_add",timeout=20,check=lambda reaction,user: reaction.emoji == "❌" and user == ctx.author and e == reaction.message)
            # When user does react with the ❌ emoji, the embeded message will be deleted.
            try:
                await e.delete()
            except discord.errors.NotFound:
                pass
        except asyncio.TimeoutError:
            try:
                # If the user does not react with the ❌ emoji, the reaction will be removed from the embed.
                await e.remove_reaction("❌",responder.user)
            except discord.errors.NotFound:
                pass
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return