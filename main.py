import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import platform 
import time

load_dotenv()

token = os.environ["token"]
# os.system("color")

bot = commands.InteractionBot(
    intents = disnake.Intents.all(),
    test_guilds = [
        1028690023207424001, #overwatch commune
        951289542684590140 #players projects
        ],
    reload = True)

print(f"\x1B[1;4mnamehere\x1B[0m \n")
print("Presented by Player1041 and SmU.")
print(f"\n\x1B[1;4mCommands\x1B[0m \n")
bot.load_extensions("commands")

@bot.event
async def on_ready():
    print(f"\n\x1B[1;4mStats\x1B[0m \n")
    print(f"| Name: {bot.user}")
    print(f"| ID: {bot.user.id}")
    print(f"| Latency: {round(bot.latency * 1000)}ms")
    print(f"| Server Count: {len(bot.guilds)}")
    print(f"| Total Users: {len(bot.users)}")
    print(f"| Disnake Version: {disnake.__version__}")
    print(f"| Python Version: {platform.python_version()}")

bot.run(token)