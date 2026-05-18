import pandas as pd
import networkx as nx

#threshold value is determined based on literature review; sensitivity analysis is NOT the scope of this work
def build_correlation_network(corr_matrix, threshold=0.3):
    """
    Build a correlation network from a correlation matrix.

    Nodes are variables.
    Edges are correlations whose absolute value is greater than or equal to the threshold.

    Parameters
    ----------
    corr_matrix : pandas.DataFrame
        Correlation matrix.
    threshold : float
        Minimum absolute correlation value required to create an edge.

    Returns
    -------
    networkx.Graph
        Correlation network.
    """

    if not isinstance(corr_matrix, pd.DataFrame):
        raise TypeError("corr_matrix must be a pandas DataFrame.")

    G = nx.Graph()

    variables = list(corr_matrix.columns)

    # Add all variables as nodes
    for variable in variables:
        G.add_node(str(variable))

    # Add edges
    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            source = variables[i]
            target = variables[j]
            weight = corr_matrix.loc[source, target]

            if pd.isna(weight):
                continue

            weight = float(weight)
            abs_weight = abs(weight)

            if abs_weight >= threshold:
                G.add_edge(
                    str(source),
                    str(target),
                    weight=weight,
                    abs_weight=abs_weight,
                    sign="positive" if weight >= 0 else "negative",
                    distance=1 / abs_weight if abs_weight > 0 else 999999,
                )

    return G
