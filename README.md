# Focus Route iOS

## Build 8

設定に「集中画面の表示」を追加しました。
「タスクに集中」「ルートを見渡す」「切り替えて使う」から選択でき、
表示を切り替えてもタイマーと進捗は継続します。
詳しくは `BUILD8_FOCUS_DISPLAY.md` を確認してください。

## Build 7

でんしゃタイマー最新版から、記録の15件ページ表示、表示中記録の4指標まとめ、
記録編集画面の自動項目表示、記録内容の説明をFocus Route向けに移植しました。
詳しくは `BUILD7_RECORDS.md` を確認してください。

## Build 6

「もう1回分追加」後も円の分割数を増やさず、同じ円を新しいラウンドとして表示します。
タスク一覧の合算進捗は維持し、タイマー描画と端末保存の反復も削減しました。
詳しくは `BUILD6_REPEAT_CIRCLE.md` を確認してください。

## Build 5

タスク完了画面へ「＋ もう1回分追加」を追加し、完了時の操作レイアウトを整理しました。
追加分は同じ時間・ステップ数で開始され、10秒間は元に戻せます。
詳しくは `BUILD5_REPEAT_TASK.md` を確認してください。

## Build 4

「記録を編集」の実施日を、締切と同じ日付表示カードへ統一しました。
選択した日付と曜日がiPhone・iPadでも常に文字で確認できます。
詳しくは `BUILD4_DATE_DISPLAY.md` を確認してください。

## Build 3

「前のタスク」「次のタスク」で、現在のタスクを「保留」または「完了」にしてから移動できるようにしました。
移動後10秒間は「元に戻す」で、移動前の進捗と記録を復元できます。
詳しくは `BUILD3_TASK_MOVE.md` を確認してください。

## Build 2

記録の絞り込み・編集・削除、カレンダー日付選択、JSONバックアップ、PDF保存、
画面スリープ防止、初回案内、動きを少なくする設定、iOSネイティブ振動を追加しました。

通知方法は「音」「振動」「音と振動」「通知しない」から選べます。
詳しくは `BUILD2_FEATURES.md`、Codespacesでの展開方法は `CODESPACES_UNZIP.md` を確認してください。

仕事をタスクとステップに分け、円形タイマーでゴールまで進めるiPhone・iPad向けアプリです。

## 構成

- Web UI: `www/index.html`
- Capacitor設定: `capacitor.config.json`
- iOSプロジェクト: `ios/App/App.xcodeproj`
- Bundle ID: `works.psychcraft.focusroute`
- Scheme: `App`
- Marketing Version: `1.0`
- Build Number: `8`

## 再利用したiOS機能

- Capacitor 8のiOSコンテナ
- Codemagicによる署名付きIPA生成
- iPhone・iPad対応
- AVAudioSessionを使ったネイティブ通知音
- WebViewとネイティブ間の音声ブリッジ

## ローカル確認

```bash
npm install
npx cap sync ios
```

Macがない場合はGitHubへ配置し、Codemagicの`ios-capacitor-check`で同期確認後、
`ios-ipa-build`でIPAを作成します。

## App Store Connect

でんしゃタイマーとは別アプリのため、App Store Connectで以下を新規作成してください。

- アプリ名: Focus Route
- Bundle ID: `works.psychcraft.focusroute`
- SKU: 任意の重複しない値

CodemagicのApp Store Connect APIキー連携は、既存の`denshatimer`連携を同じ開発者アカウントで再利用できます。
