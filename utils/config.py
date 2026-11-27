import os

TOKEN = os.environ.get("TOKEN")
NAME = "Falcony"
server = "https://discord.com/invite/codexdev"
ch = "https://discord.com/channels/699587669059174461/1271825678710476911"
OWNER_IDS = [
    int(value.strip())
    for value in os.environ.get("OWNER_IDS", "").split(",")
    if value.strip().isdigit()
]
BotName = "Falcony"
serverLink = "https://discord.com/invite/codexdev"