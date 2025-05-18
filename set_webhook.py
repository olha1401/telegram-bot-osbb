import requests

BOT_TOKEN = "7548597124:AAFnT4qW4sL2jCnQrDf1tiQs1F61yqpdeRw"
WEBHOOK_URL = f"https://telegram-bot-osbb.onrender.com/webhook/{BOT_TOKEN}"

response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(response.json())
