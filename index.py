import discord
from discord.ext import commands

TOKEN = open('token.txt', 'r').readline()
client = commands.Bot(command_prefix='mon ')

client.remove_command('help')
game = None


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
