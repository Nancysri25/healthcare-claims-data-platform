from pathlib import Path
import pandas as pd

def read_csv(file_path: Path) -> pd.DataFrame:
    """Read a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def write_csv(df: pd.DataFrame, file_path: Path) -> None:
    """Write a DataFrame to a CSV file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)