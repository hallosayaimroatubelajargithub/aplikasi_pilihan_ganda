import requests

API_URL = "https://saas.cakra.ai/genv2/llms"
API_TOKEN = "75f7a185-55a8-4aae-b0b2-47e016493b60"

def validate_answer_with_llm(question, user_answer, correct_answer):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    payload = {
        "model_name": "brain-v2",
        "messages": [
            {"role": "system", "content": "Validate the user's answer against the correct answer."},
            {"role": "user", "content": f"Question: {question}\nUser's Answer: {user_answer}\nCorrect Answer: {correct_answer}"}
        ],
        "max_new_tokens": 100,
        "do_sample": False,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1.0
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        llm_response = response.json()
        explanation = llm_response['choices'][0]['content']
        is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
        return {
            "is_correct": is_correct,
            "explanation": explanation
        }
    else:
        return {
            "is_correct": False,
            "explanation": "Error in validating answer via LLM API."
        }
