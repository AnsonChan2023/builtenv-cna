import pandas as pd
import networkx as nx

from .network import build_correlation_network


def calculate_network_metrics(G):
    """
    Calculate basic network metrics for a correlation network.
    """

    if G.number_of_nodes() == 0:
        return pd.DataFrame()

    degree = dict(G.degree())

    strength = {
        node: sum(data.get("abs_weight", abs(data.get("weight", 1))) for _, _, data in G.edges(node, data=True))
        for node in G.nodes()
    }

    betweenness = nx.betweenness_centrality(G, weight="distance", normalized=True)
    closeness = nx.closeness_centrality(G, distance="distance")
    clustering = nx.clustering(G, weight="abs_weight")

    try:
        eigenvector = nx.eigenvector_centrality(G, weight="abs_weight", max_iter=1000)
    except Exception:
        eigenvector = {node: None for node in G.nodes()}

    rows = []

    for node in G.nodes():
        rows.append(
            {
                "node": node,
                "degree": degree.get(node, 0),
                "strength": strength.get(node, 0),
                "betweenness": betweenness.get(node, 0),
                "closeness": closeness.get(node, 0),
                "clustering": clustering.get(node, 0),
                "eigenvector": eigenvector.get(node, None),
            }
        )

    return pd.DataFrame(rows).sort_values(by="strength", ascending=False)


def threshold_sensitivity(corr_matrix, thresholds=(0.2, 0.3, 0.4, 0.5)):
    """
    Run threshold sensitivity analysis.
    """

    rows = []

    for threshold in thresholds:
        G = build_correlation_network(corr_matrix, threshold=threshold)

        rows.append(
            {
                "threshold": threshold,
                "nodes": G.number_of_nodes(),
                "edges": G.number_of_edges(),
                "density": nx.density(G),
                "components": nx.number_connected_components(G) if G.number_of_nodes() > 0 else 0,
            }
        )

    return pd.DataFrame(rows)
