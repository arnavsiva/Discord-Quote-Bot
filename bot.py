import discord
from discord.ext import commands
import aiohttp

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot is online and logged in as {bot.user.name}')

@bot.command()
async def quote(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://zenquotes.io/api/random") as response:
                if response.status == 200:
                    data = await response.json()
                    quote = data[0]['q']
                    author = data[0]['a']
                    
                    embed = discord.Embed(title="Quote", description=quote, color=discord.Color.blue())
                    embed.set_footer(text=f"- {author}")
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Failed to fetch a quote. Please try again later.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    print(f"Error: {error}")

    error_message = "An error occurred while executing the command."
    await ctx.send(error_message)

bot.run('YOUR BOT TOKEN HERE') #replace with your bot token inside the quotes