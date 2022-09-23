from __module import *
import random

#BETA
Sayings = ["Thanks for joining!","Feel free to do anything you would like!","Thanks for joining us.","Happy to see you here!","We appreciate your support."]

@responder.event
async def on_member_join(member):
    with open(f"{MAINPATH}//WelcomeGuilds.txt","r") as f:
        if str(member.guild.id) in f.read():
            for channel in member.guild.channels:
                if "welcome" in channel.name or channel.name in ["welcome","hello","hi","joins"]:
                    await channel.send(embed=SimpleEmbed(f"Welcome {member}!",des=f"{member.mention} {Sayings[random.randint(0,len(Sayings)-1)]} Feel free, check out the voice chats, channels, and the rules.").rn())
                    Role = discord.utils.get(member.guild.roles, name="Member")
                    await member.add_roles(Role)

    return


@responder.event
async def on_member_remove(member):
    if member.guild.id == 1017015887695450152: 
        await responder.get_channel(1017017584362725456).send(embed=SimpleEmbed(f"{member} left the server.").rn())
    return



