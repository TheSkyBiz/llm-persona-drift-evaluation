# src/utils.py

import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ollama


# -------------------------
# Ollama Query Wrapper
# -------------------------

def query_model(model, system_prompt, user_prompt, temperature=0.7):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        options={"temperature": temperature}
    )
    return response["message"]["content"]


# -------------------------
# Embedding Utilities
# -------------------------

def compute_cosine(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]


# -------------------------
# Text Utilities
# -------------------------

CONTRACTIONS = ["n't", "'re", "'s", "'ll", "'ve", "'d"]
SLANG_WORDS = ["bro", "lol", "omg", "yolo", "lit", "vibe", "dude"]


def contains_contraction(text):
    return any(c in text for c in CONTRACTIONS)


def contains_slang(text):
    return any(word in text.lower() for word in SLANG_WORDS)


def contains_emoji(text):
    emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
    return bool(emoji_pattern.search(text))


def keyword_density(text, keywords):
    words = text.lower().split()
    if len(words) == 0:
        return 0
    count = sum(1 for w in words if w in keywords)
    return count / len(words)