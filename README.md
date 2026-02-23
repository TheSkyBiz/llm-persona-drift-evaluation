# Persona Drift Arena

## Quantifying LLM Persona Stability Under Adversarial Pressure

------------------------------------------------------------------------

## Overview

Persona Drift Arena is an adversarial evaluation framework designed to
measure how well open-source Large Language Models (LLMs) maintain
assigned stylistic personas under conflicting or malicious instructions.

The framework evaluates semantic and stylistic drift using embedding
similarity, keyword retention, structural violations, and override
detection.

------------------------------------------------------------------------

# Experimental Design

## Models Evaluated

-   llama3:8b\
-   qwen2.5:1.5b\
-   phi

## Personas

1.  Medieval Court Historian (archaic, ceremonial tone)
2.  Sarcastic Stand-Up Comedian (informal, exaggerated, rhetorical)
3.  Strict Physics Professor (structured, analytical, precise)

## Topics (5)

-   Collapse of Civilizations
-   Why the Sky is Blue
-   Economic Inequality
-   Human Space Exploration
-   Artificial Intelligence

## Attack Categories (20 Total)

-   Override Instructions
-   Tone Corruption
-   Modernity Injection
-   Role Reassignment
-   Structural Disruption

------------------------------------------------------------------------

# Dataset Scale

-   3 Models\
-   3 Personas\
-   5 Topics\
-   20 Attacks per base prompt

Total Generations: - 45 Base Outputs\
- 900 Adversarial Outputs\
- 945 Total Generations

------------------------------------------------------------------------

# Metrics

## 1. Embedding Drift Score

Drift = 1 − cosine_similarity(base, attacked)

Higher drift indicates greater semantic and stylistic deviation.

## 2. Persona Marker Retention

Keyword density comparison between base and attacked outputs.

## 3. Structural Violation Score

Detection of forbidden stylistic markers (emojis, slang, contractions,
etc.).

## 4. Override Rate

Binary detection of persona abandonment under direct override attacks.

------------------------------------------------------------------------

# Key Results

## Drift by Model (Mean)

  Model          Avg Drift
  -------------- -----------
  llama3:8b      \~0.31
  qwen2.5:1.5b   \~0.33
  phi            \~0.39

Larger models exhibit stronger persona stability under adversarial
pressure.

------------------------------------------------------------------------

## Drift by Persona

  Persona     Avg Drift
  ----------- -----------
  Comedian    \~0.40
  Historian   \~0.33
  Professor   \~0.29

Expressive personas are significantly more fragile than structured
analytical personas.

------------------------------------------------------------------------

## Drift by Attack Category

Highest destabilizing category: Modernity Injection (\~0.36)\
Lowest semantic drift: Direct Override (\~0.31)

Semantic contamination produces stronger embedding shifts than direct
instruction reversal.

------------------------------------------------------------------------

## Distribution Analysis (Heavy-Tail Behavior)

Phi exhibits heavy right-tail drift, including catastrophic collapse
cases (drift \> 0.9).\
Llama3 shows the narrowest distribution with lower variance and higher
predictability.

------------------------------------------------------------------------

# Generated Visualizations

The repository automatically produces:

-   plots/drift_by_model.png\
-   plots/override_rate.png\
-   plots/drift_by_attack_category.png\
-   plots/drift_by_persona.png\
-   plots/drift_heatmap.png\
-   plots/drift_distribution.png

These plots provide multi-dimensional behavioral insight across model
scale, persona type, and attack category.

------------------------------------------------------------------------

# How to Use This Repository

## 1. Clone Repository

``` bash
git clone <your-repo-url>
cd persona-drift-arena
```

## 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

## 3. Install and Start Ollama

Download Ollama from: https://ollama.com

Then pull required models:

``` bash
ollama pull llama3:8b
ollama pull qwen2.5:1.5b
ollama pull phi
```

Make sure Ollama is running before executing scripts.

------------------------------------------------------------------------

## 4. Run Evaluation Pipeline

Run from project root:

``` bash
python -m src.generate_base
python -m src.generate_attacks
python -m src.compute_metrics
python -m src.plot_results
```

------------------------------------------------------------------------

## Output Files

Generated CSV files:

-   outputs/base_outputs.csv\
-   outputs/attacked_outputs.csv\
-   outputs/results.csv

Generated plots:

-   plots/\*.png

------------------------------------------------------------------------

# Practical Implications

For production systems requiring tone consistency:

-   Larger models reduce catastrophic persona collapse risk.
-   Structured roles are safer than highly expressive personas.
-   Semantic contamination is a greater destabilization vector than
    direct override attacks.

------------------------------------------------------------------------

# Future Improvements

-   Statistical significance testing (t-tests)
-   Temperature sensitivity sweep
-   Token-length normalized drift
-   Real-time checkpointing for long attack runs
-   Cross-model persona transfer evaluation

------------------------------------------------------------------------

# Conclusion

Persona Drift Arena demonstrates that adversarial persona stability is:

-   Model-scale sensitive\
-   Persona-type sensitive\
-   Attack-category sensitive\
-   Distributionally asymmetric

This framework provides a reproducible and quantitative method for
evaluating stylistic robustness in open-source LLMs.

------------------------------------------------------------------------

Author: Aakash Biswas\
Focus: Applied ML, LLM Reliability, Robustness Evaluation
