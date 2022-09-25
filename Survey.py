from __module import *

class Survey(commands.Cog):
    def __init__(self,client) -> None:
        self.results = [[],[],[],[]]
        self.client = client
    @commands.command(aliases=["test","enquête"])
    async def survey(self,ctx):
        pass