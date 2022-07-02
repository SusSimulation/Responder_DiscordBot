from __module import *

TIMEONLINE = time.time()

# On boot, we/I do this... ------------------------------------------------------------------------------------------------------------------------------
@responder.event
async def on_ready():
    try:
        print("-"*40)
        print(f"Logged in boy's! {MAINPATH}")
        print(f"Logged in as {responder.user.name} with the id of {responder.user.id}")
        print(f"I am in {len([guild for guild in responder.guilds])} guilds!")
        print("-"*40)
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised while logging in."))
        exit()
    finally:
        return

# remove the usless error message; discord.ext.commands.errors.CommandNotFound
@responder.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed=SimpleEmbed(f"${ctx.command.name} requires argument < {error.param.name} >.").rn())
        return
    raise error

# ADD ADMIN ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def add_admin(ctx, user: discord.Member):
    try:
        if ctx.author.id in ADMINS:
            if user.id in ADMINS:
                await ctx.send(embed=SimpleEmbed("Yay!","This user is already an admin!").rn())
            else:
                ADMINS.append(user.id)
                with open("{MAINPATH}ADMINS.txt", "w") as f:
                    f.write(str(ADMINS)+"\n")
                await ctx.send(embed=SimpleEmbed("Yay!","This user is now an admin!").rn())
    except Exception as e:
        await ctx.send(embed=SimpleEmbed("Yay!","Error was raised while adding admin!").rn())
    finally:
        return


# Help Command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def help(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        # initialize the embed
        Commands_Embed_for_Help_Command = SimpleEmbed("Commands",des=f"{responder.user.name} has been online for { round((time.time()-TIMEONLINE)/60/60,4) } hours.\nRequested by: {ctx.author.mention}\nGames can only be called once at a time in a chat channel ( It can cause errors! )").rn()
        # Add a field for each command
        for i in Commands:
            UpdatedCommands_Embed_for_Help_Command = Commands_Embed_for_Help_Command.add_field(name=f"{i}",value=f"{Commands[i]}",inline=False)
        # Send the embed
        HelpCommandEmbed = await ctx.channel.send(embed=UpdatedCommands_Embed_for_Help_Command)
        # Adding reaction for easy deleting of the embeded message.
        await HelpCommandEmbed.add_reaction("❌")
        try:
            # Waiting for user to react with the ❌ emoji.
            await responder.wait_for("reaction_add",timeout=20,check=lambda reaction,user: reaction.emoji == "❌" and user == ctx.author and HelpCommandEmbed == reaction.message)
            # When user does react with the ❌ emoji, the embeded message will be deleted.
            await HelpCommandEmbed.delete()
        except asyncio.TimeoutError:
            # If the user does not react with the ❌ emoji, the reaction will be removed from the embed.
            await HelpCommandEmbed.remove_reaction("❌",responder.user)
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) NAME = {e.__class__.__name__} Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        return

# Rebooting the __main__.py file. ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def reboot(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        if ctx.author.id in ADMINS:
            await ctx.channel.send(embed=SimpleEmbed(f"Rebooting...",des=f"{ctx.message.author.mention} is rebooting the bot...").rn())
            call(["python", f"{MAINPATH}__main__.py"])
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        exit()

# Quit the program ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def quit(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        # If the user is in the ADMINS[0] list, then the bot will quit.
        if ctx.author.id == ADMINS[0]:
            # SUper cool embed message sending to the channel.
            await ctx.channel.send(embed=SimpleEmbed(f"Quitting...",des=f"{ctx.message.author.mention} is quitting the bot...").rn())
            exit()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        exit()

# Sending all of the .py files in the folder to the channel. ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def files(ctx):
    try:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        # If the user is in the ADMINS[0] list, then the bot will quit.
        if ctx.author.id == ADMINS[0]:
            # SUper cool embed message sending to the channel.
            await ctx.channel.send(embed=SimpleEmbed(f"Sending files...",des=f"{ctx.message.author.mention} is sending files...").rn())
            # Sending all of the .py files in the folder to the channel.
            for file in os.listdir(MAINPATH):
                try:
                    if file.endswith(".py"):
                        await ctx.channel.send(file=discord.File(f'{file}'))
                except IsADirectoryError:
                    pass
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
        return
    finally:
        return

#Server names ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def servers(ctx):
    try:
        if ctx.author.id in ADMINS:
            # Creating an regular embed for the server names.
            Servers_Embed = discord.Embed(title=f"Servers",des=f"{ctx.message.author.mention} is sending the server names...",color=0x00ff00)
            # Iterating through all of the servers.
            for server in responder.guilds:
                Servers_Embed.add_field(name=server.name,value=server.id,inline=True)
            # Sending the embed to the channel.
            await ctx.channel.send(embed=Servers_Embed)
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return
 
# Info about server and bot ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def info(ctx):
    try:
        embed = discord.Embed(title=f"Info",description=f"Requested by: {ctx.author.mention}\nIf you find any bugs, please report them and Jazzyjazz404#8538 will give you admin access.", color=0xdc00ff)
        embed.add_field(name="Current Time",value=f"{datetime.datetime.now()}",inline=False)
        embed.add_field(name="CPU Usage",value=f"{psutil.cpu_percent()}%",inline=False)
        embed.add_field(name="RAM Usage",value=f"{psutil.virtual_memory().percent}%",inline=False)
        embed.add_field(name="Disk Usage",value=f"{psutil.disk_usage('/').percent}%",inline=False)
        embed.add_field(name="Users",value=f"{len(psutil.users())}",inline=False)
        embed.add_field(name="Ping",value=f"{round(responder.latency * 1000)}ms",inline=False)
        total, used, free = shutil.disk_usage("/")
        embed.add_field(name="Total Storage",value=f"Total: %d GiB" % (total // (2**30)))
        embed.add_field(name="Used Storage",value=f"Used: %d GiB" % (used // (2**30)))
        embed.add_field(name="Free Storage",value=f"Free: %d GiB" % (free // (2**30)))
        embed.add_field(name="Uptime",value=f"{(time.time()-TIMEONLINE)/60} minutes",inline=False)
        embed.add_field(name="Version",value=f"{VERSION}",inline=False)
        embed.add_field(name="Guilds",value=f"{len([guild for guild in responder.guilds])}",inline=False)
        embed.add_field(name="Users",value=f"{len([user for user in responder.users])}",inline=False)
        e = await ctx.channel.send(embed=embed)
        await e.add_reaction("❌")
        try:
            # Waiting for user to react with the ❌ emoji.
            await responder.wait_for("reaction_add",timeout=20,check=lambda reaction,user: reaction.emoji == "❌" and user == ctx.author and e == reaction.message)
            # When user does react with the ❌ emoji, the embeded message will be deleted.
            await e.delete()
        except asyncio.TimeoutError:
            # If the user does not react with the ❌ emoji, the reaction will be removed from the embed.
            await e.remove_reaction("❌",responder.user)
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# Trust Issues Game ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def ti(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            await TrustIssuesGame(ctx).MainTable()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return


# Photo command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def photo(ctx):
    try:
        if ReturnGuildOrAuthor(ctx).rn() in COOLGUILDS:
            SendPhoto = PersonalPhotoExport(ctx)
            await SendPhoto.SendRandomPhoto()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())

    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

@responder.command()
async def add(ctx):
    try:
        if ReturnGuildOrAuthor(ctx).rn() in COOLGUILDS:
            ImportPhoto = PersonalPhotoImport(ctx)
            await ImportPhoto.SavePhoto()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# Black Jack ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def blackjack(ctx):
    try:
        if not isinstance(ctx.channel,discord.DMChannel):
            Blackjack = BlackjackGame(ctx.message)
            await Blackjack.StartGame()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())

    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# quote command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def quote(ctx):
    try:
        NewQuote = Quote(ctx)
        await NewQuote.Send()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# 8ball command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def eightball(ctx):
    try:
        New8Ball = EightBall(ctx)
        await New8Ball.Send()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# rock paper scissors ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def rps(ctx):
    try:
        NewRPS = RPS(ctx)
        await NewRPS.UserTurn()
        await NewRPS.BotTurn()
        await NewRPS.Winner()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# Survey  ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def survey(ctx):
    try:
        NewSurvey = Survey(ctx)
        await NewSurvey.Question()
        await NewSurvey.Answer()
        await NewSurvey.Stats()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return

# Penis measurer ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def pp(ctx):
    try:
        NewPP = PenisMeasurer(ctx)
        await NewPP.Send()
    except Exception as e:
        # If there is a super big error, the error will be posted in that channel, and along in the dms of JAZZYJAZZ.
        # Fetch 'me'
        JAZZYJAZZ = await responder.fetch_user(ADMINS[0])
        # Send the error in the dms of JAZZYJAZZ
        await JAZZYJAZZ.send(embed=SimpleEmbed("Yay! Error!",des=f"({e}) Error was raised in {ReturnInfo(ctx).rn()}").rn())
        # Send the error in the channel
        await ctx.channel.send(embed=SimpleEmbed("Unknown Error",des=f"{e}").rn())
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return




### MAIN CODE ------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        responder.run(RESPONDERTOKEN)
    except Exception as e:
        print(f"Error: {e}")
        quit()
    


