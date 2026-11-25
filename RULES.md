# Translation rules (EN → TH)

Applies to dialogue, tips/emails, **and UI** under `edit/`.

Source of truth: **vanilla English** in column `en`.  
Write Thai from `en` only.

## Do translate
- Spoken subtitles (`~z~…`)
- Tips / emails / help (`edit/00_global_tips_emails.csv`)
- UI / menu labels (`edit/ui/*.csv`) when seeded

## Keep Latin
- Names: Michael, Franklin, Trevor, Lamar, …
- Places: Los Santos, Vinewood, Sandy Shores, …
- Brands: Ammu-Nation, Lifeinvader, Merryweather, …

## Markup
Keep every `~TOKEN~` exactly (`~z~`, `~n~`, `~INPUT_*~`, colors, `~a~`, `~1~`, …).  
If `en` starts with `~z~`, `th` must too.

## Tone
- Match EN register (polite → polite Thai; street → casual)
- **กู/มึง** only when EN is rough / street — never harsher than EN
- Prefer ผม/ฉัน/คุณ/นาย when EN is neutral
- UI: short, clear labels — match EN length when possible
