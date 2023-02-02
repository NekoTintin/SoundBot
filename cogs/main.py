import discord
from discord.ext import commands
from discord import app_commands
from var import version

sounds_path = "/home/Tintin/discord_bot/SoundBot/sounds/"

class main(commands.Cog):
    
    def __init__(self, bot: commands.bot) -> None:
        self.bot = bot
        self.voice = None
        self.channel = None
        
    # Commande executée au démarrage du Bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Démarrage du SoundBot")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Fart Reverb SFX."))
        
    @commands.Cog.listener()
    async def on_message(self, message):
        msg_str = str(message.content)
        if message.author == self.bot.user:
            return
        if self.bot.user.mentioned_in(message) and message.mention_everyone == False:
            await message.channel.send(f"Hello {message.author.mention}, les commandes sont indiquées quand tu écrit '/' dans le chat.")
            
    
    # Pour synchroniser les commandes slash
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"{len(fmt)} commandes ont été synchronisées.")
        
    # Affiche la version du Bot
    @app_commands.command(name="version", description="Affiche la version du Bot.")
    async def ver(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"SoundBot est en version **{version}**.")
        
    # Envoie le Lien du Github du Bot
    @app_commands.command(name="github", description="Récupère le lien du repo Github.")
    async def git(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Lien du repo: https://github.com/Tintin361/SoundBot")
        
    
    # Connexion au salon vocal de l'utilisateur
    @app_commands.command(name="connect", description="Ajoute le bot dans ton channel vocal.")
    async def connect_voice(self, interaction: discord.Interaction) -> None:
        try:
            self.channel = interaction.user.voice.channel
        except:
            await interaction.response.send_message("Tu n'est pas connecté dans un salon vocal")
            return
        
        guild = interaction.guild
        self.voice = discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        
        if self.voice == None:
            await self.channel.connect()   
            self.voice = discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            
        await interaction.response.send_message(f"Connecté dans le salon **{self.channel.name}**")
            
    # Déconnecte le bot du salon vocal actuel
    @app_commands.command(name="disconnect", description="Retire le bot de ton channel vocal.")
    async def disconnect_voice(self, interaction: discord.Interaction) -> None:
        if self.voice.is_playing():
            self.voice.stop()
        
        try:
            await self.voice.disconnect()
            await interaction.response.send_message("Déconnecté")
        except:
            await interaction.response.send_message("Le bot n'est connecté dans aucun salon vocal.")
        
    # Joue un son parmi dans la liste
    @app_commands.command(name="sound", description="Jouer un son dans un salon vocal.")
    @app_commands.describe(son="Sélectionne un son")
    @app_commands.choices(son=[
        discord.app_commands.Choice(name="C'est nul !", value="1"),
        discord.app_commands.Choice(name="Fart Reverb SFX", value="2"),
        discord.app_commands.Choice(name="Salut mon pote !", value="3"),
        discord.app_commands.Choice(name="SEEEEEEEEGS", value="4"),
        discord.app_commands.Choice(name="Tu veux du pain ?", value="5"),
        discord.app_commands.Choice(name="Une blague sur les noirs", value="6"),
        discord.app_commands.Choice(name="Pouf", value="7"),
        discord.app_commands.Choice(name="Ta gueule", value="8"),
        discord.app_commands.Choice(name="C'est pas toi qui décide", value="9"),
        discord.app_commands.Choice(name="Feur", value="10"),
        discord.app_commands.Choice(name="C'est bien Éleonore", value="11"),
        discord.app_commands.Choice(name="Proverbe", value="12"),
        discord.app_commands.Choice(name="Oh these are pretty cool bananas", value="13"),
        discord.app_commands.Choice(name="Ah merde, c'est con ça", value="14"),
        discord.app_commands.Choice(name="Ouais mais c’est pas toi qui décide", value="15") # Nique ta mère la virgule
        ])
    async def sound_command(self, interaction: discord.Interaction, son: discord.app_commands.Choice[str]):
        
        try:
            self.channel = interaction.user.voice.channel
        except:
            await interaction.response.send_message("Tu n'est pas connecté dans un salon vocal.")
            return
        
        guild = interaction.guild
        self.voice = discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        
        if self.voice == None:
            await self.channel.connect()   
            self.voice = discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            
        if self.voice.is_playing():
            self.voice.stop()
        self.voice.play(source=discord.FFmpegPCMAudio(f"{sounds_path}{son.name}.mp3"))
        
        await interaction.response.send_message(f"Lecture du son: '**{son.name}**'.", ephemeral=True)
        
    @app_commands.command(name="stop", description="Stop le son en cours de lecture.")
    async def stop_sound(self, interaction: discord.Interaction) -> None:
        if self.voice.is_playing() == True:
            self.voice.stop()
            await interaction.response.send_message("Arrêt du son en cours de lecture.", ephemeral=True)
        else:
            await interaction.response.send_message("Aucun son n'est en cours de lecture...", ephemeral=True)

async def setup(bot):
    await bot.add_cog(main(bot))