import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} hat sich eingeloggt und ist online!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "hey":
        await message.channel.send("Hallo")

    if message.content.lower() == "was":
        await message.channel.send("Deine Hose ist nass")









bot.run("TOKEN")