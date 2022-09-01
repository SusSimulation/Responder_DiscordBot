from __module import *

class MHAExport:
    def __init__(self,msg) -> None:
        self.msg = msg

    async def SendRandomPhoto(self):
        try:
            a = await self.msg.channel.send( file=discord.File( f"{MAINPATH}MHA//{random.choice( os.listdir(f'{MAINPATH}MHA' ) )}") )
        finally:
            await asyncio.sleep(3500)
            await a.delete()

### SEND PHOTO FOR $PHOTO --------------------------------------------------------------------------------------------------------------------
class PersonalPhotoExport:
    def __init__(self,msg) -> None:
        self.msg = msg

    async def SendRandomPhoto(self):
        try:
            try:
                a = await self.msg.channel.send( file=discord.File( f"{MAINPATH}$photo//{random.choice( os.listdir(f'{MAINPATH}$photo' ) )}") )
            except:
                await self.msg.channel.send("No.")
        finally:
            await asyncio.sleep(3600)
            try:
                await a.delete()
            except:
                pass

### SAVE FOR $PHOTO --------------------------------------------------------------------------------------------------------------------
class PersonalPhotoImport:
    def __init__(self,msg) -> None:
        try:
            self.msg = msg
            self.name = "12345678910qwertyuiopafghjklzcvbnm_QWERTYUIOPASDFGHJKLZXCVBNM__"
        except Exception as e:
            pass

    async def SavePhoto(self):
        try:
            pspembed = discord.Embed(title="Please Send a photo.", color=0xdc00ff)
            await self.msg.channel.send(embed=pspembed)

            self.file = await responder.wait_for("message",timeout=60,check=lambda msg: msg.author.id != responder.user.id and msg.author.id == self.msg.author.id)
            await pspembed.delete()
            for attachment in self.file.attachments:
                await attachment.save(attachment.filename)
                self.newname = ''.join(random.sample(self.name,len(self.name)))
                os.rename(f"{MAINPATH}{attachment.filename}",f"{MAINPATH}{self.newname}.png")
                shutil.move(f"{MAINPATH}{self.newname}.png",f"{MAINPATH}$photo")
            siembed = SimpleEmbed(f"Sucessfully imported! Items saved to {MAINPATH}$photo",des=self.newname).rn()
            await self.msg.channel.send(embed = siembed)

        except asyncio.TimeoutError:
            pass
        except Exception as e:
            usiembed = discord.Embed(title=f"unsucessfull, did not import.",desciption=f"{e}",color=0xdc00ff)
            await self.msg.channel.send(embed=usiembed)
        finally:
            await asyncio.sleep(10)
            await self.file.delete()

class PostAndSaves(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    
    @commands.command()
    async def hen(self,ctx):
        try:
            AddAudit(f"{ctx.author} started Hen at {datetime.datetime.now()} in {ctx.channel}")
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

    @commands.command()
    async def mha(self,ctx):
        try:
            AddAudit(f"{ctx.author} started MHA at {datetime.datetime.now()} in {ctx.channel}")
            await MHAExport(ctx).SendRandomPhoto()
        finally:
            await ctx.message.delete()

    @commands.command()
    async def photo(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $photo at {datetime.datetime.now()} in {ctx.channel} in {ctx.guild.name}")
            if ReturnGuildOrAuthor(ctx).rn() in COOLGUILDS:
                partA =  PersonalPhotoExport(ctx)
                await partA.SendRandomPhoto()
            else:
                print("How do they know???")
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            return

    @commands.command()
    async def add(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $add at {datetime.datetime.now()} in {ctx.channel}")
            if ReturnGuildOrAuthor(ctx).rn() in COOLGUILDS:
                ImportPhoto = PersonalPhotoImport(ctx)
                await ImportPhoto.SavePhoto()
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            return
    
    @commands.command()
    async def poky(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $Poky at {datetime.datetime.now()} in {ctx.channel}")
            try:
                File = random.choice(os.listdir(f"{MAINPATH}Poky"))
                a = await ctx.channel.send(file=discord.File(f"{MAINPATH}Poky/{File}"))
            finally:
                await asyncio.sleep(3600)
                await a.delete()
        finally:
            await ctx.message.delete()

    @commands.command()
    async def zeldass(self,ctx):
        try:
            AddAudit(f"{ctx.author} started $zeldass at {datetime.datetime.now()} in {ctx.channel}")
            if not isinstance(ctx.channel,discord.DMChannel):
                if ctx.channel.is_nsfw():
                    file = random.choice(os.listdir(f"{MAINPATH}ZeldaFiles"))
                    f = await ctx.channel.send(file=discord.File(f"{MAINPATH}ZeldaFiles/{file}"))
                else:
                    await ctx.channel.send("This is not a NSFW channel.")
        finally:
            try:
                # if not a dm channel, but a server channel
                if not isinstance(ctx.channel, discord.DMChannel):
                    # Delete the message to reduce spam
                    await ctx.message.delete()
            except discord.errors.NotFound:
                pass
            await asyncio.sleep(3600)
            await f.delete()
            return
    

    