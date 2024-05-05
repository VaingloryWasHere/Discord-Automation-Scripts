import selfcord as discord
from selfcord.ext import commands
import asyncio
import sys
bot = commands.Bot(command_prefix=";;;", self_bot=True)


TOKEN = sys.argv[1] #token
ID = int(sys.argv[2])
MESSAGE = sys.argv[3] #messsage
REPETITION = int(sys.argv[4]) #repeat


# attack!
@bot.event
async def on_ready():
    game = discord.Game("with the API")
    await bot.change_presence(activity=game)

    print("Bot initialised. Beginning attack.")
    user = bot.get_user(ID)
    channel = user.create_dm() #KIM:1142851870130446478

    index = 0

    # async for message in channel.history(limit=None):
    #     if message.author == bot.user:
    #         await message.delete()
    #         await asyncio.sleep(0.7) #Must avoid rate limiting.
    #         print("-1")

    while index != REPETITION:
        await asyncio.sleep(1.5)
        await channel.send(MESSAGE)
        index += 1

    print("JOB COMPLETE!")
    await bot.close()
    print("BOT CLOSED.")


bot.run(token=TOKEN)
