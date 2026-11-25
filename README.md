# The World Today — 25 November 2026 (v2)

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/zairzuab/news-image-20261125-v2/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/zairzuab/news-image-20261125-v2/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the [make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125) (news-image-20261125).

## What it is

A dense newspaper front page — **"THE WORLD TODAY — 25 November 2026"** — summing up
Wednesday 25 November 2026 in **50 stories across 10 regions and 21 fields**, built
from the live leaderboard: the top entries win on breadth, drawn scenes, a UTC
timeline, a map, and how-sure labels, so this one has all of them.

- **Lead:** Two oil tankers hit naval mines and catch fire in the Strait of Hormuz,
  with a drawn scene of the burning tanker and a naval mine in the water.
- **Featured:** Trump hits 14 economies with new tariffs (China 20%, up to 40% if the
  truce fails) and Ukraine's drones sink a Russian warship off Libya — each with its
  own drawn scene (container ship, warship with a drone).
- **8 drawn pictogram scenes:** US tariffs, the KOSPI -6.2% AI rout, Pakistan's first
  astronaut aboard Shenzhou-24, the Solomons–Australia pact, Ramaphosa's court win,
  the Cairo tanker fire (31 dead), the Dow plunging 1,039, and SpaceX's 1m satellites.
- **10 regions:** Middle East, Americas, Europe, Asia-Pacific, Africa, Tech & Science,
  Markets & Economy, Climate & Health, Sport & Culture, Global — from the coalition
  striking Yemen's Hodeidah port and the Houthis hitting Ras Tanura, to Huawei's
  conviction, the Dow's first close above 50,000 and its Wednesday rout, the Ramaphosa
  Phala Phala ruling, and the Colombia hostage rescue.
- **UTC timeline:** the day's 7 turning points, from Shenzhou-24 docking (04:56 UTC)
  to the Dow's 1,039-point plunge (21:00 UTC).
- **World map:** a schematic map with red dots marking the day's flashpoints.
- **How-sure labels:** stories that are one side's claim (CLAIMED) or a single-source
  report (REPORTED) are tagged in red/amber, with a legend explaining the tags.
  Everything else is confirmed by wires and officials.

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-built front page
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the
grader). No network, no randomness, no timestamps: two runs produce byte-identical
output. The front page itself is drawn by `draw_frontpage.py` (PIL, run once on the
build machine) from the day's verified wire/search reports.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Output: a 1024×1024 PNG, well under the 1 MiB gate limit.

## Files

- `main.py` — the program that copies the front page to /output
- `draw_frontpage.py` — the program that draws the front page from the day's news
- `entry.png` — the generated front page (also produced by running `draw_frontpage.py`)
- `fonts/` — DejaVu fonts bundled with the repo (used by `draw_frontpage.py`)
- `LICENSE` — MIT

Built by Muse for [@zairzuab](https://github.com/zairzuab) for make.fun bounty `news-image-20261125`.
