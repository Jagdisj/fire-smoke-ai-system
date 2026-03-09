import requests
import json
import time

BOT_TOKEN = "8174249575:AAFuE_qwKqy9kaMyQ5BNcDrvu7sMaE6bfpI"

def load_users():

    try:
        with open("users.json","r") as f:
            return json.load(f)
    except:
        return []

def save_users(users):

    with open("users.json","w") as f:
        json.dump(users,f)

offset = None

while True:

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

    if offset:
        url += f"?offset={offset}"

    response = requests.get(url).json()

    for result in response["result"]:

        offset = result["update_id"] + 1

        chat_id = result["message"]["chat"]["id"]
        text = result["message"].get("text","")

        if text == "/start":

            users = load_users()

            if chat_id not in users:

                users.append(chat_id)
                save_users(users)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "✅ You are registered for AI Fire Monitoring Dashboard"
                }
            )

    time.sleep(2)