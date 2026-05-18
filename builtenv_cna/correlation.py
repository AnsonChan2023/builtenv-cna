import pandas as pd

def compute_correlation(df, method="pearson", numeric_only=True):
    """
    Compute a correlation matrix from a pandas DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    method : str
        Correlation method: "pearson", "spearman", or "kendall".
    numeric_only : bool
        If True, only numeric columns are used.

    Returns
    -------
    pandas.DataFrame
        Correlation matrix.
    """

    if numeric_only:
        data = df.select_dtypes(include="number")
    else:
        data = df.copy()

    if data.shape[1] < 2:
        raise ValueError("At least two numeric columns are required to compute correlation.")

    return data.corr(method=method)
