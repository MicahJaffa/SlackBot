import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


app = App(token=os.environ["SLACK_BOT_TOKEN"])

CHANNEL_ID = "C0C0H887J5A"

def send_greeting():
    app.client.chat_postMessage(channel=CHANNEL_ID, text="Hi")

if __name__ == "__main__":
    send_greeting()
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()