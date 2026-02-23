# src/plot_results.py

import pandas as pd
import matplotlib.pyplot as plt
import os

RESULTS_PATH = "outputs/results.csv"
os.makedirs("plots", exist_ok=True)

df = pd.read_csv(RESULTS_PATH)

# Drift by model
drift_by_model = df.groupby("model")["drift"].mean()

plt.figure()
drift_by_model.plot(kind="bar")
plt.title("Average Drift by Model")
plt.ylabel("Drift (1 - cosine similarity)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/drift_by_model.png")
plt.close()

# Override rate by model
override_rate = df.groupby("model")["override_flag"].mean()

plt.figure()
override_rate.plot(kind="bar")
plt.title("Override Rate by Model")
plt.ylabel("Override Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/override_rate.png")
plt.close()

# Drift by attack category
drift_by_category = df.groupby("attack_category")["drift"].mean()

plt.figure()
drift_by_category.plot(kind="bar")
plt.title("Average Drift by Attack Category")
plt.ylabel("Drift")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/drift_by_attack_category.png")
plt.close()

#Drift by Persona
drift_by_persona = df.groupby("persona")["drift"].mean()

plt.figure()
drift_by_persona.plot(kind="bar")
plt.title("Average Drift by Persona")
plt.ylabel("Drift")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/drift_by_persona.png")
plt.close()

# Heatmap of drift by persona and model
import seaborn as sns

pivot = df.pivot_table(
    values="drift",
    index="persona",
    columns="model",
    aggfunc="mean"
)

plt.figure()
sns.heatmap(pivot, annot=True, cmap="coolwarm")
plt.title("Drift Heatmap (Persona × Model)")
plt.tight_layout()
plt.savefig("plots/drift_heatmap.png")
plt.close()

# KDE plot of drift distribution by model
plt.figure()
for model in df["model"].unique():
    subset = df[df["model"] == model]["drift"]
    subset.plot(kind="kde", label=model)

plt.title("Drift Distribution by Model")
plt.xlabel("Drift")
plt.legend()
plt.tight_layout()
plt.savefig("plots/drift_distribution.png")
plt.close()

print("Plots saved in plots/")