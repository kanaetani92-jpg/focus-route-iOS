import { readFile, stat } from "node:fs/promises";

const files = {
  web: "www/index.html",
  publicWeb: "ios/App/App/public/index.html",
  capacitor: "capacitor.config.json",
  iosCapacitor: "ios/App/App/capacitor.config.json",
  plist: "ios/App/App/Info.plist",
  project: "ios/App/App.xcodeproj/project.pbxproj",
  appDelegate: "ios/App/App/AppDelegate.swift",
  icon: "ios/App/App/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png",
};

const contents = Object.fromEntries(
  await Promise.all(
    Object.entries(files).map(async ([key, path]) => [key, await readFile(path, key === "icon" ? null : "utf8")]),
  ),
);

const requireText = (key, needle) => {
  if (!contents[key].includes(needle)) {
    throw new Error(`${files[key]} is missing: ${needle}`);
  }
};

requireText("web", "<title>Focus Route</title>");
requireText("web", "今日、どこまで進みますか");
requireText("web", "到着したルート");
requireText("web", "NativeAudioMode");
requireText("publicWeb", "<title>Focus Route</title>");
requireText("capacitor", "works.psychcraft.focusroute");
requireText("capacitor", '"appName": "Focus Route"');
requireText("iosCapacitor", "works.psychcraft.focusroute");
requireText("plist", "<string>Focus Route</string>");
requireText("project", "PRODUCT_BUNDLE_IDENTIFIER = works.psychcraft.focusroute;");
requireText("project", "CURRENT_PROJECT_VERSION = 3;");
requireText("appDelegate", "NativeAudioModePlugin");
requireText("appDelegate", "NativeHapticEngine");
requireText("appDelegate", "Focus Route 進んだ記録");
requireText("web", "バックアップを書き出す");
requireText("web", "playTaskHaptic");
requireText("web", "保留にして移動");
requireText("web", "undo-task-move");

if (contents.web !== contents.publicWeb) {
  throw new Error("www/index.html and ios/App/App/public/index.html are not synchronized");
}

const icon = await stat(files.icon);
if (icon.size < 5000) {
  throw new Error("App icon appears to be invalid");
}

console.log("Focus Route iOS assets and configuration are valid");
