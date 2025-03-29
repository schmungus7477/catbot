TOKEN = ""  

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author != client.user:  # Ignore messages from others
        return

    if message.content.lower() == "!meow":
        # Make a GET request to TheCatAPI to fetch a random cat image
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        
        if response.status_code == 200:
            data = response.json()  # Parse the response as JSON
            cat_image_url = data[0]["url"]  # Extract the image URL from the response
            
            # Send the image URL as a message (this will display the image as an embed)
            await message.channel.send(cat_image_url)

client.run(TOKEN)