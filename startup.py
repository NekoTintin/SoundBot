from os import listdir

import discord
from discord.ext import commands
from discord.embeds import Embed
import asyncio

import var

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents, application_id=var.app_id, help_command=None)

@bot.command()
async def startup(bot):
    async with bot:
        for filename in listdir('/home/Tintin/discord_bot/SoundBot/cogs'):
            if filename.endswith(".py"):
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(var.api_code)
        
# Erreur de commande
@bot.event
async def on_command_error(ctx, error):
    print(error)
    emd = Embed(title="<:Erreur:945123023546093611> Commande inconnue", description="Erreur dans la commande.", color=0xe24647).add_field(name="Sortie:", value=str(error), inline=False)
    await ctx.channel.send(embed=emd)
        
asyncio.run(startup(bot))