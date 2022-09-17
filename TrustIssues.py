from __module import *

class TrustIssuesGameC:
    def __init__(self,msg):
        self.msg = msg
        self.question = None
        self.answers = []
        self.yes = 0
        self.no = 0
        self.players = []
        self.delmsg = []
        self.startdelmsg = []
        self.time = 90  
        self.newanswers = []  
    async def MainTable(self):
        if await self.GetPeople() != False:
            if await self.GetQuestion() != False:
                await self.Results()
        for l in self.delmsg:
            try:
                await l.delete()
            except:
                pass
        return
        

    async def GetPeople(self):

        customtimeembed = await self.msg.channel.send(embed=SimpleEmbed("🕐 = add 1 minute ⌛ = add 1 hour 📅 = add 1 day",des="Click the ❌ to reset time ✅ to continue the game!").rn())
        await customtimeembed.add_reaction("🕐")
        await customtimeembed.add_reaction("⌛")
        await customtimeembed.add_reaction("📅")
        await customtimeembed.add_reaction("❌")
        await customtimeembed.add_reaction("✅")
        self.startdelmsg.append(customtimeembed)
        try:
            while True:
                reaction, user = await responder.wait_for('reaction_add', timeout = 100,check=lambda reaction,user: reaction.emoji in ["🕐","⌛","📅","❌","✅"] and user.id == self.msg.author.id and reaction.message.id == customtimeembed.id)
            
                if str(reaction.emoji) == "🕐":
                    self.time += 60
                    minembed = await self.msg.channel.send(embed=SimpleEmbed("1 minute was added!",des=f"Time = {self.time//(60)} minutes").rn())
                    self.startdelmsg.append(minembed)
                elif str(reaction.emoji) == "⌛":
                    self.time += 3600
                    hourembed = await self.msg.channel.send(embed=SimpleEmbed("1 hour was added!",des=f"Time = {self.time//(60*60)} hours").rn())
                    self.startdelmsg.append(hourembed)
                elif str(reaction.emoji) == "📅":
                    self.time += 86400
                    dayembed = await self.msg.channel.send(embed=SimpleEmbed("1 day was added!",des=f"Time = {self.time//(60*60*24)} days").rn())
                    self.startdelmsg.append(dayembed)
                elif str(reaction.emoji) == "✅":
                    break
                elif str(reaction.emoji) == "❌":
                    self.time = 90
                    timeresetembed = await self.msg.channel.send(embed=SimpleEmbed("Time was reset. Time = 90 seconds").rn())
                    self.startdelmsg.append(timeresetembed)
        except asyncio.TimeoutError:
            self.time = 90

        for m in self.startdelmsg:
            try:
                await m.delete()
            except:
                pass

        Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("Click 👍 to join.",des=f"The time limit for responding in this game is: {self.time//60//60} hours.\nControls for the gamemaster: ✅ to start ❌ to quit the game").rn())
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("✅")
        await Reaction_attachment.add_reaction("❌")
        self.delmsg.append(Reaction_attachment)

        try:
            self.players.append(self.msg.author.id)
            starterjoined = await self.msg.channel.send(f"{self.msg.author.name} started and joined the game.")
            self.delmsg.append(starterjoined)
            while True:
                reaction, user = await responder.wait_for('reaction_add', timeout = self.time,check=lambda reaction,user: reaction.emoji == "👍" and user.id != responder.user.id and user.id not in self.players and reaction.message.id == Reaction_attachment.id or reaction.message.id == Reaction_attachment.id and reaction.emoji in ["✅","❌"] and self.msg.author.id == user.id)
                
                if str(reaction.emoji) == "👍":
                    self.players.append(user.id)
                elif str(reaction.emoji) == "✅":
                    break
                elif str(reaction.emoji) == "❌":
                    return False
                joinedthegamemsg = await self.msg.channel.send(f"{user.name} joined.")
                self.delmsg.append(joinedthegamemsg)
            if len(self.players) <= 0:
                nooneembed = await self.msg.channel.send("No one has joined the game.")
                self.delmsg.append(nooneembed)
                return False

            self.playerjoined = await self.msg.channel.send(f"{len(self.players)} people have joined the game.")
            return True
        except asyncio.TimeoutError:
            await self.msg.channel.send("Game timed out, super sadly...")
            return False
       

    async def GetQuestion(self):
        self.questionembed = await self.msg.channel.send(embed=SimpleEmbed("What is your question?",des="Type your question in this text channel.").rn())
        self.delmsg.append(self.questionembed)
        try:
            self.q = await responder.wait_for('message',timeout=self.time,check=lambda message:message.author.id == self.msg.author.id and message.channel.id == self.msg.channel.id and message.content != "")
            self.question = self.q.content
            self.delmsg.append(self.q)
            self.delmsg.append(self.playerjoined)
            return True
        except asyncio.TimeoutError:
            return False

    async def Results(self):
        questionembedtwo = await self.msg.channel.send(embed=SimpleEmbed("Question:",des=self.question).rn())
        self.delmsg.append(questionembedtwo)
        random.shuffle(self.players)
        for i, player in enumerate(self.players):
            fuser = await responder.fetch_user(player)
            turndisplayembed = await self.msg.channel.send(embed=SimpleEmbed(f"Turn {i+1}",des=f"Waiting on {fuser.mention}, their turn will be skipped in {self.time} seconds.").rn())
            self.delmsg.append(turndisplayembed)
            await fuser.send(embed= SimpleEmbed("Type your answer cooresponding to the question below. 1024 character limit.",des=f"Question: {self.question}").rn() )
            def check(m):
                return m.author.id == player and m.author.id != responder.user.id and m.channel.id == fuser.dm_channel.id and len(m.content.lower()) <= 1024
            try:
                m = await responder.wait_for('message',timeout=self.time,check=check)
                
                self.answers.append(m.content)
                
                await fuser.send(embed=SimpleEmbed("Your answer has been received!").rn())

                hasansweredembed = await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
                self.delmsg.append(hasansweredembed)
            except asyncio.TimeoutError:
                hasnotansweredembed =await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't answer in time").rn())
                self.delmsg.append(hasnotansweredembed)
        if not len(self.answers) == 0:
            Stats_Embed = discord.Embed(title="Stats",description=f"Question = {self.question}",color=0xff0000)
            random.shuffle(self.answers)
            for t in self.answers:
                self.newanswers.append([f"{round(self.answers.count(t)/len(self.answers)*100,3)}%",t])
                for i in self.answers:
                    if i == t:
                        self.answers.remove(i)
                    
            for response in self.newanswers:
                Stats_Embed.add_field(name=response[0],value=response[1],inline=True)
            await self.msg.channel.send(embed=Stats_Embed)
        else:
            Stats_Embed = discord.Embed(title="No one finished the game.",description=f"question = {self.question}",color=0xff0000)
            await asyncio.sleep(10)


class TrustIssuesGame(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    # Trust Issues Game ------------------------------------------------------------------------------------------------------------------------------
    @commands.command(aliases=["trust_issues_custom","trustissuescustom","ti","trust_issues"])
    async def trustissues(self,ctx):
        try:
            INUSE = False
            if not ctx.channel.id in ChannelsInUse:
                ChannelsInUse.append(ctx.channel.id)
                AddAudit(f"{ctx.author} started $ti at {datetime.datetime.now()} in {ctx.channel}")
                if not isinstance(ctx.channel,discord.DMChannel):
                    TINewGame = TrustIssuesGameC(ctx)
                    await TINewGame.MainTable()
            else:
                INUSE = True
                a = await ctx.channel.send("Channel already playing. Wait for the game to end.")
        finally:
            try:
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            if not INUSE == True:
                try:
                    ChannelsInUse.remove(ctx.channel.id)
                except:
                    ChannelsInUse.clear()
            else:
                await asyncio.sleep(10)
                await a.delete()

            return