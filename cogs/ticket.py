import discord
from discord.ext import commands
from discord.ui import Button, View

class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.green, custom_id="open_ticket")
    async def ticket_callback(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        user = interaction.user
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            user: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(name=f"ticket-{user.name}", overwrites=overwrites)

        await interaction.response.send_message(f"Your ticket has been created: {channel.mention}", ephemeral=True)

class TicketCog(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        embed = discord.Embed(
            title="🛠️ Support Desk",
            description="Need help? Click the button below to open a private ticket.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed, view=TicketView())

async def setup(bot):
    await bot.add_cog(TicketCog(bot))