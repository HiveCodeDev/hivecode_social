// Records a scripted walk through the live site as a 1080x1920 screencast.
// usage: node tools/record.mjs <out-dir>   (writes frames/*.jpg + frames.txt for ffmpeg concat)
import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";

const out = resolve(process.argv[2]);
const framesDir = join(out, "frames");
mkdirSync(framesDir, { recursive: true });
const SITE = process.env.SITE ?? "https://www.hivecode.pt";

const edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const port = 9800 + Math.floor(Math.random() * 150);
const proc = spawn(edge, [
  "--headless=new",
  `--remote-debugging-port=${port}`,
  "--hide-scrollbars",
  "--window-size=540,960",
  `--user-data-dir=${process.env.TEMP}\\edge-rec-${port}`,
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
const frames = [];
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    pending.get(msg.id)(msg);
    pending.delete(msg.id);
  } else if (msg.method === "Page.screencastFrame") {
    const { data, metadata, sessionId } = msg.params;
    frames.push({ data, t: metadata.timestamp });
    ws.send(JSON.stringify({ id: ++id, method: "Page.screencastFrameAck", params: { sessionId } }));
  }
});
const send = (method, params = {}) =>
  new Promise((done) => {
    const n = ++id;
    pending.set(n, done);
    ws.send(JSON.stringify({ id: n, method, params }));
  });
const js = (expression) => send("Runtime.evaluate", { expression, awaitPromise: true });

await send("Page.enable");
await send("Page.bringToFront");
await send("Emulation.setFocusEmulationEnabled", { enabled: true });
await send("Emulation.setDeviceMetricsOverride", { width: 540, height: 960, deviceScaleFactor: 2, mobile: true });
await send("Network.enable");
await send("Network.setUserAgentOverride", {
  userAgent:
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
});
// Warm the cache so the recording does not show loading.
await send("Page.navigate", { url: SITE });
await sleep(6000);
await send("Page.navigate", { url: "about:blank" });
await sleep(500);

console.log("start:", JSON.stringify(await send("Page.startScreencast", { format: "jpeg", quality: 90, maxWidth: 1080, maxHeight: 1920, everyNthFrame: 1 })));
await send("Page.navigate", { url: SITE });
await sleep(5200); // opening curtain + hero devices
console.log("frames after load:", frames.length);
const smooth = (y, ms) =>
  js(`new Promise(r=>{const s=scrollY,d=${y}-s,t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/${ms});
  const e=1-Math.pow(1-p,4);scrollTo(0,s+d*e);p<1?requestAnimationFrame(f):r(true)};requestAnimationFrame(f)})`);
await smooth(900, 1600);
await sleep(900);
await smooth(1900, 1600);
await sleep(900);
await smooth(0, 1000);
await sleep(400);
await js(`document.querySelector('a[href="/business"]').click()`);
await sleep(3600); // curtain + business hero
await smooth(800, 1400);
await sleep(1600); // chaos -> order
await js(`document.querySelector('a[href="/contacto"]').click()`);
await sleep(4200); // curtain + contact hero
await send("Page.stopScreencast");
await sleep(300);

const lines = [];
frames.forEach((f, i) => {
  const name = `f${String(i).padStart(5, "0")}.jpg`;
  writeFileSync(join(framesDir, name), Buffer.from(f.data, "base64"));
  const next = frames[i + 1];
  lines.push(`file 'frames/${name}'`, `duration ${next ? (next.t - f.t).toFixed(4) : "0.5"}`);
});
lines.push(`file 'frames/f${String(frames.length - 1).padStart(5, "0")}.jpg'`);
writeFileSync(join(out, "frames.txt"), lines.join("\n"));
console.log(`${frames.length} frames, ${(frames.at(-1).t - frames[0].t).toFixed(1)}s`);
ws.close();
proc.kill();
