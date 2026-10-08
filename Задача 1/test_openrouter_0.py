import requests
import json

# First API call with reasoning
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions", 
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "inclusionai/ling-3.0-flash-vl:free",
        "messages": [
            {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
            }
        ],
        "reasoning": {"enabled": True}
    })
) 

print("Status Code:", response.status_code)

if response.status_code == 200:
    # Extract the assistant message with reasoning_details
    response_json = response.json()
    message = response_json['choices'][0]['message']
    print(message)
else:
    print("Error:", response.text)