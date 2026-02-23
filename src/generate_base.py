# src/generate_base.py

import os
import pandas as pd
from tqdm import tqdm

from data.personas import PERSONAS
from data.topics import TOPICS
from src.utils import query_model

# -------------------------
# CONFIG
# -------------------------

MODELS = [
    "qwen2.5:1.5b",
    "phi",
    "llama3:8b"
]

TEMPERATURE = 0.7
OUTPUT_PATH = "outputs/base_outputs.csv"

os.makedirs("outputs", exist_ok=True)


def main():
    rows = []

    for model in MODELS:
        print(f"\nGenerating base outputs for model: {model}")

        for persona_name, persona_data in PERSONAS.items():
            system_prompt = persona_data["system_prompt"]

            for topic in tqdm(TOPICS):
                try:
                    output = query_model(
                        model=model,
                        system_prompt=system_prompt,
                        user_prompt=topic,
                        temperature=TEMPERATURE
                    )

                    rows.append({
                        "model": model,
                        "persona": persona_name,
                        "topic": topic,
                        "base_text": output
                    })

                except Exception as e:
                    print(f"Error: {e}")

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved base outputs to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()