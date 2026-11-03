# REFLECTIONS (TD3)

## 1. Silent vs. loud failure (robots.txt check)
A loud crash stops you immediately and points at the exact cause, so you fix it before anything downstream runs. A silent failure doesn't: `rp.read()` returns `False` and the script would just skip scraping, but it could just as easily have defaulted the other way and let scraping proceed while believing it had checked permission when it hadn't. That's the real danger

## 2. Official API vs. jobspy-scraped data, and public/private
France Travail's API is explicitly licensed for reuse — the risk of redistributing it is essentially zero because the owner already said yes. The jobspy-derived sample has no such license; Indeed/LinkedIn's Terms of Service forbid redistributing what's scraped from them, so the risk isn't about the data's content, it's about not having permission to share it. My answer would change with public vs. private, but only partway: a private repo lowers the *chance* of this being noticed, but it doesn't make it allowed — republishing without a license is still a ToS violation either way. That's exactly why the `.gitignore` keeps `jobs_sample.csv` out of the repo regardless of visibility, rather than relying on the repo being private.

## 3. Why an LLM fits free-text extraction but not a record of your own actions
CM5's distinction is: use an LLM where the task is turning messy, unstructured input into a structured guess that a human can still check, not where it would replace a factual record of what you actually did. Free-text-to-skills fits the first case: the posting text already exists, and the LLM's job is to summarize/structure it

## 4. The capitalization check
**Prediction:** the same real skill would likely come back with inconsistent capitalization across calls, since each posting is processed independently with no shared memory of previous answers.

**Found it:** yes — `"generative AI"` (CarCutter and Diffusely postings) vs. `"Generative AI"` (the CEA posting). Same real skill, two capitalizations, which would silently split into two separate bars if I started counting without normalizing.

## 5. The critique pass as human-in-the-loop
This counts as human-in-the-loop because a person checks the model's raw output against the original source before it's trusted for anything downstream — the model proposes, a human disposes, instead of the output being used unchecked. It has to run on `extracted.json`, not `kpi.json`, because that's the only file that still has both the model's actual per-posting answer and enough context (title, skill list) to compare against the original description; `kpi.json` only holds an already-aggregated number, so by the time an error would show up there, the specific wrong skill and which posting it came from are gone, and there's nothing left to correct it against.

## 6. TARGET_SKILL: my choice vs. the default
Before seeing any number, the skill I'd track for a curriculum committee is **CI/CD** — it's concrete, teachable in a course, and shows up across genuinely different job types (an embedded test-bench role, a DevOps role, a software integration role), not just one niche track, which is exactly the kind of cross-cutting demand a committee would want evidence for before changing a syllabus.

Running both through the same matching logic as `compute_kpi.py`, on my real 12-posting sample: `python` → 2/12 (16.7%), `ci/cd` → 3/12 (25%). Neither is the one I'd actually trust for a real decision — the sample is only 12 postings, so one extra posting changes the percentage by over 8 points, and the KPI only checks whether a skill was *mentioned*, not how central it is to the role. I'd trust mine over the default only in the narrow sense that I named it for a reason tied to the actual postings rather than it being the manual's pre-picked example; I wouldn't present either number to a real committee without a much bigger sample first.

## 7. What `kpi.json` does and doesn't reveal
it has `kpi_label`, `kpi_value`, counts, and a `top_skills` list of skill names with how often they recur — no job URLs, no company names, no locations, no dates, no raw posting text. A classmate couldn't reconstruct which specific postings were scraped or which company any came from. That's a deliberate design choice in `compute_kpi()`, not luck: the function only ever reads `title` and `required_skills` off each posting internally, and the only things it writes back out are aggregates (a ratio, a count, a `Counter` of skill names) — `company`, `job_url`, and the raw `description` text that exist in `jobs_sample.csv` are never even passed into the returned dict, so there was nothing company-identifying left to accidentally leak.

## 8. Who this dashboard is actually for
It's for me, the title "Scraping to KPI lab" and the description ("see `data/extracted.json` and `compute_kpi.py`") both point a reader at the pipeline and the code behind it, which only makes sense to someone verifying the build, not a curriculum committee deciding what to teach next. A committee wouldn't know what `extracted.json` or `compute_kpi.py` even are.

## 9. Second KPI vs. Stage 4's KPI
My second KPI: % of postings mentioning any cloud provider (AWS, Azure or GCP) — 2 of 12 (16.7%), from the DevOps and L2 Desktop Support postings. Comparing it to Stage 4's `python` KPI (also 2/12): both move together here only by coincidence of a 12-posting sample, but they measure different things.