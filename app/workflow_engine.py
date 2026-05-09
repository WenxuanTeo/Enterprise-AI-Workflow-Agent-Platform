from app.tools import resume_parser, scoring, web_search

def run_workflow(plan: dict):
    results = {}

    for step in plan["steps"]:
        if "简历" in step:
            results[step] = resume_parser.run()
        
        elif "评分" in step:
            results[step] = scoring.run(results)
        
        elif "搜索" in step:
            results[step] = web_search.run()

        else:
            results[step] = "LLM fallback execution"

    return results
