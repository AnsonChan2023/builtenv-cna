import pandas as pd

from builtenv_cna import (
    compute_correlation,
    build_correlation_network,
    calculate_network_metrics,
    threshold_sensitivity,
    plot_heatmap,
    plot_network,
    export_to_gephi,
)

# Load dataset
df = pd.read_csv("data/sample_data.csv")

# Step 1: Compute correlation matrix
corr = compute_correlation(df)

# Step 2: Plot heatmap
plot_heatmap(corr)

# Step 3: Build correlation network
G = build_correlation_network(corr, threshold=0.3)

# Step 4: Calculate network metrics
metrics = calculate_network_metrics(G)
print(metrics)

# Step 5: Run threshold sensitivity analysis
sensitivity = threshold_sensitivity(corr)
print(sensitivity)

# Step 6: Plot network
plot_network(G)

# Step 7: Export to Gephi
export_to_gephi(G, "cna_network.gexf")
