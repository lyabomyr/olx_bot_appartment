import requests

def send_to_telegram(message: str, telegram_bot_token: str, telegram_chat_id: str) -> None:
    telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    response = requests.post(telegram_api_url, data=payload)

    if response.status_code == 200:
        print("Message sent to Telegram successfully")
    else:
        raise Exception(f"Failed to send message to Telegram with error {response.text}")