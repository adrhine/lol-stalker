import os
import util

from dotenv import load_dotenv
from riot_wrapper import riot_fetcher
from stalker_bot import discord_bot

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
api_key = os.getenv('API_KEY')

bot = discord_bot(command_prefix = '.')
fetcher = riot_fetcher(api_key)
champions = util.championBootstrap()

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

@bot.command(name = 'matches', help = 'Get Match History for this guy')
async def summoner_match_history(ctx, summoner_name):
	summoner = fetcher.get_summoner(summoner_name)
	match_history = fetcher.get_match_history(summoner)
	for match in match_history:
		summoner.add_match(champions, match)

	response = "Summoner {summoner_name} has played".format(summoner_name = summoner_name)
	for champion_id, match_entry in summoner.champ_history:
		response = response + "\n" + str(match_entry)
	await ctx.send(response)

bot.run(token)