import disnake
from disnake.ext import commands

class members(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

@bot.slash_command(description='how many members do you think you have?')
async def members(inter):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
    )
    
def setup(bot):
    bot.add_cog(members(bot))
    print("| members command - Loaded")
