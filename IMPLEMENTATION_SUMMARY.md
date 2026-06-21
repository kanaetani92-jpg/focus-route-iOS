# Focus Route iOS 実装内容

## アプリ識別情報

- アプリ名：Focus Route
- Bundle ID：`works.psychcraft.focusroute`
- バージョン：`1.0`
- ビルド番号：`1`
- 対応端末：iPhone / iPad

でんしゃタイマーとは別アプリとして、App Store Connectに新規登録する構成です。

## Focus Routeから移植した内容

- 今日のルート
- 円形の分割タイマー
- タスク・ステップ編集
- タスクごとの途中位置保存と再開
- 前のタスク・次のタスクへの移動
- 進んだ記録の5表示
- 到着したルート
- ルートの複製・保管・再利用
- 締切と曜日表示
- 端末内保存

## でんしゃタイマーから再利用した内容

- Capacitor 8のiOSプロジェクト
- CodemagicのIPA生成フロー
- iPhone・iPadの画面回転設定
- AVAudioSessionを利用したネイティブ通知音
- WebViewとSwift間の音声ブリッジ

## iOS専用対応

- Focus Route専用アイコン
- Focus Route専用スプラッシュ画面
- アプリ内プライバシーポリシー
- Web Audioが利用できない場合のネイティブ音声フォールバック
- iOS復帰後も端末時刻から経過時間を補正

## Codemagicでの確認順

1. このフォルダを新しいGitHubリポジトリへ配置する
2. App Store ConnectでBundle ID `works.psychcraft.focusroute`を登録する
3. App Store Connectで新しいアプリ「Focus Route」を作成する
4. Codemagicでリポジトリを追加する
5. `ios-capacitor-check`を実行する
6. 成功後、`ios-ipa-build`を実行する

既存のCodemagic App Store Connect連携名`denshatimer`は、同じApple DeveloperアカウントのAPIキー連携として再利用できます。

## 検証済み項目

- Focus RouteのHTML・JavaScript構文
- `www`とXcode `public`の一致
- Bundle IDと表示名
- Xcodeのバージョン・ビルド番号
- Codemagic設定
- アプリアイコンと起動画面の画像サイズ
- ネイティブ音声ブリッジ
- プライバシーポリシー同梱

この実行環境にはXcodeとSwiftがないため、最終的な署名付きIPAの生成はCodemagicで行います。
