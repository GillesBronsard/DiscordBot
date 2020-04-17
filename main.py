import discord #pip install discord
from notOnGit import laCleSecrete #le token est dans un fichier à part et ignoré par github

#ajouter un composant de discord.py
from discord.ext import commands

# creer une nouvelle instance de notre bot
bot = commands.Bot(command_prefix='!')

#detecter quand le bot est ON
@bot.event
async def on_ready():
	print("Bot ready !")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Gilles est en ligne"))

#creer la commande !regles
@bot.command()
async def regles(ctx):
	await ctx.send("Les règles :\n1. Pas d'insultes\n2. Pas de double compte\n3. Pas de spam")

#creer la commande !bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, new_member : discord.Member):
	pseudo = new_member.mention
	await ctx.send(f"Bienvenue à {pseudo} sur le serveur Discord")

#verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
	#detecter cette erreur
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("tu doit taper !bienvenue @pseudo")
		
#donner le jeton pour qu'il se connecte
jeton = laCleSecrete

#test
print('Test')

#connecter au serveur
bot.run(jeton)

