import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
    # Camera

    # Discord
    DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK")
