import discord
from discord.ext import commands
from discord import app_commands
from var import version

class Tools(commands.GroupCog, name="tools"):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    # Pour synchroniser les commandes slash
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"{len(fmt)} commandes ont été synchronisées.")

    # Affiche la version du Bot
    @app_commands.command(name="version", description="Affiche la version du Bot.")
    async def ver(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"SoundBot est en version **{version}**.", ephemeral=True)
        
    # Envoie le Lien du Github du Bot
    @app_commands.command(name="github", description="Récupère le lien du repo Github.")
    async def git(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Lien du repo: https://github.com/Tintin361/SoundBot", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tools(bot))