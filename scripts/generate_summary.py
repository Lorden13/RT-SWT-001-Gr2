import os
import pandas as pd
import numpy as np
import ast
import scipy.stats as stats
from sentence_transformers import SentenceTransformer, util

# Define paths
base_dir = r"D:\fptu\ky5\swt\RT-SWT-001-Gr2"
data_path = os.path.join(base_dir, "data", "sample_100.csv")
zero_path = os.path.join(base_dir, "results", "full_zero_shot_100.csv")
few_path = os.path.join(base_dir, "results", "full_few_shot_100.csv")
cot_path = os.path.join(base_dir, "results", "full_cot_100.csv")
output_path = os.path.join(base_dir, "results", "summary.csv")

print("Loading datasets...")
df_gt = pd.read_csv(data_path)
df_zero = pd.read_csv(zero_path)
df_few = pd.read_csv(few_path)
df_cot = pd.read_csv(cot_path)

# Ensure data is sorted/aligned by ID
df_gt = df_gt.sort_values("ID").reset_index(drop=True)
df_zero = df_zero.sort_values("ID").reset_index(drop=True)
df_few = df_few.sort_values("ID").reset_index(drop=True)
df_cot = df_cot.sort_values("ID").reset_index(drop=True)

# Helper function to extract Gherkin and Python sections
def parse_output(text):
    if not isinstance(text, str):
        return "", ""
    
    lines = text.split("\n")
    gherkin_lines = []
    python_lines = []
    
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

print("Parsing outputs...")
# Extract Gherkin and Python for all rows
gt_gherkin = df_gt["Manual Scenario"].fillna("").astype(str).tolist()

zero_parsed = [parse_output(x) for x in df_zero["Output"]]
few_parsed = [parse_output(x) for x in df_few["Output"]]
cot_parsed = [parse_output(x) for x in df_cot["Output"]]

zero_gherkin = [x[0] for x in zero_parsed]
zero_python = [x[1] for x in zero_parsed]

few_gherkin = [x[0] for x in few_parsed]
few_python = [x[1] for x in few_parsed]

cot_gherkin = [x[0] for x in cot_parsed]
cot_python = [x[1] for x in cot_parsed]

# 1. Calculate AST Parse Rate
def check_ast(code):
    if not code:
        return 0
    try:
        ast.parse(code)
        return 1
    except SyntaxError:
        return 0

print("Checking AST Parse Status...")
zero_ast = [check_ast(code) for code in zero_python]
few_ast = [check_ast(code) for code in few_python]
cot_ast = [check_ast(code) for code in cot_python]

# 2. Calculate SBERT Cosine Similarity
print("Loading SBERT model (all-MiniLM-L6-v2)...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Encoding sentences...")
embeddings_gt = model.encode(gt_gherkin, convert_to_tensor=True)
embeddings_zero = model.encode(zero_gherkin, convert_to_tensor=True)
embeddings_few = model.encode(few_gherkin, convert_to_tensor=True)
embeddings_cot = model.encode(cot_gherkin, convert_to_tensor=True)

print("Calculating Cosine Similarity...")
cos_zero = []
cos_few = []
cos_cot = []

for i in range(len(df_gt)):
    sim_zero = util.cos_sim(embeddings_gt[i], embeddings_zero[i]).item()
    sim_few = util.cos_sim(embeddings_gt[i], embeddings_few[i]).item()
    sim_cot = util.cos_sim(embeddings_gt[i], embeddings_cot[i]).item()
    cos_zero.append(sim_zero)
    cos_few.append(sim_few)
    cos_cot.append(sim_cot)

cos_zero = np.array(cos_zero)
cos_few = np.array(cos_few)
cos_cot = np.array(cos_cot)

print(f"Zero-Shot Cosine Mean: {cos_zero.mean():.4f}")
print(f"Few-Shot Cosine Mean: {cos_few.mean():.4f}")
print(f"CoT Cosine Mean: {cos_cot.mean():.4f}")
print(f"Zero-Shot AST Mean: {np.mean(zero_ast):.4f}")
print(f"Few-Shot AST Mean: {np.mean(few_ast):.4f}")
print(f"CoT AST Mean: {np.mean(cot_ast):.4f}")

# 3. Statistical Tests
# One-sample Wilcoxon vs threshold 0.80
p_wilc_zero = stats.wilcoxon(cos_zero - 0.80, alternative="greater").pvalue
p_wilc_few = stats.wilcoxon(cos_few - 0.80, alternative="greater").pvalue
p_wilc_cot = stats.wilcoxon(cos_cot - 0.80, alternative="greater").pvalue

# One-sample Binomial vs threshold 85% (0.85)
zero_pass_count = sum(zero_ast)
few_pass_count = sum(few_ast)
cot_pass_count = sum(cot_ast)
n_total = len(df_gt)

# stats.binomtest was introduced in scipy 1.7.0, fall back to binom_test if necessary
try:
    p_binom_zero = stats.binomtest(zero_pass_count, n_total, 0.85, alternative="greater").pvalue
    p_binom_few = stats.binomtest(few_pass_count, n_total, 0.85, alternative="greater").pvalue
    p_binom_cot = stats.binomtest(cot_pass_count, n_total, 0.85, alternative="greater").pvalue
except AttributeError:
    p_binom_zero = stats.binom_test(zero_pass_count, n_total, 0.85, alternative="greater")
    p_binom_few = stats.binom_test(few_pass_count, n_total, 0.85, alternative="greater")
    p_binom_cot = stats.binom_test(cot_pass_count, n_total, 0.85, alternative="greater")

# Paired Wilcoxon (Comparisons)
p_paired_few_zero = stats.wilcoxon(cos_few, cos_zero).pvalue
p_paired_few_cot = stats.wilcoxon(cos_few, cos_cot).pvalue
p_paired_zero_cot = stats.wilcoxon(cos_zero, cos_cot).pvalue

# McNemar Test for syntax
def mcnemar_p(ast1, ast2):
    # Contingency table
    a = sum(1 for x, y in zip(ast1, ast2) if x == 1 and y == 1)
    b = sum(1 for x, y in zip(ast1, ast2) if x == 1 and y == 0)
    c = sum(1 for x, y in zip(ast1, ast2) if x == 0 and y == 1)
    d = sum(1 for x, y in zip(ast1, ast2) if x == 0 and y == 0)
    
    # Exact binomial test for McNemar (b vs c)
    total_disagreements = b + c
    if total_disagreements == 0:
        return 1.0
    try:
        p_val = stats.binomtest(b, total_disagreements, 0.5).pvalue
    except AttributeError:
        p_val = stats.binom_test(b, total_disagreements, 0.5)
    return p_val

p_mcnemar_few_zero = mcnemar_p(few_ast, zero_ast)
p_mcnemar_few_cot = mcnemar_p(few_ast, cot_ast)
p_mcnemar_zero_cot = mcnemar_p(zero_ast, cot_ast)

# Calculate Effect Sizes
# Cohen's d helper
def cohen_d_paired(x, y):
    diff = x - y
    return np.mean(diff) / np.std(diff, ddof=1) if np.std(diff, ddof=1) != 0 else 0

d_few_zero = cohen_d_paired(cos_few, cos_zero)
d_few_cot = cohen_d_paired(cos_few, cos_cot)
d_zero_cot = cohen_d_paired(cos_zero, cos_cot)

# One-sample Cohen's d vs 0.80
d_zero = (np.mean(cos_zero) - 0.80) / np.std(cos_zero, ddof=1)
d_few = (np.mean(cos_few) - 0.80) / np.std(cos_few, ddof=1)
d_cot = (np.mean(cos_cot) - 0.80) / np.std(cos_cot, ddof=1)

# Format rows for summary.csv
summary_rows = [
    # RQ1: Semantic Similarity vs threshold 0.80
    {"RQ": "RQ1", "Metric": "Cosine Similarity", "Technique/Comparison": "Zero-Shot", "Value": f"{cos_zero.mean():.4f}", "Threshold/Comparison": "0.80", "p-value": f"{p_wilc_zero:.4f}", "Effect Size": f"{d_zero:.4f}", "N": str(n_total), "Status": "Đạt" if cos_zero.mean() >= 0.80 and p_wilc_zero < 0.05 else "Không đạt"},
    {"RQ": "RQ1", "Metric": "Cosine Similarity", "Technique/Comparison": "Few-Shot", "Value": f"{cos_few.mean():.4f}", "Threshold/Comparison": "0.80", "p-value": f"{p_wilc_few:.4f}", "Effect Size": f"{d_few:.4f}", "N": str(n_total), "Status": "Đạt" if cos_few.mean() >= 0.80 and p_wilc_few < 0.05 else "Không đạt"},
    {"RQ": "RQ1", "Metric": "Cosine Similarity", "Technique/Comparison": "Chain-of-Thought", "Value": f"{cos_cot.mean():.4f}", "Threshold/Comparison": "0.80", "p-value": f"{p_wilc_cot:.4f}", "Effect Size": f"{d_cot:.4f}", "N": str(n_total), "Status": "Đạt" if cos_cot.mean() >= 0.80 and p_wilc_cot < 0.05 else "Không đạt"},
    
    # RQ2: AST Parse Rate vs threshold 85%
    {"RQ": "RQ2", "Metric": "AST Parse Rate", "Technique/Comparison": "Zero-Shot", "Value": f"{np.mean(zero_ast):.4f}", "Threshold/Comparison": "0.85", "p-value": f"{p_binom_zero:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Đạt" if np.mean(zero_ast) >= 0.85 and p_binom_zero < 0.05 else "Không đạt"},
    {"RQ": "RQ2", "Metric": "AST Parse Rate", "Technique/Comparison": "Few-Shot", "Value": f"{np.mean(few_ast):.4f}", "Threshold/Comparison": "0.85", "p-value": f"{p_binom_few:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Đạt" if np.mean(few_ast) >= 0.85 and p_binom_few < 0.05 else "Không đạt"},
    {"RQ": "RQ2", "Metric": "AST Parse Rate", "Technique/Comparison": "Chain-of-Thought", "Value": f"{np.mean(cot_ast):.4f}", "Threshold/Comparison": "0.85", "p-value": f"{p_binom_cot:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Đạt" if np.mean(cot_ast) >= 0.85 and p_binom_cot < 0.05 else "Không đạt"},
    
    # RQ3: Comparisons Semantic
    {"RQ": "RQ3 (Semantic)", "Metric": "Cosine Similarity", "Technique/Comparison": "Few-Shot vs Zero-Shot", "Value": f"{cos_few.mean():.4f} vs {cos_zero.mean():.4f}", "Threshold/Comparison": "Paired", "p-value": f"{p_paired_few_zero:.4f}", "Effect Size": f"{d_few_zero:.4f}", "N": str(n_total), "Status": "Có ý nghĩa" if p_paired_few_zero < 0.05 else "Không ý nghĩa"},
    {"RQ": "RQ3 (Semantic)", "Metric": "Cosine Similarity", "Technique/Comparison": "Few-Shot vs CoT", "Value": f"{cos_few.mean():.4f} vs {cos_cot.mean():.4f}", "Threshold/Comparison": "Paired", "p-value": f"{p_paired_few_cot:.4f}", "Effect Size": f"{d_few_cot:.4f}", "N": str(n_total), "Status": "Có ý nghĩa" if p_paired_few_cot < 0.05 else "Không ý nghĩa"},
    {"RQ": "RQ3 (Semantic)", "Metric": "Cosine Similarity", "Technique/Comparison": "Zero-Shot vs CoT", "Value": f"{cos_zero.mean():.4f} vs {cos_cot.mean():.4f}", "Threshold/Comparison": "Paired", "p-value": f"{p_paired_zero_cot:.4f}", "Effect Size": f"{d_zero_cot:.4f}", "N": str(n_total), "Status": "Có ý nghĩa" if p_paired_zero_cot < 0.05 else "Không ý nghĩa"},
    
    # RQ3: Comparisons Syntax
    {"RQ": "RQ3 (Syntax)", "Metric": "AST Parse Rate", "Technique/Comparison": "Few-Shot vs Zero-Shot", "Value": f"{np.mean(few_ast):.4f} vs {np.mean(zero_ast):.4f}", "Threshold/Comparison": "McNemar", "p-value": f"{p_mcnemar_few_zero:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Có ý nghĩa" if p_mcnemar_few_zero < 0.05 else "Không ý nghĩa"},
    {"RQ": "RQ3 (Syntax)", "Metric": "AST Parse Rate", "Technique/Comparison": "Few-Shot vs CoT", "Value": f"{np.mean(few_ast):.4f} vs {np.mean(cot_ast):.4f}", "Threshold/Comparison": "McNemar", "p-value": f"{p_mcnemar_few_cot:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Có ý nghĩa" if p_mcnemar_few_cot < 0.05 else "Không ý nghĩa"},
    {"RQ": "RQ3 (Syntax)", "Metric": "AST Parse Rate", "Technique/Comparison": "Zero-Shot vs CoT", "Value": f"{np.mean(zero_ast):.4f} vs {np.mean(cot_ast):.4f}", "Threshold/Comparison": "McNemar", "p-value": f"{p_mcnemar_zero_cot:.4f}", "Effect Size": "—", "N": str(n_total), "Status": "Có ý nghĩa" if p_mcnemar_zero_cot < 0.05 else "Không ý nghĩa"}
]

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"Successfully generated summary.csv at: {output_path}")
