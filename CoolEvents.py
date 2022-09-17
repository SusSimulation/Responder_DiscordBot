from __module import *
import random

Sayings = ["Thanks for joining!","Feel free to do anything you would like!","Thanks for joining us.","Happy to see you here!","We appreciate your support."]

@responder.event
async def on_member_join(member):
    # Main Server!! Should be named; TrustIssues.
    if member.guild.id == 992058629517742080: 
        AddAudit(f"{member} joined the main server.")
        role = discord.utils.get(member.guild.roles, name="Member")
        await responder.get_channel(992110942156505099).send(f"{member.mention} welcome! {Sayings[random.randint(0,len(Sayings)-1)]}")
        await responder.get_channel(992110942156505099).send(embed=SimpleEmbed(t=f"{member.name} has joined!",des=f"I have assigned you the role: {role.name}.").rn())
        await member.add_roles(role)
    elif member.guild.id == 1017015887695450152:
        role = discord.utils.get(member.guild.roles, name="Communist enjoyer",id=1017016090758479884)
        await responder.get_channel(1017017549118001173).send(f"{member.mention} welcome! {Sayings[random.randint(0,len(Sayings)-1)]}")
        await responder.get_channel(1017017549118001173).send(embed=SimpleEmbed(t=f"{member.name} has joined",des=f"I have assigned you the role: {role.name}.").rn())
        await member.add_roles(role)
    # Still figuring it out...
    elif member.guild.id in WelcomeGuilds:
        pass
    return

@responder.event
async def on_member_remove(member):
    if member.guild.id == 1017015887695450152:
        await responder.get_channel(1017017584362725456).send(embed=SimpleEmbed(f"{member} left the server.").rn())
    return



