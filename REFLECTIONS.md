# REFLECTIONS (TD3)

## Stage 1 — silent vs. loud failure (robots.txt check)
A loud crash stops you immediately and points at the exact cause, so you fix it before anything downstream runs. A silent failure doesn't: `rp.read()` returns `False` and the script would just skip scraping, but it could just as easily have defaulted the other way and let scraping proceed while believing it had checked permission when it hadn't. That's the real danger.

## Stage 1 — official API vs. jobspy-scraped data, and public/private
France Travail's API is explicitly licensed for reuse — the risk of redistributing it is essentially zero because the owner already said yes. The jobspy-derived sample has no such license; Indeed/LinkedIn's Terms of Service forbid redistributing what's scraped from them, so the risk isn't about the data's content, it's about not having permission to share it. My answer would change with public vs. private, but only partway: a private repo lowers the *chance* of this being noticed, but it doesn't make it allowed — republishing without a license is still a ToS violation either way. That's exactly why the `.gitignore` keeps `jobs_sample.csv` out of the repo regardless of visibility, rather than relying on the repo being private.

## Stage 2 — why an LLM fits free-text extraction but not a record of your own actions
CM5's distinction is: use an LLM where the task is turning messy, unstructured input into a structured guess that a human can still check, not where it would replace a factual record of what you actually did. Free-text-to-skills fits the first case: the posting text already exists, and the LLM's job is to summarize/structure it

## Stage 3 — the capitalization check
**Prediction:** the same real skill would likely come back with inconsistent capitalization across calls, since each posting is processed independently with no shared memory of previous answers.

**Found it:** yes — `"generative AI"` (CarCutter and Diffusely postings) vs. `"Generative AI"` (the CEA posting). Same real skill, two capitalizations, which would silently split into two separate bars if I started counting without normalizing.

