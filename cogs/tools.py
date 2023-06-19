import discord
from discord.ext import commands
from discord import app_commands
from discord.embeds import Embed
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
        
    # Renvoie un lien vers le repo GitHub
    @app_commands.command(name="github", description="Lien vers le repo sur GitHub.")
    async def git(self, interaction: discord.Interaction):
        message = Embed(title="Lien du GitHub:", color=0xfbfcfc).add_field(name="Repo de Kiri-Chan:", value="https://github.com/Tintin361/Kiri-chan")\
        .add_field(name="Repo de Little Kyubey", value="https://github.com/Tintin361/Lil_Kyubey")\
        .add_field(name="Repo de NekoBot", value="https://github.com/Tintin361/NekoBot")\
        .add_field(name="Repo de VeemoBot", value="https://github.com/Tintin361/VeemoBot")
        await interaction.response.send_message(embed=message, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tools(bot))