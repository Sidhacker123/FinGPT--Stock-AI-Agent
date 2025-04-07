
import pandas as pd

def summarize_csv(file):
    df = pd.read_csv(file)
    summary = df.describe().to_string()
    return summary
