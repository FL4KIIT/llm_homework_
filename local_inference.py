from src.config import MODEL_PATHS, SYSTEM_PROMPT
from src.local_llm import LocalLLM

for name in ("qwen", "llama"):
    print(f"\n=== {name.upper()} ===")
    llm = LocalLLM(MODEL_PATHS[name])
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Кратко объясни, что такое машинное обучение."},
    ]
    answer = llm.complete_text(messages)
    print(answer)
