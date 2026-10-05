// Public metrics of other professional Instagram accounts (Graph API business_discovery).
// usage: node tools/market.mjs <out.json> user1 user2 ...
// Only public business data: followers, recent posts, format, likes, comments, time.
import { writeFileSync } from "node:fs";

const [out, ...users] = process.argv.slice(2);
const token = process.env.INSTAGRAM_ACCESS_TOKEN;
const account = process.env.INSTAGRAM_ACCOUNT_ID;
const version = process.env.INSTAGRAM_API_VERSION || "v26.0";
if (!token || !account) throw new Error("Missing INSTAGRAM_ACCESS_TOKEN or INSTAGRAM_ACCOUNT_ID");

const MEDIA = "caption,like_count,comments_count,media_type,media_product_type,timestamp,permalink";
const results = [];
for (const user of users) {
  const fields = `business_discovery.username(${user}){username,name,followers_count,media_count,media.limit(40){${MEDIA}}}`;
  const url = `https://graph.facebook.com/${version}/${account}?fields=${encodeURIComponent(fields)}`;
  const data = await (await fetch(url, { headers: { Authorization: `Bearer ${token}` } })).json();
  if (data.error) {
    results.push({ user, error: data.error.message });
    console.log(`${user}: ${data.error.message}`);
    continue;
  }
  const bd = data.business_discovery;
  const media = bd.media?.data ?? [];
  results.push({ user, name: bd.name, followers: bd.followers_count, posts: bd.media_count, media });
  console.log(`${user}: ${bd.followers_count} followers, ${media.length} recent posts`);
}
writeFileSync(out, JSON.stringify(results, null, 2));
