import disnake
from disnake.ext import commands
from deta import Deta
from dotenv import load_dotenv


class Ban(commands.Cog):
    
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
    
    @commands.slash_command()
    async def ban(self, inter, user: disnake.User, delete: commands.Range[0,14] = 0, reason: str = "| None"):
        """
        Bans a user.
        Parameters
        ----------
        user: A user to ban; takes @ and ID.
        delete: How many days of message to delete. 0-14.
        reason: A reason to ban the user if there is one.
        """
        blankEmbed = disnake.Embed(
            colour = disnake.Colour.random())
        
        if inter.author.top_role < user.top_role:
            blankEmbed.title = "Ban Failed: Hierarchy"
            blankEmbed.description = "Your role is lower than the target; get a role higher than the target."
            return await inter.response.send_message(embed = blankEmbed)
            
        if inter.guild.me.top_role < user.top_role:
            blankEmbed.title = "Ban Failed: Hierarchy"
            blankEmbed.description = "My role is lower than the target; raise my role or lower theirs."
            return await inter.response.send_message(embed = blankEmbed)
            
        if not inter.author.guild_permissions.ban_members:
            blankEmbed.title = "Ban Failed: Permissions"
            blankEmbed.description = "You don't have the `Ban Members` permission; get that and try again."
            return await inter.response.send_message(embed = blankEmbed)
            
        if not inter.guild.me.guild_permissions.ban_members:
            blankEmbed.title = "Ban Failed: Permissions"
            blankEmbed.description = "I don't have the `Ban Members` permission; give me that and try again."
            return await inter.response.send_message(embed = blankEmbed)
            
        if user.id == inter.author.id:
            blankEmbed.title = "Ban Failed: That's You!"
            blankEmbed.description = "That's You! You can't ban yourself; just leave the server."
            blankEmbed.add_field(
                name = "You're Dumb.",
                value = "<a:A_peepoleave:766815761100046386>"
                )
            return await inter.response.send_message(embed = blankEmbed)
            
        if user.id == inter.guild.me.id:
            blankEmbed.title = "Ban Failed: That's Me!"
            blankEmbed.description = "You can't ban me (at least not through me); just ban me manually or with a bot."
            return await inter.response.send_message(embed = blankEmbed)
        
        await inter.guild.ban(user, reason=f": {reason}", delete_message_days=delete)
        blankEmbed.title = "Ban Successful"
        blankEmbed.description = f"You have banned {user.name} successfully."
        await inter.response.send_message(embed = blankEmbed)
    
def setup(bot):
    bot.add_cog(Ban(bot))
    print("| Ban - Loaded")