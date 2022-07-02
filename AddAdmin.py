from __module import *

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