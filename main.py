import discord
from discord.ext import commands
from config import Config


from config import Config
from api.discord_webhook import send_discord_message
from person_detect.detector import PersonDetector
from person_detect.rtsp_handler import RTSPStream
from person_detect.utils import draw_boxes
import cv2
import asyncio


intents = discord.Intents.default()
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


async def set_discordbot_custom_status(message: str):
    print(f"\n\n### change status to {message} ###\n\n")
    await bot.change_presence(activity=discord.Game(name=message), status=discord.Status.online)


async def send_discordbot_message(message: str):
    print(f"\n\n### send message: {message} ###\n\n")
    channel_id = Config.DISCORD_BOT_CHANNEL_ID
    channel = await bot.fetch_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        print("\n\n!!! No Channnel !!!\n\n")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    asyncio.create_task(monitor_loop())

async def monitor_loop():
    print("Loop start")
    stream = RTSPStream(Config.CAMERAS[0])
    detector = PersonDetector()
    count = 0
    await bot.wait_until_ready()
    print("bot is ready")
    try:
        while True:
            frame = stream.frame()
            if frame is None:
                continue

            boxes = detector.detect(frame)
            frame = draw_boxes(frame, boxes)

            cv2.putText(frame, f"People: {count}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow("411-monitor", frame)

            if count != len(boxes):
                count = len(boxes)
                # send_discord_message(f"411には{count}人います！")
                if count == 1:
                    # await send_discordbot_message("最初の一人がやってきました！")
                    print("")
                
                if count == 0:
                    # await set_discordbot_custom_status("誰もいません！")
                    # await send_discordbot_message("全員が退出しました。")
                    print("")
                else:
                    await set_discordbot_custom_status(f"在室人数: {count}人")
                    print(f"\n\n在室人数: {count}人\n\n")

                await asyncio.sleep(3)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    finally:
        stream.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(bot.start(Config.DISCORD_BOT_TOKEN))

