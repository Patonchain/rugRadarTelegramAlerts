import requests
import time
import telegram
import asyncio

# Setup async event for the bot message
loop = asyncio.get_event_loop()
async def send_message_async(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)
# Set up your Telegram bot
bot = telegram.Bot(token='5873635459:AAEYVNTzVmIYPH0IMPIbo6E90PpNDBc-WMo')
# Set the API endpoint URL
api_url = 'https://server.rugradar.org/api/v1/token?limit=20'
# Get the chat ID from the user
chat_id = '@RugRadarAlerts'
# Initialize the "old" list
old_names = []
while True:
    # Call the API endpoint
    response = requests.get(api_url)
    # Get the list of names from the API response
    new_names = [item['name'] for item in response.json()['data']]
    print(new_names)
    # Compare the old and new lists
    if old_names:
        for item in response.json()['data']:
            if item['name'] not in old_names:
                # Build the message text
                text = f"SUS TOKEN! Be careful!\n"
                text += f"Name: {item['name']}\n"
                text += f"Contract address: {item['contract_address']}\n"
                text += f"Symbol: {item['symbol']}\n"
                text += f"Network: {item['chain']}\n"
                # Send the message
                loop.run_until_complete(send_message_async(chat_id, text))
    # Update the old list
    old_names = new_names
    # Wait 10 seconds before calling the API again
    time.sleep(10)