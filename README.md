# ChatGPT Request Server and Slack bot

## 環境変数の設定

### Server用環境変数
環境変数 OPENAI_API_KEY に ChatGPT の API_KEY を設定する
```shell
例：
$ export OPEN_API_KEY="sk-1234567890abcdefghijklmnopqrstuvwxyz"
```
### Slack bot用
SLACK_BOT_TOKEN、 SLACK_APP_TOKEN の二つの環境変数を設定する。
#### SLACK_APP_TOKEN
https://api.slack.com/apps から登録したアプリを選択し、Basic Infomationにある、App-Level Token で設定していたtokenを取得する。
#### SLACK_BOT_TOKEN
次は左メニューの OAuth & Permissions から、OAuth Tokens for Your Workspace にある、Bot User OAuth Token からtokenを取得する。


```shell
例：
$ export SLACK_APP_TOKEN=xapp-9-abcdefghijklmnopqrstuvwxyzabcdefghijklmno-opqrstuvwxyz

$ export SLACK_BOT_TOKEN=xoxb-1234567890-0987654321-abcdefghijklmnopq
```

その後、`$ docker compose up`で起動し、8000ポートで待機します。

## PortなどURLを変更したい場合
必要に応じて、./bot/Dockerfile, ./server/Dockerfile や、docker-compose.ymlのポートを変更して下さい。

## botの使い方
登録したWorkspaceの使いたいチャンネルの設定を開き、インテグレーションタブからAppグループの、アプリを追加するで、使いたいチャンネルに追加されます。その後、botに向かってChatGPTに聞きたい事をmentionで指定して下さい
