from datetime import datetime
from pathlib import Path

from src.assistant_core import run_assistant
from src.config import MODEL_PATHS
from src.local_llm import LocalLLM

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

TESTS = [
    "Какая погода в Москве?",
    "Который час в Варшаве?",
    "Какой учебный курс USD к RUB?",
    "Расскажи в двух предложениях, зачем нужны базы данных.",
]


def write_log(model_name: str, entries: list[str]):
    path = LOG_DIR / f"{model_name}.log"
    path.write_text("\n".join(entries), encoding="utf-8")
    print(f"Saved {path}")


def main():
    for model_name in ("qwen", "llama"):
        llm = LocalLLM(MODEL_PATHS[model_name])
        entries = [
            f"MODEL={model_name}",
            f"START={datetime.now().isoformat()}",
            "",
        ]

        for i, prompt in enumerate(TESTS, 1):
            result = run_assistant(llm, prompt)
            entries += [
                f"===== TEST {i} =====",
                f"USER: {prompt}",
                "RAW:",
                result["raw"],
                "",
                f"TOOL_CALL: {result['tool_call']}",
                f"TOOL_RESULT: {result['tool_result']}",
                "FINAL:",
                result["final"],
                "",
            ]

        entries.append(f"END={datetime.now().isoformat()}")
        write_log(model_name, entries)


if __name__ == "__main__":
    main()
