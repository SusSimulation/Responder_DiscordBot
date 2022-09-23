from __module import *

### Think of the command $hen as a gift?

class PostAndSaves(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    
    @commands.command()
    async def hen(self,ctx):
        try:
            AddAudit(ctx=ctx,finished=False)
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
                await ctx.message.delete()
            except:
                pass
            return