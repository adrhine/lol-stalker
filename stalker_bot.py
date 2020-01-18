from discord.ext import commands

class discord_bot(commands.Bot):
	# bot is ready
	async def on_ready(self):
	    try:
	        print(self.user.name)
	        print(self.user.id)
	    except Exception as e:
	        print(e)