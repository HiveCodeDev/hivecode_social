// Publishes one approved post from a plan file to Instagram (Graph API, Facebook login).
// usage: node tools/publish.mjs <plan.json> <post-id> [--dry-run]
//
// Reads INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID and INSTAGRAM_API_VERSION from the
// environment; the token goes in the Authorization header and is never printed.
// Only posts with status "approved" and no media_id are published, so a repeated run
// (for example after the app reopens) never posts twice.
import { readFileSync, writeFileSync } from "node:fs";

const [planPath, postId, flag] = process.argv.slice(2);
const dryRun = flag === "--dry-run";
const token = process.env.INSTAGRAM_ACCESS_TOKEN;
const account = process.env.INSTAGRAM_ACCOUNT_ID;
const version = process.env.INSTAGRAM_API_VERSION || "v26.0";
const api = `https://graph.facebook.com/${version}`;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const fail = (message) => {
  console.log(JSON.stringify({ ok: false, post: postId, error: message }));
  process.exit(1);
};

if (!token || !account) fail("Missing INSTAGRAM_ACCESS_TOKEN or INSTAGRAM_ACCOUNT_ID");
const plan = JSON.parse(readFileSync(planPath, "utf8"));
const post = plan.find((p) => p.id === postId);
if (!post) fail("Post not found in plan");
if (post.media_id) {
  console.log(JSON.stringify({ ok: true, post: postId, skipped: "already published", media_id: post.media_id }));
  process.exit(0);
}
if (post.status !== "approved") fail(`Status is "${post.status}", not "approved"`);

// The plan's date and time are Lisbon local time. Before that moment (minus a
// 5-minute margin) the script only checks, so a run started early never posts.
function lisbonInstant(date, time) {
  const guess = new Date(`${date}T${time}:00Z`);
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Lisbon", hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" })
      .formatToParts(guess)
      .map((p) => [p.type, p.value]),
  );
  const shown = new Date(`${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}:00Z`);
  return new Date(guess.getTime() - (shown.getTime() - guess.getTime()));
}
const scheduled = lisbonInstant(post.date, post.time);
const early = Date.now() < scheduled.getTime() - 5 * 60 * 1000;

async function call(method, path, params = {}) {
  const query = new URLSearchParams(params);
  const headers = { Authorization: `Bearer ${token}` };
  const url = method === "GET" ? `${api}/${path}?${query}` : `${api}/${path}`;
  const res = await fetch(url, method === "GET" ? { headers } : { method, headers, body: query });
  const data = await res.json();
  if (data.error) throw new Error(`${data.error.message} (code ${data.error.code})`);
  return data;
}

// Every media URL must answer before Instagram is asked to fetch it.
for (const url of [post.video_url, post.image_url, post.cover_url, ...(post.image_urls ?? [])].filter(Boolean)) {
  const res = await fetch(url, { method: "HEAD" });
  if (!res.ok) fail(`Media not reachable (${res.status}): ${url}`);
}
if (dryRun || early) {
  console.log(JSON.stringify({ ok: true, post: postId, dryRun: true, reason: dryRun ? "--dry-run" : "before scheduled time", scheduled: scheduled.toISOString(), type: post.type }));
  process.exit(0);
}

try {
  // Containers are processed asynchronously; publishing before FINISHED fails.
  const ready = async (containerId) => {
    for (let i = 0; i < 60; i++) {
      const { status_code: status } = await call("GET", containerId, { fields: "status_code" });
      if (status === "FINISHED") return;
      if (status === "ERROR" || status === "EXPIRED") throw new Error(`Container ${status}`);
      await sleep(i < 6 ? 5000 : 10000);
    }
    throw new Error("Container still processing after 10 minutes");
  };

  let params;
  if (post.type === "reel") {
    params = { media_type: "REELS", video_url: post.video_url, caption: post.caption, share_to_feed: "true", ...(post.cover_url && { cover_url: post.cover_url }) };
  } else if (post.type === "carousel") {
    const children = [];
    for (const url of post.image_urls) {
      const child = await call("POST", `${account}/media`, { image_url: url, is_carousel_item: "true" });
      await ready(child.id);
      children.push(child.id);
    }
    params = { media_type: "CAROUSEL", children: children.join(","), caption: post.caption };
  } else {
    params = { image_url: post.image_url, caption: post.caption };
  }
  const container = await call("POST", `${account}/media`, params);
  await ready(container.id);

  const { id } = await call("POST", `${account}/media_publish`, { creation_id: container.id });
  const { permalink } = await call("GET", id, { fields: "permalink" });
  post.media_id = id;
  post.permalink = permalink;
  post.status = "published";
  post.published_at = new Date().toISOString();
  writeFileSync(planPath, JSON.stringify(plan, null, 2) + "\n");
  console.log(JSON.stringify({ ok: true, post: postId, media_id: id, permalink }));
} catch (error) {
  fail(error.message);
}
