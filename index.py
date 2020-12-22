import discord
from discord.ext import commands

TOKEN = open('token.txt', 'r').readline()
client = commands.Bot(command_prefix='mon ')

client.remove_command('help')
game = None


class Monopoly(object):

    def __init__(self, n_players):

        self.player_cash = [1500] * n_players
        self.player_locations = [0] * n_players  # 0 --> 40
        self.properties_owned = [[]] * n_players
        """
        represented by tuple with: 
         - strings (e.g `lb1` for Light Blue 1)
         - houses purchased (hotel = 5 houses)
        """
        self.in_jail = [False] * n_players


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed()
    embed.title = 'Help/About'
    embed.add_field(name='start', value='Create a game.', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def start(ctx):

    pass

client.run(TOKEN)
