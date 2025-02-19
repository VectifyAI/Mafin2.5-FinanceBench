import time
import asyncio
import json
from openai import AsyncOpenAI
from tqdm.asyncio import tqdm


OPENAI_API_KEY = ""

DEEPSEEK_MODEL = ""
DEEPSEEK_BASE_URL = ""
DEEPSEEK_API_KEY = ""


async def get_completion_async(prompt, model=None, temperature=0):
    if model == DEEPSEEK_MODEL:
        openai_client = AsyncOpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    else:
        openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    for i in range(3):
        try:
            messages = [{"role": "user", "content": prompt}]
            if model in ['o3-mini', 'o1-mini']:
                response = await openai_client.chat.completions.create(model=model, messages=messages)
            else:
                response = await openai_client.chat.completions.create(model=model, messages=messages, temperature=temperature)
            await openai_client.close()
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            time.sleep(1)
    await openai_client.close()


async def check_answer_equivalence(answer, gold_answer, query=None, model="gpt-4o-2024-11-20"):

    query_prompt = f"- Query: {query}" if query else ""

    prompt = f"""
    You are an expert evaluator for AI-generated responses to queries. Your task is to determine whether the AI-generated answer correctly answers the query based on the golden answer provided by a human expert.

    Numerical Accuracy: 
    - Rounding differences should be **ignored** if they do not meaningfully change the conclusion.
    - You can allow some flexibility in accuracy. For example, 1.2 is considered similar to 1.23. Two numbers are considered similar if one can be rounded to the other.
    - Fractions, percentage, and numerics could be considered similar, for example: "11 of 14" is considered equivalent to "79%" and "0.79".

    Evaluation Criteria:
    - If the golden answer or any of its equivalence can be inferred or generated from the AI-generated answer, then the AI-generated answer is considered correct.
    - If any number, percentage, fraction, or figure in the golden answer is not present in the AI-generated answer, but can be inferred or generated from the AI-generated answer or implicitly exist in the AI-generated answer, then the AI-generated answer is considered correct.
    - The AI-generated answer is considered correct if it conveys the same or similar meaning, conclusion, or rationale as the golden answer.
    - If the AI-generated answer is a superset of the golden answer, it is also considered correct.
    - If the AI-generated answer provides a valid answer or reasonable interpretation compared to the golden answer, it is considered correct.
    - If the AI-generated answer contains subjective judgments or opinions, it is considered correct as long as they are reasonable and justifiable compared to the golden answer.

    - Otherwise, the AI-generated answer is incorrect.

    Inputs:
    {query_prompt}
    - AI-Generated Answer: {answer}
    - Golden Answer: {gold_answer}

    Your output should be ONLY a boolean value: `True` or `False`, nothing else.
    """

    response = await get_completion_async(prompt, model=model)

    if "true" in response.lower():
        return True
    elif "false" in response.lower():
        return False
    

async def judge_benchmark_results(benchmark_results, model="gpt-4o-2024-11-20"):
    tasks = []
    for result in benchmark_results:
        query = result['question']
        gold_answer = result['benchmark_answer']
        answer = result['mafin_answer']
        tasks.append(check_answer_equivalence(answer, gold_answer, query=query, model=model))
    results = await tqdm.gather(*tasks, desc="Evaluating answers")
    return results


def judge_benchmark_results_from_file(json_file_path, model="gpt-4o-2024-11-20"):
    with open(json_file_path, 'r') as f:
        benchmark_results = json.load(f)
    results = asyncio.run(judge_benchmark_results(benchmark_results, model=model))
    wrong_indexes = []
    for i, result in enumerate(results):
        if not result and 'AL' == benchmark_results[i]['label']:
            wrong_indexes.append(i)
    print(f"Wrong indexes: {wrong_indexes}")
    return results


def judge_benchmark_results_from_file_hybrid(json_file_path, models=["gpt-4o-2024-11-20", "o1-mini", "o3-mini"]):
    if not models:
        raise ValueError("No models provided for hybrid evaluation.")
    
    hybrid_results = {}
    for model in models:
        print(f"\nJudging results using model '{model}'...")
        results = judge_benchmark_results_from_file(json_file_path, model=model)
        hybrid_results[model] = results
    
    base_model = models[0]
    combined_results = []
    results = hybrid_results[base_model]
    for i in range(len(results)):
        combined_result = any([hybrid_results[model][i] for model in models])
        combined_results.append(combined_result)

    return combined_results


if __name__ == "__main__":

    file_path = "result_gpt4o.json"

    results = judge_benchmark_results_from_file(file_path)

    print(results)