# GTA V Enhanced Thai v3 — translation rules (EN → TH)

Source of truth: **vanilla English**. Write Thai from column `en` only.

## Translate
- Spoken subtitles (`~z~…`)
- Mission help / tips / emails / long instructional lines in `global` (and similar narrative text)
- Keep all `~TOKEN~` markup exactly (`~z~`, `~n~`, `~INPUT_*~`, `~a~`, `~1~`, colors, etc.)

## Keep English (Latin)
- Character names: Michael, Franklin, Trevor, Lamar, Lester, Simeon, …
- Places: Los Santos, Vinewood, Sandy Shores, Paleto Bay, …
- Brands / orgs: Ammu-Nation, Lifeinvader, Merryweather, Ballas, Vagos, …
- Short UI-only labels, clothing/tattoo/gun menu stems, credits, track IDs, creator (`fmmc`), vehicle model names alone
- Speaker-name-only lines (`~z~Lamar`, `~z~Franklin!`) — keep as-is

## Tone (match the game, not harsher than EN)
- Match EN register: polite EN → polite Thai; street/gang EN → casual Thai
- Use **กู/มึง** when EN is rough *or* speaker is clearly street/Trevor-heat — do **not** force กู/มึง onto polite/professional lines
- Do **not** escalate violence/insults beyond what EN says
- Natural spoken Thai; avoid stiff bureaucratic phrasing
- Prefer ผม/ฉัน/คุณ/นาย when EN is neutral and speaker isn’t in gang register

## Output
JSON object: `"{stem}:{hash}" → {"stem","h","en","th"}`  
Every input row must appear once. `th` must include leading `~z~` when `en` has it.