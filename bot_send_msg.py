import requests
import json

# 从 Config 文件中导入 Telegram Bot API token 和 频道 ID
from config_bot import BOT_CONFIG

def telegram_send_message(text):
    
    token = BOT_CONFIG["BOT_TOKEN"]
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    
    payload = {
        "chat_id": BOT_CONFIG["Id_user"],
        "text": text
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.json())

if __name__ == '__main__':
    # 发送消息
    message = "Hello, this is!"
    telegram_send_message(message)

