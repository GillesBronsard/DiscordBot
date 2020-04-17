import discord #pip install discord
from notOnGit import laCleSecrete #le token est dans un fichier à part et ignoré par github

# creer une nouvelle instance de notre bot
bot = discord.Client()

#detecter quand le bot est ON
@bot.event
async def on_ready():
	print("Bot ready !")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Gilles est en ligne"))
#donner le jeton pour qu'il se connecte
jeton = laCleSecrete

#test
print('Test')

#connecter au serveur
bot.run(jeton)

