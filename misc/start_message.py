import requests

from config import bot_token, whitelisted_id


message = "PC Started"
def sendmsg(): requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={whitelisted_id}&text={message}")