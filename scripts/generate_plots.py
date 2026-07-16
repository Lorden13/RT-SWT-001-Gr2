import os
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns
from sentence_transformers import SentenceTransformer, util

# Define paths
base_dir = r"D:\fptu\ky5\swt\RT-SWT-001-Gr2"
data_path = os.path.join(base_dir, "data", "sample_100.csv")
zero_path = os.path.join(base_dir, "results", "full_zero_shot_100.csv")
few_path = os.path.join(base_dir, "results", "full_few_shot_100.csv")
cot_path = os.path.join(base_dir, "results", "full_cot_100.csv")
fig1_path = os.path.join(base_dir, "figures", "fig1_distribution.png")
fig2_path = os.path.join(base_dir, "figures", "fig2_comparison.png")

print("Loading datasets...")
df_gt = pd.read_csv(data_path).sort_values("ID").reset_index(drop=True)
df_zero = pd.read_csv(zero_path).sort_values("ID").reset_index(drop=True)
df_few = pd.read_csv(few_path).sort_values("ID").reset_index(drop=True)
df_cot = pd.read_csv(cot_path).sort_values("ID").reset_index(drop=True)

# Helper function to extract Gherkin and Python sections
def parse_output(text):
    if not isinstance(text, str):
        return "", ""
    lines = text.split("\n")
    gherkin_lines, python_lines = [], []
    current_section = None
    for line in lines:
        cleaned = line.strip().lower()
        if cleaned.startswith("gherkin:"):
            current_section = "gherkin"
            continue
        elif cleaned.startswith("python:"):
            current_section = "python"
            continue
        elif cleaned.startswith("feature:") and current_section is None:
            current_section = "gherkin"
        if current_section == "gherkin":
            gherkin_lines.append(line)
        elif current_section == "python":
            python_lines.append(line)
    return "\n".join(gherkin_lines).strip(), "\n".join(python_lines).strip()

print("Parsing Gherkin and Python content...")
gt_gherkin = df_gt["Manual Scenario"].fillna("").astype(str).tolist()
zero_gherkin = [parse_output(x)[0] for x in df_zero["Output"]]
few_gherkin = [parse_output(x)[0] for x in df_few["Output"]]
cot_gherkin = [parse_output(x)[0] for x in df_cot["Output"]]

zero_python = [parse_output(x)[1] for x in df_zero["Output"]]
few_python = [parse_output(x)[1] for x in df_few["Output"]]
cot_python = [parse_output(x)[1] for x in df_cot["Output"]]

# Check AST Parse Status
def check_ast(code):
    if not code: return 0
    try:
        ast.parse(code)
        return 1
    except SyntaxError:
        return 0

print("Calculating AST status...")
zero_ast = [check_ast(c) for c in zero_python]
few_ast = [check_ast(c) for c in few_python]
cot_ast = [check_ast(c) for c in cot_python]

# Calculate SBERT Cosine Similarity
print("Loading SBERT model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Encoding sentences...")
emb_gt = model.encode(gt_gherkin, convert_to_tensor=True)
emb_zero = model.encode(zero_gherkin, convert_to_tensor=True)
emb_few = model.encode(few_gherkin, convert_to_tensor=True)
emb_cot = model.encode(cot_gherkin, convert_to_tensor=True)

cos_zero, cos_few, cos_cot = [], [], []
for i in range(len(df_gt)):
    cos_zero.append(util.cos_sim(emb_gt[i], emb_zero[i]).item())
    cos_few.append(util.cos_sim(emb_gt[i], emb_few[i]).item())
    cos_cot.append(util.cos_sim(emb_gt[i], emb_cot[i]).item())

print("Plotting Fig 1: Cosine Similarity Distribution...")
# Set design aesthetics (sleek dark mode or clean academic light mode)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))

# Prepare data for plotting
plot_data = pd.DataFrame({
    "Zero-Shot": cos_zero,
    "Few-Shot": cos_few,
    "Chain-of-Thought": cos_cot
})

# Draw Box and Whisker Plot with individual points (jitter)
ax = sns.boxplot(data=plot_data, palette="Set2", width=0.5, showmeans=True,
                 meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"8"})
sns.stripplot(data=plot_data, color="black", alpha=0.3, jitter=0.2, size=4)

plt.axhline(y=0.80, color="red", linestyle="--", linewidth=1.5, label="Threshold (0.80)")
plt.title("Semantic Similarity (Cosine Similarity) Distribution (N=100)", fontsize=14, fontweight="bold", pad=15)
plt.ylabel("Cosine Similarity Score", fontsize=12)
plt.xlabel("Prompting Technique", fontsize=12)
plt.ylim(0.4, 1.05)
plt.legend(loc="lower left")

plt.tight_layout()
os.makedirs(os.path.dirname(fig1_path), exist_ok=True)
plt.savefig(fig1_path, dpi=300)
plt.close()
print(f"Successfully saved fig1_distribution.png at: {fig1_path}")

print("Plotting Fig 2: AST Parse Rate Comparison...")
plt.figure(figsize=(6, 5))

# Parse rates
rates = [np.mean(zero_ast) * 100, np.mean(few_ast) * 100, np.mean(cot_ast) * 100]
labels = ["Zero-Shot", "Few-Shot", "CoT"]

# Sleek bar chart
colors = ["#4c72b0", "#55a868", "#c44e52"]
bars = plt.bar(labels, rates, color=colors, width=0.4)

# Draw baseline/threshold
plt.axhline(y=85.0, color="red", linestyle="--", linewidth=1.5, label="Threshold (85%)")

# Add text labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 1, f"{height:.1f}%", ha="center", va="bottom", fontweight="bold")

plt.title("Executable Syntax Rate (AST Parse) (N=100)", fontsize=13, fontweight="bold", pad=15)
plt.ylabel("Success Rate (%)", fontsize=12)
plt.ylim(0, 110)
plt.legend(loc="lower left")

plt.tight_layout()
plt.savefig(fig2_path, dpi=300)
plt.close()
print(f"Successfully saved fig2_comparison.png at: {fig2_path}")
