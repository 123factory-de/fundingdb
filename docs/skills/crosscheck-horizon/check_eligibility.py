#!/usr/bin/env python3
"""Report country/control participation restrictions for every topic of every
Horizon Europe page in content/programs/.

For each `horizon-*.md` page the call identifier is taken from the portal link
in the front matter, the call's topics are looked up in the portal bulk dataset
(grantsTenders.json), and each topic's official "Conditions" text is fetched from
the portal topic-details endpoint. Two kinds of clause are extracted:

  * "participation is limited to legal entities established in ..." — a
    country restriction. Korea (associated to Pillar II) is eligible when the
    scope names it, or covers "associated countries" / OECD; otherwise Korean
    entities are excluded (e.g. Space topics limited to Member States + NO/IS).
  * "restriction on control in innovation actions in critical technology areas"
    (General Annexes Part 15) — entities directly or indirectly controlled by China
    may not participate. This is an ownership test, not a nationality test: an
    ordinary Korean company is unaffected.
  * "The following additional eligibility criteria apply:" — topic-specific
    requirements that often matter more in practice than the country rules, e.g.
    CL3 topics that require EU police / border-guard / disaster authorities as
    beneficiaries, CL6 topics requiring the multi-actor approach, geographic
    mandates (African Union, Ukraine), consortium size caps, or topics open only
    to a named predecessor consortium.

Output: one line per page, then per restricted topic. Exit code 0 always; the
report is meant to be read, and the page's 지원자격 section updated by hand.

Usage:
  python3 docs/skills/crosscheck-horizon/check_eligibility.py [--dump grantsTenders.json] [--cache DIR]

Standard library only. Topic JSON files are cached in --cache (default: temp dir)
so re-runs are fast.
"""
import argparse, collections, html, json, os, re, subprocess, sys, tempfile

DUMP_URL = "https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json"
TOPIC_URL = "https://ec.europa.eu/info/funding-tenders/opportunities/data/topicDetails/{}.json"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROGRAMS = os.path.join(ROOT, "content", "programs")

def strip_html(v):
    if isinstance(v, list):
        v = " ".join(str(x) for x in v)
    return html.unescape(re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", v or "")))

def fetch(url, path):
    if not os.path.exists(path):
        subprocess.run(["curl", "-sL", "-o", path, url], check=True)
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump")
    ap.add_argument("--cache", default=os.path.join(tempfile.gettempdir(), "horizon-topics"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    dump = a.dump or fetch(DUMP_URL, os.path.join(tempfile.gettempdir(), "grantsTenders.json"))
    data = json.load(open(dump, encoding="utf-8"))["fundingData"]["GrantTenderObj"]
    bycall = collections.defaultdict(list)
    for g in data:
        if g.get("type") == 1:
            bycall[g.get("callIdentifier", "").lower()].append(g)
    for f in sorted(os.listdir(PROGRAMS)):
        if not f.startswith("horizon-") or not f.endswith(".md"):
            continue
        s = open(os.path.join(PROGRAMS, f), encoding="utf-8").read()
        m = re.search(r"callIdentifier=([A-Za-z0-9-]+)", s)
        if not m:
            print(f"{f[:-3]}: no callIdentifier link"); continue
        call = m.group(1)
        topics = sorted(bycall[call.lower()], key=lambda x: x["identifier"])
        rows = []
        for g in topics:
            tid = g["identifier"]
            t = json.load(open(fetch(TOPIC_URL.format(tid.lower()), os.path.join(a.cache, tid.lower() + ".json"))))["TopicDetails"]
            c = strip_html(t.get("conditions")) + " " + strip_html(t.get("description"))
            m2 = re.search(r"participation is limited to legal entities established in ([^.]*)\.", c)
            if m2:
                sc = m2.group(1)
                # A closed list ("the following additional associated countries: ...")
                # only covers Korea if it is named; an open "associated countries" does.
                lc = sc.lower()
                kr = "korea" in lc or ("associated countries" in lc and "following" not in lc)
                rows.append((tid, ("KR-OK   " if kr else "KR-EXCL ") + "limited to: " + sc))
            if "restriction on control in innovation actions" in c:
                rows.append((tid, "CN-CTRL entities controlled by China not eligible"))
            m3 = re.search(r"The following additional eligibility criteria apply:(.*?)"
                           r"(?:If projects use satellite|Described in Annex B|described in Annex B|"
                           r"4\. Financial and operational|Proposal page limits|$)", c, re.S)
            if m3:
                txt = re.sub(r"\[\[.*?\]\]", " ", m3.group(1))
                rows.append((tid, "EXTRA   " + re.sub(r"\s+", " ", txt).strip()[:200]))
        print(f"{f[:-3]} ({call}): {len(topics)} topics, {len(rows)} restriction clause(s)")
        for tid, msg in rows:
            print(f"    {tid}: {msg}")

if __name__ == "__main__":
    main()
