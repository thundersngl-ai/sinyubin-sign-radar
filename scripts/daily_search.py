import json, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

QUERY = '"신유빈" (친필 OR 싸인 OR 사인)'
RSS_URL = "https://news.google.com/rss/search?q=" + urllib.parse.quote(QUERY) + "&hl=ko&gl=KR&ceid=KR:ko"
OUT = Path("results.json")

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

items = []
try:
    req = urllib.request.Request(RSS_URL, headers={"User-Agent":"Mozilla/5.0 sign-radar/1.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    for node in root.findall("./channel/item"):
        title = clean(node.findtext("title"))
        link = clean(node.findtext("link"))
        pub = clean(node.findtext("pubDate"))
        source = clean(node.findtext("source")) or "Google News RSS"
        if not title or not link:
            continue
        # Remove exact duplicates by canonical link.
        if any(x["link"] == link for x in items):
            continue
        items.append({"title":title,"link":link,"published":pub,"source":source,
                      "authenticity":"unverified"})
except Exception as exc:
    print("RSS fetch failed:", repr(exc))
    # Preserve a clear error state; do not silently claim a successful scan.
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    old["last_error"] = str(exc)
    old["updated_at"] = datetime.now(timezone.utc).isoformat()
    OUT.write_text(json.dumps(old,ensure_ascii=False,indent=2),encoding="utf-8")
    raise

payload = {
    "query": QUERY,
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "source_note": "Google News RSS public index only; not a complete marketplace scan.",
    "items": items
}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Saved {len(items)} public RSS results")
