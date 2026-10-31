
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"


def prepare_powerbi_data():
    # Load raw sensor measurements
    ps1 = pd.read_csv(
        RAW_DIR / "PS1.txt",
        sep=r"\s+",
        header=None,
    )

    profile = pd.read_csv(
        RAW_DIR / "profile.txt",
        sep=r"\s+",
        header=None,
    )

    # Calculate summary statistics for each cycle
    summary = pd.DataFrame({
        "cycle": range(1, len(ps1) + 1),
        "pressure_mean_bar": ps1.mean(axis=1),
        "pressure_min_bar": ps1.min(axis=1),
        "pressure_max_bar": ps1.max(axis=1),
        "pressure_std_bar": ps1.std(axis=1),
    })

    # Add component condition information
    profile.columns = [
        "cooler_condition_pct",
        "valve_condition_pct",
        "pump_leakage",
        "accumulator_pressure_bar",
        "stable_flag",
    ]

    summary = pd.concat(
        [summary, profile.reset_index(drop=True)],
        axis=1,
    )

    # Save the prepared dataset
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "ps1_cycle_summary.csv"
    summary.to_csv(output_file, index=False)

    print("Output file:", output_file)
    print("Dataset shape:", summary.shape)
    print(summary.head())


if __name__ == "__main__":
    prepare_powerbi_data()