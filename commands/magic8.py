import disnake
from disnake.ext import commands
import random

class Magic8(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def magic8(self, inter, question: str):
        """Question the Magic 8 Ball.
        Parameters
        ----------
        question: What do you wish to ask?
        """
        
        responses = [
        "It is certain.",
        "It is decidedly so.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
        
        ]
        resp = random.choice(responses)
        aEmbed = disnake.Embed(
            title = f"{question.capitalize()}",
            description = f"**{resp}**"
            )
        await inter.response.send_message(embed = aEmbed)
        
def setup(bot):
    bot.add_cog(Magic8(bot))
    print("| Magic 8 - Loaded")