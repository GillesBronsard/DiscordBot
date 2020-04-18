import discord #pip install discord
from notOnGit import laCleSecrete #le token (Module ignoré par github)
from discord.utils import get

#ajouter un composant de discord.py
from discord.ext import commands

# creer une nouvelle instance de notre bot
bot = commands.Bot(command_prefix='!')

#detecter quand le bot est ON
@bot.event
async def on_ready():
	print("Bot ready !")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Gilles est en ligne"))

#detecter quand quelqu'un ajoute un emoji sur un msg
@bot.event
async def on_raw_reaction_add(payload):
	#recupere l'emoji
	emoji = payload.emoji.name
	#recupere le numero du canal
	canal = payload.channel_id
	#recupere le numero du message
	message = payload.message_id
	
	python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
	membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

	#recupere le numero du serveur
	server = payload.guild_id
	#verifier si l'emoji qu'on a ajoutée est "python"
	if canal == 700785659295694919 and message == 700786866924028047 and emoji == "python":
		print("Grade ajouté !")
		await membre.add_roles(python_role)
		await membre.send("Tu obtiens le grade Python !")

#detecter quand quelqu'un supprime l'emoji sur le msg
@bot.event
async def on_raw_reaction_remove(payload):
	#recupere l'emoji
	emoji = payload.emoji.name
	#recupere le numero du canal
	canal = payload.channel_id
	#recupere le numero du message
	message = payload.message_id

	python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
	membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

	#verifier si l'emoji qu'on a ajoutée est "python"
	if canal == 700785659295694919 and message == 700786866924028047 and emoji == "python":
		print("Grade supprimé !")
		await membre.remove_roles(python_role)
		await membre.send("Tu perds le grade Python !")

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


#connection au serveur avec le jeton situé dans un fichier à part ignoré par Github
bot.run(laCleSecrete)

