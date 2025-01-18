import sys
import requests

# Configuration
BOT_TOKEN = "Ton bot token"
CHANNEL_ID = "Ton channel ID"

def send_message(message):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"content": message}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Message envoyé avec succès !")
    else:
        print(f"Erreur lors de l'envoi : {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
        send_message(message)
    else:
        print("Aucun message fourni.")
