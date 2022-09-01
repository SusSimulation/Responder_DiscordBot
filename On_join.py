from __module import *

@responder.event
async def on_member_join(member):
    if member.guild.id == 992058629517742080:  #type your server name
        AddAudit(f"Member joined with the name; {member.name}")
        embed = discord.Embed(title=f'welcome {member.name} !\nwelcome to {member.guild.name} go see #rules, and chillax',color=0x0061ff,font_size=200)
        await responder.get_channel(992110942156505099).send(f"{member.mention}")
        await responder.get_channel(992110942156505099).send(embed=embed)
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)
    else:
        return