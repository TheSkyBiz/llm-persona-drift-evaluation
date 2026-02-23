
# Persona Drift Evaluation in LLMs
## Quantifying LLM Persona Stability Under Adversarial Pressure

---

## Overview

**Persona Drift Arena** is an adversarial evaluation framework designed to measure how well open-source Large Language Models (LLMs) maintain assigned stylistic personas when subjected to conflicting or malicious instructions.

The framework quantifies semantic and stylistic instability using:

- Embedding-based drift measurement
- Persona keyword retention
- Structural violation scoring
- Override detection

This project focuses on robustness, controllability, and behavioral stability in generative LLMs.

---

# Experimental Design

## Models Evaluated

- llama3:8b
- qwen2.5:1.5b
- phi

## Personas

1. Medieval Court Historian — archaic, ceremonial, narrative tone  
2. Sarcastic Stand-Up Comedian — informal, exaggerated, rhetorical  
3. Strict Physics Professor — structured, analytical, precise  

## Topics (5)

- Collapse of Civilizations  
- Why the Sky is Blue  
- Economic Inequality  
- Human Space Exploration  
- Artificial Intelligence  

## Attack Categories (20 Total)

- Override Instructions  
- Tone Corruption  
- Modernity Injection  
- Role Reassignment  
- Structural Disruption  

Each base persona response is subjected to all 20 adversarial attacks.

---

# Dataset Scale

| Component | Count |
|-----------|--------|
| Models | 3 |
| Personas | 3 |
| Topics | 5 |
| Attacks per Base Prompt | 20 |

### Total Generations

| Type | Count |
|------|--------|
| Base Outputs | 45 |
| Adversarial Outputs | 900 |
| **Total Generations** | **945** |

---

# Metrics

## 1. Embedding Drift Score

Drift = 1 − cosine_similarity(base, attacked)

Higher drift indicates greater semantic and stylistic deviation.

## 2. Persona Marker Retention

Retention = Attacked Keyword Density / Base Keyword Density

Lower retention indicates higher stylistic degradation.

## 3. Structural Violation Score

Detects forbidden stylistic markers such as:

- Emojis  
- Slang  
- Contractions  
- Excess punctuation  

Normalized between 0 and 1.

## 4. Override Rate

Binary detection of persona abandonment under direct override attacks.

---

# Key Results

## Drift by Model (Mean)

| Model | Avg Drift |
|--------|------------|
| llama3:8b | ~0.31 |
| qwen2.5:1.5b | ~0.33 |
| phi | ~0.39 |

**Insight:** Larger models demonstrate stronger persona stability under adversarial pressure.

---

## Drift by Persona

| Persona | Avg Drift |
|----------|------------|
| Comedian | ~0.40 |
| Historian | ~0.33 |
| Professor | ~0.29 |

**Insight:** Expressive personas are significantly more fragile than structured analytical personas.

---

## Drift by Attack Category

| Attack Category | Avg Drift |
|------------------|------------|
| Modernity Injection | ~0.36 |
| Structural Disruption | ~0.35 |
| Tone Corruption | ~0.35 |
| Role Reassignment | ~0.33 |
| Direct Override | ~0.31 |

**Insight:** Semantic contamination destabilizes personas more than direct override attempts.

---

## Distribution Analysis (Heavy-Tail Behavior)

- phi exhibits heavy right-tail drift, including catastrophic collapse cases (drift > 0.9).
- llama3:8b shows the narrowest distribution and lowest variance.

This indicates that smaller models exhibit episodic catastrophic instability under adversarial pressure.

---

# Generated Visualizations

The pipeline automatically produces:

- plots/drift_by_model.png  
- plots/override_rate.png  
- plots/drift_by_attack_category.png  
- plots/drift_by_persona.png  
- plots/drift_heatmap.png  
- plots/drift_distribution.png  

---

# How to Use This Repository

## 1. Clone Repository

```bash
git clone https://github.com/TheSkyBiz/llm-persona-drift-evaluation.git
cd llm-persona-drift-evaluation
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Install and Start Ollama

Download Ollama from: https://ollama.com

Pull required models:

```bash
ollama pull llama3:8b
ollama pull qwen2.5:1.5b
ollama pull phi
```

Ensure Ollama is running before executing scripts.

---

## 4. Run Evaluation Pipeline

From project root:

```bash
python -m src.generate_base
python -m src.generate_attacks
python -m src.compute_metrics
python -m src.plot_results
```

---

# Output Files

### Generated CSV Files

- outputs/base_outputs.csv  
- outputs/attacked_outputs.csv  
- outputs/results.csv  

### Generated Plots

- plots/*.png  

Raw CSV outputs are excluded via .gitignore and can be regenerated via the pipeline.

---

# Practical Implications

For production systems requiring tone consistency:

- Larger models reduce catastrophic persona collapse risk.
- Structured roles are inherently more stable.
- Semantic contamination is a stronger destabilization vector than direct override attempts.
- Smaller models exhibit higher variance and unpredictability.

---

# Future Improvements

- Statistical significance testing
- Temperature sensitivity sweep
- Token-length normalized drift
- Incremental checkpointing
- Cross-model persona transfer evaluation

---

# Conclusion

Persona Drift Arena demonstrates that adversarial persona stability is:

- Model-scale sensitive  
- Persona-type sensitive  
- Attack-category sensitive  
- Distributionally asymmetric  

This framework provides a reproducible and quantitative method for evaluating stylistic robustness in open-source LLMs.

---
