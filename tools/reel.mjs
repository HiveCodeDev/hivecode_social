// Renders an animated reel page frame by frame (no screen recording, so no dropped frames).
// The page must expose window.seek(seconds) that draws the exact state at that time.
// usage: node tools/reel.mjs <reel.html> <frames-dir> <seconds> [fps=30]
import { spawn } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const [html, dir, seconds, fpsArg] = process.argv.slice(2);
const fps = Number(fpsArg || 30);
const frames = Math.ceil(Number(seconds) * fps);
const out = resolve(dir);
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });

const edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const port = 9400 + Math.floor(Math.random() * 400);
const proc = spawn(edge, [
  "--headless=new",
  `--remote-debugging-port=${port}`,
  "--hide-scrollbars",
  "--allow-file-access-from-files",
  "--window-size=1080,1920",
  `--user-data-dir=${process.env.TEMP}\\edge-reel-${port}`,
  "about:blank",
]);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

let targets;
for (let i = 0; i < 40; i++) {
  try {
    targets = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    if (targets.some((t) => t.type === "page")) break;
  } catch {}
  await sleep(250);
}
const ws = new WebSocket(targets.find((t) => t.type === "page").webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener("open", r, { once: true }));
let id = 0;
const pending = new Map();
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    pending.get(msg.id)(msg);
    pending.delete(msg.id);
  }
});
const send = (method, params = {}) =>
  new Promise((done) => {
    const n = ++id;
    pending.set(n, done);
    ws.send(JSON.stringify({ id: n, method, params }));
  });

await send("Page.enable");
await send("Emulation.setDeviceMetricsOverride", { width: 1080, height: 1920, deviceScaleFactor: 1, mobile: false });
await send("Page.navigate", { url: pathToFileURL(resolve(html)).href });
await sleep(1500);
await send("Runtime.evaluate", { expression: "document.fonts.ready.then(() => true)", awaitPromise: true });

for (let f = 0; f < frames; f++) {
  await send("Runtime.evaluate", { expression: `window.seek(${f / fps})` });
  const shot = await send("Page.captureScreenshot", {
    format: "jpeg",
    quality: 92,
    clip: { x: 0, y: 0, width: 1080, height: 1920, scale: 1 },
  });
  writeFileSync(join(out, `${String(f).padStart(5, "0")}.jpg`), Buffer.from(shot.result.data, "base64"));
  if (f % fps === 0) process.stdout.write(`${f / fps}s `);
}
console.log(`\n${frames} frames`);
ws.close();
proc.kill();
