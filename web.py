from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def keep_alive():
    app.run(host='0.0.0.0', port=8080)

# To keep the server alive, you can use threading
def run():
    threading.Thread(target=keep_alive).start()
