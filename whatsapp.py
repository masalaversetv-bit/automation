# whatsapp.py
import os
import requests
import json

PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_PERMANENT_TOKEN")
TO_NUMBER = os.getenv("WHATSAPP_TO_NUMBER")  # Format: 91xxxxxxxxxx

def send_whatsapp_text(message):
    url = f"https://graph.facebook.com/v18.0/{PHONE_ID}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": TO_NUMBER,
        "type": "text",
        "text": {"body": message}
    }

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    try:
        return response.json()
    except:
        return {"error": "Invalid response", "text": response.text}
