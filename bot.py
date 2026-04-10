import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class TicketBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('cogs.ticket')


bot = TicketBot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'System Online: Logged in as {bot.user}')

bot.run(token)