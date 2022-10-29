import disnake
from disnake.ext import commands

class kick(commands.Cog):
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

@commands.slash_command()
async def kick(self, inter, user: disnake.Member, delete: commands.Range[0,14] = 0, reason: str = "| None"):
    """
     kicks a user.
     Parameters
     ----------
     user: A user to kick; takes @.
     delete: How many days of message to delete. 0-14.
     reason: A reason to ban the user if there is one.
     """
    blankEmbed = disnake.Embed(
           colour = disnake.Colour.random())
    await inter.guild.kick(user, reason=f": {reason}", delete_message_days=delete)
    blankEmbed.title = "Ban Successful"
    blankEmbed.description = f"You have kicked {user.name} successfully."
    await inter.response.send_message(embed = blankEmbed)

def setup(bot):
    bot.add_cog(kick(bot))
    print("| kick - Loaded")
