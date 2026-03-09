import requests

BOT_TOKEN = "8174249575:AAFuE_qwKqy9kaMyQ5BNcDrvu7sMaE6bfpI"
CHAT_ID = "1794397732"


def send_telegram_alert(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)