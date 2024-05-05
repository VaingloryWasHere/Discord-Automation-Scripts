import selfcord as discord
from selfcord.ext import commands
import sys
bot = commands.Bot(command_prefix=";;;", self_bot=True)

def process_data():
	data = ['','','','']
	data[0] = sys.argv[1] #token
	data[1] = int(sys.argv[2]) #chatroom/ID
	data[2] = sys.argv[3] #messsage
	data[3] = int(sys.argv[4]) #repeat
	return data

# attack!
@bot.event
async def on_ready():
	print("Bot initialised.")

@bot.event
async def on_message(message):
	data = process_data()
	if message.author.id == bot.user.id and message.content == "start":
		chatroom = bot.get_channel(data[1])
		for member in chatroom.recipients:
			if member.id == bot.user.id:
				pass
			else:
				index = 0
				try:
					while index < data[3]:
						await member.send(data[2])
						print(f"Sent message to {member.name}. Repetition {index}")
						index += 1
				except: #Usually meaning the account has been deleted, could also be rate limitation, but selfcord would send the warning in that case.
					pass
		print("JOB COMPLETE!")

	else:
		return



bot.run(token=process_data()[0])
