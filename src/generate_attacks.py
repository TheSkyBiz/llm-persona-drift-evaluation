# src/generate_attacks.py

import os
import pandas as pd
from tqdm import tqdm

from data.personas import PERSONAS
from data.attacks import ATTACKS
from src.utils import query_model

TEMPERATURE = 0.7
BASE_PATH = "outputs/base_outputs.csv"
OUTPUT_PATH = "outputs/attacked_outputs.csv"

os.makedirs("outputs", exist_ok=True)


def main():
    base_df = pd.read_csv(BASE_PATH)
    rows = []

    for _, row in tqdm(base_df.iterrows(), total=len(base_df)):
        model = row["model"]
        persona = row["persona"]
        topic = row["topic"]
        system_prompt = PERSONAS[persona]["system_prompt"]

        for attack in ATTACKS:
            attack_prompt = topic + "\n\n" + attack["text"]

            try:
                attacked_output = query_model(
                    model=model,
                    system_prompt=system_prompt,
                    user_prompt=attack_prompt,
                    temperature=TEMPERATURE
                )

                rows.append({
                    "model": model,
                    "persona": persona,
                    "topic": topic,
                    "attack_id": attack["id"],
                    "attack_category": attack["category"],
                    "attacked_text": attacked_output
                })

            except Exception as e:
                print(f"Error: {e}")

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved attacked outputs to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()