// Publishes every approved post whose time has come, across all plans/*.json.
// usage: node tools/publish_due.mjs [--dry-run]
//
// Runs from GitHub Actions every 5 minutes in a self-restarting loop (.github/workflows/publish.yml), so the PC can be off.
// A post is due from 5 minutes before its Lisbon date/time until MAX_LATE hours after; older
// approved posts without media_id are reported but never published (safety against surprises).
// Each post goes through tools/publish.mjs, which skips anything that already has a media_id.
import { readdirSync, readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";

const MAX_LATE = 12;
const dryRun = process.argv.includes("--dry-run");

function lisbonInstant(date, time) {
  const guess = new Date(`${date}T${time}:00Z`);
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Lisbon", hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" })
      .formatToParts(guess).map((p) => [p.type, p.value]),
  );
  const shown = new Date(`${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}:00Z`);
  return new Date(guess.getTime() - (shown.getTime() - guess.getTime()));
}

if (dryRun) {  // check the token against the account (never printed)
  const v = process.env.INSTAGRAM_API_VERSION || "v26.0";
  const r = await (await fetch(`https://graph.facebook.com/${v}/${process.env.INSTAGRAM_ACCOUNT_ID}?fields=username`,
    { headers: { Authorization: `Bearer ${process.env.INSTAGRAM_ACCESS_TOKEN}` } })).json();
  console.log(r.username ? `token ok: @${r.username}` : `token FAILED: ${r.error?.message ?? "no answer"}`);
  if (!r.username) process.exit(1);
}

const now = Date.now(), due = [];
for (const file of readdirSync("plans").filter((f) => f.endsWith(".json")).sort()) {
  const plan = JSON.parse(readFileSync(`plans/${file}`, "utf8"));
  for (const post of Array.isArray(plan) ? plan : [plan]) {
    if (post.status !== "approved" || post.media_id || !post.date || !post.time) continue;
    const at = lisbonInstant(post.date, post.time).getTime();
    if (at - 5 * 60e3 > now) continue;
    if (now - at > MAX_LATE * 3600e3) { console.log(`too late, not published: ${post.id} (${post.date} ${post.time})`); continue; }
    due.push({ file: `plans/${file}`, id: post.id, at });
  }
}
due.sort((a, b) => a.at - b.at);
if (!due.length) console.log("nothing due");

let failed = 0;
for (const { file, id } of due) {
  const run = spawnSync(process.execPath, ["tools/publish.mjs", file, id, ...(dryRun ? ["--dry-run"] : [])], { encoding: "utf8", timeout: 15 * 60e3 });
  process.stdout.write(run.stdout || "");
  if (run.status !== 0) failed++;
}
process.exit(failed ? 1 : 0);
