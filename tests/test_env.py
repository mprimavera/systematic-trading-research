import numpy as np
import pandas as pd


def main():
    # --- NumPy test ---
    arr = np.array([1, 2, 3, 4, 5])
    squared = arr ** 2
    print("NumPy array:", arr)
    print("NumPy squared:", squared)
    print("NumPy mean:", np.mean(arr))

    # --- Pandas test ---
    dates = pd.date_range(start="2024-01-01", periods=5, freq="D")
    df = pd.DataFrame({
        "price": [100, 102, 101, 105, 110]
    }, index=dates)

    df["returns"] = df["price"].pct_change()
    df["rolling_mean"] = df["price"].rolling(window=2).mean()

    print("\nPandas DataFrame:")
    print(df)

    print("\nSharpe-style metric (mean/std):",
          df["returns"].mean() / df["returns"].std())


if __name__ == "__main__":
    main()
