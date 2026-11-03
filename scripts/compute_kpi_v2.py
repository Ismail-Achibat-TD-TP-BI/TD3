import json, time

# A genuinely different KPI from Stage 4's (not just a different TARGET_SKILL):
# the fraction of postings mentioning any cloud provider at all, rather than one
# single named skill. Same "a KPI is a construct" principle applies here too --
# the provider list below is a choice, not a neutral fact (e.g. it excludes
# smaller/regional providers and on-prem equivalents like OpenStack).
CLOUD_PROVIDERS = ["aws", "amazon web services", "azure", "gcp", "google cloud"]

def load_extracted(path="data/extracted.json"):
    with open(path) as f:
        return json.load(f)["postings"]

def compute_cloud_kpi(postings):
    n = len(postings)
    matching = []
    for p in postings:
        skills_lower = [s.lower() for s in p.get("required_skills", [])]
        if any(any(prov in s for s in skills_lower) for prov in CLOUD_PROVIDERS):
            matching.append(p)
    return {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kpi_label": "% of postings mentioning any cloud provider (AWS/Azure/GCP)",
        "kpi_value": round(len(matching) / n, 3) if n else 0.0,
        "n_postings_analyzed": n,
        "n_matching": len(matching),
        "matching_titles": [p["title"] for p in matching],
    }

def main():
    postings = load_extracted()
    kpi = compute_cloud_kpi(postings)
    print(json.dumps(kpi, indent=2))
    with open("docs/data/kpi_v2.json", "w") as f:
        json.dump(kpi, f, indent=2)
    print("\nWrote docs/data/kpi_v2.json")

if __name__ == "__main__":
    main()
