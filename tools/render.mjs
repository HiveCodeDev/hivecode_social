// Renders each posts/*/post.html to post.jpg (1080x1350, JPEG) with the local Edge.
// usage: node tools/render.mjs <week-folder>
import { spawn } from "node:child_process";
import { readdirSync, writeFileSync, existsSync } from "node:fs";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const week = resolve(process.argv[2]);
const edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const port = 9400 + Math.floor(Math.random() * 400);
const proc = spawn(edge, [
  "--headless=new",
  `--remote-debugging-port=${port}`,
  "--hide-scrollbars",
  "--allow-file-access-from-files",
  "--window-size=1080,1350",
  `--user-data-dir=${process.env.TEMP}\\edge-social-${port}`,
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
await send("Emulation.setDeviceMetricsOverride", { width: 1080, height: 1350, deviceScaleFactor: 1, mobile: false });

for (const day of readdirSync(week).sort()) {
  const html = join(week, day, "post.html");
  if (!existsSync(html)) continue;
  await send("Page.navigate", { url: pathToFileURL(html).href });
  await sleep(1500);
  await send("Runtime.evaluate", { expression: "document.fonts.ready.then(() => true)", awaitPromise: true });
  await sleep(300);
  const shot = await send("Page.captureScreenshot", {
    format: "jpeg",
    quality: 92,
    clip: { x: 0, y: 0, width: 1080, height: 1350, scale: 1 },
  });
  writeFileSync(join(week, day, "post.jpg"), Buffer.from(shot.result.data, "base64"));
  console.log("rendered", day);
}
ws.close();
proc.kill();
