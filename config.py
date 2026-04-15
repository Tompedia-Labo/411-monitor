import os
from dotenv import load_dotenv
from models import CameraAuth

load_dotenv(".env")

class Config:
    # Camera
    CAMERA_N = int(os.getenv("CAMERA_N"))
    CAMERAS = []
    for i in range(1, CAMERA_N+1):
        CAMERAS.append(CameraAuth(
            url=os.getenv(f"CAMERA{i}_URI"),
            user=os.getenv(f"CAMERA{i}_USER"),
            password=os.getenv(f"CAMERA{i}_PWD")
        ))

    # Discord
    DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK")
