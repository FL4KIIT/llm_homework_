import requests
import json



r = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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", 
        "Content-Type": "application/json",
    },
    data=json.dumps({
        # "model": "qwen/qwen3.8-27b:free",
        "model": "inclusionai/ling-3.0-flash-vl:free",
        "messages": [{"role": "user", "content": "hi"}]
    }),
    # proxies=PROXIES,
    timeout=(10, 60),
)

print("status:", r.status_code)
print("body:", r.text[:500])