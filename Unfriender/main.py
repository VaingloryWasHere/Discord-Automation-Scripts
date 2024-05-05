import selfcord as discord
from selfcord.ext import commands
import asyncio
import sys

bot = commands.Bot(command_prefix=";;;", self_bot=True)


TOKEN = sys.argv[1] #token


# attack!
@bot.event
async def on_ready():
    index = 1
    game = discord.Game("with the API")
    await bot.change_presence(activity=game)
    print("Bot initialised. Beginning attack.")
    original_friends = len(bot.friends)
    for relationship in bot.friends:
        try:
            await relationship.delete()
            print(f"-1 Removed")
            index += 1
        except:
            print(f"IGNORING EXCEPTION WITH USER")
            pass

    print(f"JOB COMPLETE! {index} users have been removed from the friend list, {original_friends} originally!")
    await bot.close()


bot.run(token=TOKEN)
print("BOT CLOSED.")