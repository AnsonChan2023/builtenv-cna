import pandas as pd
import networkx as nx

def export_to_gephi(G, filename="cna_network.gexf"):
    """
    Export a NetworkX graph to a Gephi-compatible GEXF file.
    """

    nx.write_gexf(G, filename)
    print(f"Network exported to {filename}")


def export_edges_csv(G, filename="cna_edges.csv"):
    """
    Export network edges to CSV.
    """

    edges = []

    for source, target, data in G.edges(data=True):
        edges.append(
            {
                "source": source,
                "target": target,
                "weight": data.get("weight"),
                "abs_weight": data.get("abs_weight"),
                "sign": data.get("sign"),
            }
        )

    pd.DataFrame(edges).to_csv(filename, index=False)
    print(f"Edges exported to {filename}")


def export_metrics_csv(metrics_df, filename="cna_metrics.csv"):
    """
    Export network metrics table to CSV.
    """

    metrics_df.to_csv(filename, index=False)
    print(f"Metrics exported to {filename}")
