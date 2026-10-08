from pathlib import Path
from huggingface_hub import hf_hub_download

MODELS = [
    (
        "bartowski/Qwen2.5-3B-Instruct-GGUF",
        "Qwen2.5-3B-Instruct-Q4_K_M.gguf",
    ),
    (
        "bartowski/Llama-3.2-3B-Instruct-GGUF",
        "Llama-3.2-3B-Instruct-Q4_K_M.gguf",
    ),
]

OUT = Path("models")
OUT.mkdir(exist_ok=True)

for repo_id, filename in MODELS:
    print(f"Downloading {repo_id}/{filename} ...")
    cached = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        local_dir=str(OUT),
    )
    print(f"Saved: {cached}")

print("All models downloaded.")
