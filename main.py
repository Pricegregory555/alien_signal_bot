import os
import telebot
from flask import Flask, request

app = Flask(__name__)

# Токен бота и чат ID
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data:
        # Обрабатываем данные, например, отправляем сообщение в чат
        bot.send_message(CHAT_ID, f"Новый сигнал: {data}")
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
