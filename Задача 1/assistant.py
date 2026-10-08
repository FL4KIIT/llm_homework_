import argparse

from src.assistant_core import run_assistant
from src.config import MODEL_PATHS
from src.local_llm import LocalLLM


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=["qwen", "llama"], default="qwen")
    args = parser.parse_args()

    llm = LocalLLM(MODEL_PATHS[args.model])

    print("Tool assistant.")
    print("Примеры: 'Какая погода в Москве?', 'Курс USD к RUB?', 'Время в Варшаве?'")
    print("/exit — выход.")

    while True:
        try:
            user = input("\nВы: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user.lower() in {"/exit", "/quit"}:
            break
        if not user:
            continue

        result = run_assistant(llm, user)

        print("\n[RAW MODEL OUTPUT]")
        print(result["raw"])

        if result["tool_call"]:
            print("\n[PARSED TOOL CALL]")
            print("name =", result["tool_call"].name)
            print("arguments =", result["tool_call"].arguments)
            print("[TOOL RESULT]")
            print(result["tool_result"])

        print("\n[FINAL]")
        print(result["final"])


if __name__ == "__main__":
    main()
