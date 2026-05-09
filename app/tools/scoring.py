def run(data):
    scored = []

    for item in data:
        score = 80 if "LLM" in item["skill"] else 60
        scored.append({**item, "score": score})

    return sorted(scored, key=lambda x: x["score"], reverse=True)
