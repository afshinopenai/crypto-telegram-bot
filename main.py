import os
import requests

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

message = "🚀 تست پیام ساده از GitHub به تلگرام"

url = f"https://api.telegram.org/bot{token}/sendMessage"
params = {"chat_id": chat_id, "text": message}

response = requests.get(url, params=params)

print("🔧 Status Code:", response.status_code)
print("🔧 Response Text:", response.text)
