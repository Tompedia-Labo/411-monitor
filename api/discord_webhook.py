import os
import requests
from config import Config

URL = Config.DISCORD_WEBHOOK_URL

def send_discord_message(content: str, username: str = "411-alert") -> bool:
    """
    Discordのチャンネルに411の状況報告をする関数
    """
    if not URL:
        print("Error: DISCORD_WEBHOOK_URLが設定されていません。")
        return False

    payload = {
        "content": content,
        "username": username
    }

    try:
        response = requests.post(URL, json=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Discord Webhook送信エラー: {e}")
        return False
