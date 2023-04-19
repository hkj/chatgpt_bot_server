# ChatGPT Request Server and Slack bot

## 環境変数の設定

### .envファイルを作成
.env.exampleファイルを.envにリネームし
中にある環境変数を設定する。
```shell
OPENAI_API_KEY=
SLACK_APP_TOKEN=
SLACK_BOT_TOKEN=
SERVER_URL=
SERVER_PORT=
```

### OPENAI_API_KEY に ChatGPT の API_KEY を設定する

```shell
例：
OPENAI_API_KEY="sk-1234567890abcdefghijklmnopqrstuvwxyz"
```
### SLACK_APP_TOKEN
https://api.slack.com/apps から登録したアプリを選択し、Basic Infomationにある、App-Level Token で設定していたtokenを取得する。
### SLACK_BOT_TOKEN
次は左メニューの OAuth & Permissions から、OAuth Tokens for Your Workspace にある、Bot User OAuth Token からtokenを取得する。

```shell
例：
 SLACK_APP_TOKEN=xapp-9-abcdefghijklmnopqrstuvwxyzabcdefghijklmno-opqrstuvwxyz

SLACK_BOT_TOKEN=xoxb-1234567890-0987654321-abcdefghijklmnopq
```

### SERVER_URL, SERVER_PORTを設定する
```shell
例：
SERVER_URL=http://localhost
SERVER_PORT=8000
```

その後、`$ docker compose up`で起動し、8000ポートで待機します。

## botの使い方
登録したWorkspaceの使いたいチャンネルの設定を開き、インテグレーションタブからAppグループの、アプリを追加するで、使いたいチャンネルに追加されます。その後、botに向かってChatGPTに聞きたい事をmentionで指定して下さい
