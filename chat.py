import argparse

from src.config import MODEL_PATHS, SYSTEM_PROMPT
from src.local_llm import LocalLLM
from src.openrouter_llm import OpenRouterLLM


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["local", "openrouter"], default="local")
    parser.add_argument("--model", choices=["qwen", "llama"], default="qwen")
    args = parser.parse_args()

    llm = (
        LocalLLM(MODEL_PATHS[args.model])
        if args.backend == "local"
        else OpenRouterLLM()
    )

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("LLM chat. /reset — очистить историю, /exit — выход.")

    while True:
        try:
            user = input("\nВы: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход.")
            break

        if not user:
            continue
        if user.lower() in {"/exit", "/quit"}:
            print("Выход.")
            break
        if user.lower() == "/reset":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("История очищена.")
            continue

        messages.append({"role": "user", "content": user})
        print("Ассистент: ", end="", flush=True)

        answer_parts = []
        try:
            for token in llm.stream_text(messages):
                print(token, end="", flush=True)
                answer_parts.append(token)
        except Exception as exc:
            print(f"\nОшибка: {exc}")
            messages.pop()
            continue

        print()
        messages.append(
            {"role": "assistant", "content": "".join(answer_parts)}
        )


if __name__ == "__main__":
    main()
