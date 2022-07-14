from __module import *

# 8ball command ------------------------------------------------------------------------------------------------------------------------------
@responder.command("8ball")
async def eightball(ctx):
    try:
        New8Ball = EightBall(ctx)
        await New8Ball.Send()
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return
