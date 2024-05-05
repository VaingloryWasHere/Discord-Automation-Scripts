import selfcord as discord
from selfcord.ext import commands
import asyncio
import sys
import sys
bot = commands.Bot(command_prefix=";;;", self_bot=True)


TOKEN = sys.argv[1]


# attack!
@bot.event
async def on_ready():
    game = discord.Game("with the API")
    await bot.change_presence(activity=game)

    print("Bot initialised. Beginning attack.")

    index = 0

    # async for message in channel.history(limit=None):
    #     if message.author == bot.user:
    #         await message.delete()
    #         await asyncio.sleep(0.7) #Must avoid rate limiting.
    #         print("-1")
    print(len(bot.guilds))
    for server in bot.guilds:
        try:
            await server.leave()
            index += 1
            print(index)
            asyncio.sleep(3)
        except:
            pass


    print("JOB COMPLETE!")
    await bot.close()


bot.run(token=TOKEN)
