# builtenv-cna

Correlation Network Analysis (CNA) framework for sustainable built environment and construction management research.

---

# Overview

`builtenv-cna` is a Python-based analytical framework for transforming correlation matrices into graph-based network structures.

The framework supports:

- correlation matrix generation
- correlation network construction
- heatmap visualization
- network visualization
- node-level network metrics
- threshold sensitivity analysis
- Gephi-compatible GEXF export

---

# Research Motivation

Construction management and sustainable built environment studies commonly rely on the below research methodologies with several limitations:

- Regression analysis: assume linear relationships between independent and dependent variables and predict their structure
- Structural Equation Modeling (SEM): assume a predefined causal relationship
- Principal Component Analysis (PCA): reduce multiple variables into factors but can hide network positions
- Descriptive correlation analysis: summarise mean, median, ranking and standard deviation, but does not show the system relationships among variables
- Social Network Analysis (SNA): variables are usually about stakholders and organisations but not the variable itself

However, these approaches often treat variables as isolated predictors rather than interconnected system components as shown in this table:

 Aspect | Regression | SEM | PCA | SNA | Proposed CNA Framework |
|---|---|---|---|---|---|
| Relationship focus | 🎯 Predictor–outcome | 🎯 Causal pathways | 📊 Variance structure | 👥 Stakeholder relationships | 🔗 Emergent variable correlations |
| Captures system interdependency | ⚠️ Limited | 🟡 Moderate | ⚠️ Partial | ⚠️ Social ties only | ✅ Strong |
| Requires predefined model | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Identifies influential variables | ⚠️ Limited | 🟡 Moderate | ❌ No | ✅ Yes | ✅ Centrality metrics |
| Detects hidden clusters/modules | ❌ No | ⚠️ Partial | ✅ Yes | ⚠️ Partial | ✅ Community detection |
| Visualization & network analysis | ⚠️ Basic plots | ⚠️ Moderate | ⚠️ Basic plots | ✅ Network visualization | ✅ Heatmap + network + Gephi |
| Typical use in construction research | ✅ Very common | ✅ Very common | ✅ Common | 🟡 Stakeholder-focused | 🚀 Emerging system-level approach |

This project introduces a Correlation Network Analysis (CNA) framework where:

- variables are represented as nodes
- correlations are represented as weighted edges
- network metrics reveal influential variables and structural patterns
- Gephi integration enables advanced graph-theoretic analysis

Unlike traditional Social Network Analysis (SNA) in construction management, which typically focuses on stakeholder relationships, this framework models quantitative sustainability and performance variables as interconnected systems.

---

# Features

## Correlation Analysis

```python
compute_correlation(df)
```

Supports:

- Pearson correlation
- Spearman correlation
- Kendall correlation

---

## Correlation Network Construction

```python
build_correlation_network(corr_matrix, threshold=0.3)
```

Features:

- weighted edges
- positive and negative edge signs
- threshold-based filtering
- network-ready graph structure

---

## Network Metrics

```python
calculate_network_metrics(G)
```

Calculates:

- degree centrality
- weighted strength
- betweenness centrality
- closeness centrality
- clustering coefficient
- eigenvector centrality

---

## Threshold Sensitivity Analysis (optional)

```python
threshold_sensitivity(corr_matrix)
```

Evaluates:

- network density
- edge count
- connected components
- structural changes across thresholds

---

## Gephi Export (export to Gephi software for network analysis)

```python
export_to_gephi(G)
```

Exports networks in `.gexf` format for advanced analysis in Gephi.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/builtenv-cna.git
```

## Enter the repository

```bash
cd builtenv-cna
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Example Workflow

```python
import pandas as pd

from builtenv_cna import (
    compute_correlation,
    build_correlation_network,
    calculate_network_metrics,
    threshold_sensitivity,
    plot_heatmap,
    plot_network,
    export_to_gephi
)

# Load dataset
df = pd.read_csv("Data_All.csv")

# Step 1: Correlation matrix
corr = compute_correlation(df)

# Step 2: Heatmap visualization
plot_heatmap(corr)

# Step 3: Build correlation network
G = build_correlation_network(
    corr,
    threshold=0.3
)

# Step 4: Network metrics
metrics = calculate_network_metrics(G)

print(metrics)

# Step 5: Threshold sensitivity analysis
sensitivity = threshold_sensitivity(corr)

print(sensitivity)

# Step 6: Visualize network
plot_network(G)

# Step 7: Export to Gephi
export_to_gephi(G, "cna_network.gexf")
```

---

# Recommended Research Workflow

1. Prepare sustainability variables, for example, survey responses.
2. Compute correlation matrix of the variables under study.
3. Generate correlation heatmap.
4. Transform correlations into network structure.
5. Calculate network metrics.
6. Evaluate threshold sensitivity.
7. Export network to Gephi.
8. Perform advanced graph analysis.
9. Interpret central variables and modular structures.

---

# Suggested Applications

- sustainable built environment analysis
- Life Cycle Assessment (LCA)
- Building Information Modeling (BIM)
- carbon emission studies
- sustainability indicator analysis
- infrastructure systems
- complex systems analysis

---

# Research Contribution

This framework introduces Correlation Network Analysis (CNA) into sustainable built environment and construction management research through a reproducible Python–Gephi workflow.

The framework enables:

- system-level interpretation of sustainability variables
- graph-based analysis of interdependencies
- identification of influential variables and clusters
- reproducible network-science workflows for construction datasets

---

# Limitations

Correlation Network Analysis identifies statistical association rather than causation.

Threshold selection influences network structure and should be justified or evaluated through sensitivity analysis.

---

# Software Stack

- Python
- Pandas
- NetworkX
- Matplotlib
- Seaborn
- Gephi

---

# License

MIT License
