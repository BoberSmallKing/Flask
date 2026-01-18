import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat_page():
    return render_template('chat.html')

# Эндпоинт для обработки сообщений (опционально для будущего)
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    user_text = data.get("message")
    # Здесь можно подключить логику ИИ
    return jsonify({"status": "sent", "reply": f"Эхо: {user_text}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)