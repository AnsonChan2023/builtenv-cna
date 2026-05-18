import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

def plot_heatmap(corr_matrix, title="Correlation Heatmap"):
    """
    Plot a correlation heatmap.
    """

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8, "label": "Correlation coefficient"},
    )

    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_network(G, title="Correlation Network"):
    """
    Plot a correlation network using NetworkX.
    """

    plt.figure(figsize=(12, 10))

    pos = nx.spring_layout(G, seed=42)

    node_sizes = [500 + 150 * G.degree(node) for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10)

    edge_labels = nx.get_edge_attributes(G, "weight")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels={edge: f"{value:.2f}" for edge, value in edge_labels.items()},
        font_size=8,
    )

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
