import os
import util

from riot_wrapper import riot_fetcher
from stalker_bot import discord_bot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
api_key = os.getenv('API_KEY')

bot = discord_bot(command_prefix = '.')
fetcher = riot_fetcher(api_key)

@bot.command(name = 'levels', help = 'Get combined total of all Champion Levels')
async def champion_levels(ctx, summoner_name):
	mastery_response = fetcher.get_mastery_response(summoner_name)

	total_champion_levels = util.parse_mastery_response(mastery_response, 'championLevel')

	response = '{} has {} Combined Champion Levels!'.format(summoner_name, total_champion_levels)
	await ctx.send(response)

@bot.command(name = 'points', help = 'Get combined total of all Champion Mastery Points')
async def champion_mastery_points(ctx, summoner_name):
	mastery_response = fetcher.get_mastery_response(summoner_name)

	total_champion_points = util.parse_mastery_response(mastery_response, 'championPoints')
	
	response = '{} has {} Combined Champion Mastery Points!'.format(summoner_name, total_champion_points)
	await ctx.send(response)

bot.run(token)