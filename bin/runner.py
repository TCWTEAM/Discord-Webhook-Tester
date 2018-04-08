from discord_hooks import Webhook
import json

with open("config.json") as file:
    config = json.load(file)
    file.close()

url = config['url']

msg = Webhook(url, msg="Webhook Test \n \n Discord Webhook Tester By XO")
msg.post()
