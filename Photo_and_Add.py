from __module import *

# Photo command ------------------------------------------------------------------------------------------------------------------------------
@responder.command()
async def photo(ctx):
    try:
        if ReturnGuildOrAuthor(ctx).rn() in COOLGUILDS:
            SendPhoto = PersonalPhotoExport(ctx)
            await SendPhoto.SendRandomPhoto()
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
    finally:
        try:
            # if not a dm channel, but a server channel
            if not isinstance(ctx.channel, discord.DMChannel):
                # Delete the message to reduce spam
                await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        return