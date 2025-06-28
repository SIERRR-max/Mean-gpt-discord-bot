import discord
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!mean"):
        prompt = message.content[6:].strip()

        rude_prompt = f"""You're a mean, sarcastic AI. Roast the user in a funny way. Don't be hateful or offensive. Just sassy and witty.
User: {prompt}
MeanGPT:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": rude_prompt}]
            )
            roast = response.choices[0].message.content.strip()
            await message.channel.send(roast)

        except Exception as e:
            await message.channel.send("Oops. My roast engine failed.")
            print(e)

client.run(DISCORD_BOT_TOKEN)
