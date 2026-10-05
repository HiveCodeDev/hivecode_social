// Renders one HTML file to a JPEG of the given size with the local Edge.
// usage: node tools/render_one.mjs <in.html> <out.jpg> <width> <height>
import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const [input, output, w = "1080", h = "1920"] = process.argv.slice(2);
const width = Number(w);
const height = Number(h);
const edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const port = 9960 + Math.floor(Math.random() * 30);
const proc = spawn(edge, [
  "--headless=new",
  `--remote-debugging-port=${port}`,
  "--hide-scrollbars",
  "--allow-file-access-from-files",
  `--window-size=${width},${height}`,
  `--user-data-dir=${process.env.TEMP}\\edge-one-${port}`,
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
await send("Emulation.setDeviceMetricsOverride", { width, height, deviceScaleFactor: 1, mobile: false });
await send("Page.navigate", { url: pathToFileURL(resolve(input)).href });
await sleep(1500);
await send("Runtime.evaluate", { expression: "document.fonts.ready.then(() => true)", awaitPromise: true });
await sleep(300);
const shot = await send("Page.captureScreenshot", { format: "jpeg", quality: 92, clip: { x: 0, y: 0, width, height, scale: 1 } });
writeFileSync(resolve(output), Buffer.from(shot.result.data, "base64"));
ws.close();
proc.kill();
