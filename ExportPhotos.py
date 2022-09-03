from __module import *

### Think of the command $hen as a gift?

class PostAndSaves(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    
    @commands.command()
    async def hen(self,ctx):
        try:
            AddAudit(f"{ctx.author} started Hen at {datetime.datetime.now()} in {ctx.channel}")
            if ctx.channel.is_nsfw():
                while True:
                    try:
                        file = random.choice(os.listdir(f"{MAINPATH}HenFiles"))
                        if not file.endswith(".url"):
                            f = await ctx.channel.send(file=discord.File(f"{MAINPATH}HenFiles/{file}"))
                            break
                    except:
                        pass
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            await asyncio.sleep(3600) #after an hour, delete the message
            await f.delete()
            return