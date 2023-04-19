import os
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# bot tokenとsocketmode handlerを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
# mentionが来たら、ChatGPTサーバに送り、返答を貰う
def message_mention(event, say):
  try:
    server_url = os.environ.get("SERVER_URL")
    server_port = os.environ.get("SERVER_PORT")
    url = f'{server_url}:{server_port}/q/' + event["text"]
    # url = 'http://localhost:8000/q/' + event["text"]
    response = requests.get(url)
    # 問題が無ければ、jsonを取得
    if response.status_code == 200:
      json = response.json()

    say(json['answer'])
  except Exception as e:
    say("Some error occurred." + str(e))

@app.event("message")
def handle_message_events(body, logger):
  logger.info(body)

# アプリを起動します
if __name__ == "__main__":
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
