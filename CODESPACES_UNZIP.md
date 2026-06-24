# GitHub Codespacesでの展開手順

## 1. ZIPをCodespacesへアップロード

Codespacesの左側にあるExplorerへ、ZIPファイルをドラッグします。

## 2. ZIPを展開

ZIPが `/workspaces/focus-route-ios/focus-route-ios-build9-full-20260625.zip` にある場合:

```bash
cd /workspaces/focus-route-ios
unzip -o focus-route-ios-build9-full-20260625.zip
cd focus-route-ios-build9-route-editor-ux-20260625
```

既存リポジトリのルートへ内容を反映する場合は、いったん展開してからコピーします。

```bash
cd /workspaces/focus-route-ios
unzip -o focus-route-ios-build9-full-20260625.zip
cp -a focus-route-ios-build9-route-editor-ux-20260625/. .
```

## 3. GitHubへ反映

新しいリポジトリで使用する場合:

```bash
git init
git add .
git commit -m "Implement Focus Route iOS build 9"
git branch -M main
git remote add origin https://github.com/ユーザー名/リポジトリ名.git
git push -u origin main
```

既存のFocus Routeリポジトリへ上書き展開した場合:

```bash
git status
git add .
git commit -m "Improve route editor UX"
git push
```

## 4. 検証

```bash
npm ci
npm run validate
npx cap sync ios
```

## 5. Codemagic

1. `ios-capacitor-check`を実行
2. 成功後に`ios-ipa-build`を実行
3. App Store ConnectでBuild 9を選択
