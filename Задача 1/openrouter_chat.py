from src.config import SYSTEM_PROMPT, OPENROUTER_MODEL
from src.openrouter_llm import OpenRouterLLM

llm = OpenRouterLLM(OPENROUTER_MODEL)
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Кратко объясни, что такое машинное обучение."},
]

print("OpenRouter model:", OPENROUTER_MODEL)
for token in llm.stream_text(messages):
    print(token, end="", flush=True)
print()
