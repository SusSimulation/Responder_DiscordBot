from __module import *
import random

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
        self.French = French(self.msg).rn()
        if self.French == True:
            self.language = "FR"
        else:
            self.language = "EN"
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
        if self.language == "FR":
            customtimeembed = await self.msg.channel.send(embed=SimpleEmbed("🕐 = ajouter 1 minute. ⌛ = ajouter 1 heure. 📅 = ajouter 1 jour.",des="Cliquez sur le ❌ pour réinitialiser le temps. ✅ pour continuer le jeu !").rn())
        else:
            customtimeembed = await self.msg.channel.send(embed=SimpleEmbed("🕐 = add 1 minute. ⌛ = add 1 hour. 📅 = add 1 day.",des="Click the ❌ to reset time. ✅ to continue the game!").rn())
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
                    if self.language == "FR":
                        minembed = await self.msg.channel.send(embed=SimpleEmbed("1 minute a été ajoutée!",des=f"Temps = {self.time//(60)} minutes").rn())
                    else:
                        minembed = await self.msg.channel.send(embed=SimpleEmbed("1 minute was added!",des=f"Time = {self.time//(60)} minutes").rn())
                    self.startdelmsg.append(minembed)
                elif str(reaction.emoji) == "⌛":
                    self.time += 3600
                    if self.language == "FR":
                        hourembed = await self.msg.channel.send(embed=SimpleEmbed("1 heure a été ajoutée!",des=f"Temps = {self.time//(60*60)} heures").rn())
                    else:
                        hourembed = await self.msg.channel.send(embed=SimpleEmbed("1 hour was added!",des=f"Time = {self.time//(60*60)} hours").rn())
                    self.startdelmsg.append(hourembed)
                elif str(reaction.emoji) == "📅":
                    self.time += 86400
                    if self.language == "FR":
                        dayembed = await self.msg.channel.send(embed=SimpleEmbed("1 jour a été ajoutée!",des=f"Temps = {self.time//(60*60*24)} jours").rn())
                    else:
                        dayembed = await self.msg.channel.send(embed=SimpleEmbed("1 day was added!",des=f"Time = {self.time//(60*60*24)} days").rn())

                    self.startdelmsg.append(dayembed)
                elif str(reaction.emoji) == "✅":
                    break
                elif str(reaction.emoji) == "❌":
                    self.time = 90
                    if self.language == "FR":
                        timeresetembed = await self.msg.channel.send(embed=SimpleEmbed("Le temps a été remis à zéro. Temps = 90 secondes").rn())
                    else:
                        timeresetembed = await self.msg.channel.send(embed=SimpleEmbed("Time was reset. Time = 90 seconds").rn())

                    self.startdelmsg.append(timeresetembed)
        except asyncio.TimeoutError:
            self.time = 90

        for m in self.startdelmsg:
            try:
                await m.delete()
            except:
                pass
        
        if self.language == "FR":
            Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("Cliquez sur 👍 pour vous inscrire.",des=f"Le temps limite pour répondre dans ce jeu est de : {self.time//60//60} heures.\nContrôles pour le maître du jeu : ✅ pour démarrer ❌ pour quitter le jeu").rn())
        else:
            Reaction_attachment = await self.msg.channel.send(embed=SimpleEmbed("Click 👍 to join.",des=f"The time limit for responding in this game is: {self.time//60//60} hours.\nControls for the gamemaster: ✅ to start ❌ to quit the game").rn())
          
        await Reaction_attachment.add_reaction("👍")
        await Reaction_attachment.add_reaction("✅")
        await Reaction_attachment.add_reaction("❌")
        self.delmsg.append(Reaction_attachment)

        try:
            self.players.append(self.msg.author.id)
            if self.language == "FR":
                starterjoined = await self.msg.channel.send(f"{self.msg.author.name} a commencé et a rejoint le jeu.")
            else:
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

                if self.language == "FR":
                    joinedthegamemsg = await self.msg.channel.send(f"{user.name} a rejoint.")
                else:
                    joinedthegamemsg = await self.msg.channel.send(f"{user.name} joined.")
                self.delmsg.append(joinedthegamemsg)
            if self.language == "FR":
                self.playerjoined = await self.msg.channel.send(f"{len(self.players)} personnes ont rejoint le jeu.")
            else:
                self.playerjoined = await self.msg.channel.send(f"{len(self.players)} people have joined the game.")
            return True
        except asyncio.TimeoutError:
            if self.language == "FR":
                await self.msg.channel.send("Le jeu s'est arrêté, c'est triste...")
            else:
                await self.msg.channel.send("Game timed out, super sadly...")
            return False
       

    async def GetQuestion(self):
        if self.language == "FR":
            self.questionembed = await self.msg.channel.send(embed=SimpleEmbed("Quelle est votre question ?",des="Tapez votre question dans ce canal de texte.").rn())
        else:
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
            if self.language == "FR":
                turndisplayembed = await self.msg.channel.send(embed=SimpleEmbed(f"Tour {i+1}",des=f"En attendant {fuser.mention}, leur tour sera sauté dans {self.time} secondes.").rn())
            else:
                turndisplayembed = await self.msg.channel.send(embed=SimpleEmbed(f"Turn {i+1}",des=f"Waiting on {fuser.mention}, their turn will be skipped in {self.time} seconds.").rn())
            self.delmsg.append(turndisplayembed)
            if self.language == "FR":
                await fuser.send(embed= SimpleEmbed("Tapez votre réponse en coorespondant à la question ci-dessous. Limite de 1024 caractères.",des=f"Question : {self.question}").rn())
            else:
                await fuser.send(embed= SimpleEmbed("Type your answer cooresponding to the question below. 1024 character limit.",des=f"Question: {self.question}").rn() )

            def check(m):
                return m.author.id == player and m.author.id != responder.user.id and m.channel.id == fuser.dm_channel.id and len(m.content.lower()) <= 1024
            try:
                m = await responder.wait_for('message',timeout=self.time,check=check)
                
                self.answers.append(m.content)
                if self.language == "FR":
                    await fuser.send(embed=SimpleEmbed("Votre réponse a été reçue !").rn())
                else:
                    await fuser.send(embed=SimpleEmbed("Your answer has been received!").rn())

                if self.language == "FR":
                    hasansweredembed = await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} a répondu.").rn())
                else:
                    hasansweredembed = await self.msg.channel.send(embed = SimpleEmbed(f"{m.author.name} has answered.").rn())
                self.delmsg.append(hasansweredembed)
            except asyncio.TimeoutError:
                if self.language == "FR":
                    hasnotansweredembed =await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} a été ignoré. N'a pas répondu à temps.").rn())
                else:
                    hasnotansweredembed =await self.msg.channel.send(embed = SimpleEmbed(f"{fuser.name} has been skipped. Didn't answer in time.").rn())
                self.delmsg.append(hasnotansweredembed)
        if not len(self.answers) == 0:
            Stats_Embed = discord.Embed(title="Stats",description=f"Question = {self.question}",color=0xff0000)
            random.shuffle(self.answers)
                    
            for response in self.answers:
                Stats_Embed.add_field(name="?",value=response,inline=True)
            await self.msg.channel.send(embed=Stats_Embed)
        else:
            if self.language == "FR":
                Stats_Embed = discord.Embed(title="Personne n'a terminé le jeu.",description=f"Question = {self.question}",color=0xff0000)
            else:
                Stats_Embed = discord.Embed(title="No one finished the game.",description=f"Question = {self.question}",color=0xff0000)

            await asyncio.sleep(10)


class TrustIssuesGame(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    # Trust Issues Game ------------------------------------------------------------------------------------------------------------------------------
    @commands.command(aliases=["trustissue","ti","trust_issues","t_i"])
    @cooldowns(20)
    async def trustissues(self,ctx):
        try:
            if "trust" in ctx.channel.name:
                try:

                    INUSE = False
                    if not ctx.channel.id in ChannelsInUse:
                        ChannelsInUse.append(ctx.channel.id)
                        if not isinstance(ctx.channel,discord.DMChannel):
                            AddAudit(ctx,finished=False)
                            TINewGame = TrustIssuesGameC(ctx)
                            await TINewGame.MainTable()
                        else:
                            return
                    else:
                        INUSE = True
                        if French(ctx).rn() == True:
                            a = await ctx.channel.send("Chaîne déjà en jeu. Attendez que le jeu se termine.")
                        else:
                            a = await ctx.channel.send("Channel already playing. Wait for the game to end.")
                finally:
                    try:
                        await ctx.message.delete()
                    except:
                        pass
                    if INUSE != True:
                        try:
                            ChannelsInUse.remove(ctx.channel.id)
                        except:
                            ChannelsInUse.clear()
                    else:
                        await asyncio.sleep(10)
                        await a.delete()
                    return
            else:
                if French(ctx).rn() == True:
                    await ctx.channel.send("Pour jouer à TrustIssues, il faut avoir un canal nommé trust-issues ou trustissues (ou du moins avoir cela dans le nom). Si vous souhaitez un canal personnalisé, demandez-le à notre support et nos développeurs feront de leur mieux !")
                else:
                    await ctx.channel.send("To play TrustIssues there needs to be a channel named; trust-issues or trustissues (or at least have 'trust' in the name).\nIf you would like a custom channel area ask in our support and our developers will do their best!")
                try:
                    await ctx.message.delete()
                except:
                    pass
        finally:
            AddAudit(ctx,finished=True)

    
            