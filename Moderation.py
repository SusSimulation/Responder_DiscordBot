from __module import *

class Moderation(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client

    @commands.command(aliases=["add_welcome","bienvenue"])
    @commands.has_permissions(administrator=True, ban_members=True)
    @cooldowns(25)
    async def addwelcome(self,ctx):
        await responder.wait_until_ready()
        try:
            with open(f"{MAINPATH}//WelcomeGuilds.txt","r") as f:
                if str(ctx.guild.id) in f.read():
                    await ctx.channel.send("Server already allows welcome messages.\nIf you don't know how to activate it, make sure that there is a channel named; 'welcome'\nIf you want the bot the give a role when someone joins, make sure there is a role named; 'Member'.")
                    return
            with open(f"{MAINPATH}//WelcomeGuilds.txt","r") as fi:
                file = fi.read()
                with open(f"{MAINPATH}//WelcomeGuilds.txt","w") as fil:
                    fil.write(file+f"{ctx.guild.id}\n")
                await ctx.channel.send("Successfully added feature!")
        except Exception as e:
            await ctx.channel.send(f"Major error, could effect most servers; please report this error, The error message is; {e}")
        finally:
            try:
                await ctx.message.delete()
            except:
                pass

    @commands.command(aliases=["remove_welcome","supprimer_l'accueil"])
    @commands.has_permissions(administrator=True, ban_members=True)
    @cooldowns(25)
    async def removewelcome(self,ctx):
        await responder.wait_until_ready()
        try:
            with open(f"{MAINPATH}//WelcomeGuilds.txt","r") as f:
                if str(ctx.guild.id) in f.read():
                    with open(f"{MAINPATH}//WelcomeGuilds.txt","r") as f:
                        new = f.read().replace(f"{ctx.guild.id}\n","")
                        with open(f"{MAINPATH}//WelcomeGuilds.txt","w") as fil:
                            fil.write(new)
                    await ctx.channel.send("Succesfully removed feature, thank you for using it!")
                    return
                else:
                    await ctx.channel.send("This server does not have the welcome feature yet, to add it type; $remove_welcome")
        except Exception as e:
            await ctx.channel.send(f"Major error, could effect most servers; please report this error, The error message is; {e}")
        finally:
            try:
                await ctx.message.delete()
            except:
                pass

    @commands.command(aliases=["language","swap_language","changerlangue"])
    @cooldowns(25)
    async def change_language(self,ctx):
        await responder.wait_until_ready()
        try:
            with open(f"{MAINPATH}//Francais.txt","r") as f:
                if str(ctx.author.id) in f.read():
                    with open(f"{MAINPATH}//Francais.txt","r") as f:
                        new = f.read().replace(f"{ctx.author.id}\n","")
                        with open(f"{MAINPATH}//Francais.txt","w") as fil:
                            fil.write(new)
                    await ctx.channel.send("Succesfully changed language, you are now in english.")
                else:
                    with open(f"{MAINPATH}//Francais.txt","r") as fi:
                        file = fi.read()
                        with open(f"{MAINPATH}//Francais.txt","w") as fil:
                            fil.write(file+f"{ctx.author.id}\n")
                        await ctx.channel.send("La langue a été changée en français avec succès !")
        except Exception as e:
            if French(ctx).rn() == False:
                await ctx.channel.send(f"Major error, could effect most servers; please report this error, The error message is; {e}")
            else:
                await ctx.channel.send(f"Erreur majeure, pouvant affecter la plupart des serveurs ; veuillez signaler cette erreur, Le message d'erreur est: {e}")
        finally:
            pass
