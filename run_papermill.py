"""
Run the full notebook pipeline with Papermill (similar style to shopping_cart_analysis).

Pipeline:
  01 preprocessing_and_eda.ipynb
  02 feature_preparation.ipynb
  03 classification_modelling.ipynb

Outputs:
  data/processed/cleaned.parquet
  data/processed/dataset_for_clf.parquet
  data/processed/metrics.json
  data/processed/predictions_sample.csv
  notebooks/runs/*_run.ipynb
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import papermill as pm


# -----------------------------
# Global parameters (edit here)
# -----------------------------
USE_UCIMLREPO = True
RAW_ZIP_PATH = None  # e.g. "data/raw/PRSA2017_Data_20130301-20170228.zip"

LAG_HOURS = (1, 3, 24)

CUTOFF = "2017-01-01"


def _run_one(input_nb: Path, output_nb: Path, parameters: dict) -> None:
    output_nb.parent.mkdir(parents=True, exist_ok=True)
    pm.execute_notebook(
        input_path=str(input_nb),
        output_path=str(output_nb),
        parameters=parameters,
        log_output=True,
    )


def main() -> None:
    project_root = Path(__file__).resolve().parent
    nb_dir = project_root / "notebooks"
    runs_dir = nb_dir / "runs"

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    pipeline = [
        ("preprocessing_and_eda.ipynb", f"preprocessing_and_eda_run_{ts}.ipynb"),
        ("feature_preparation.ipynb", f"feature_preparation_run_{ts}.ipynb"),
        ("classification_modelling.ipynb", f"classification_modelling_run_{ts}.ipynb"),
    ]

    for in_name, out_name in pipeline:
        in_path = nb_dir / in_name
        out_path = runs_dir / out_name

        if in_name == "preprocessing_and_eda.ipynb":
            params = {
                "USE_UCIMLREPO": USE_UCIMLREPO,
                "RAW_ZIP_PATH": RAW_ZIP_PATH,
                "OUTPUT_CLEANED_PATH": "data/processed/cleaned.parquet",
                "LAG_HOURS": LAG_HOURS,
            }
        elif in_name == "feature_preparation.ipynb":
            params = {
                "CLEANED_PATH": "data/processed/cleaned.parquet",
                "OUTPUT_DATASET_PATH": "data/processed/dataset_for_clf.parquet",
                "DROP_ROWS_WITHOUT_TARGET": True,
            }
        else:
            params = {
                "DATASET_PATH": "data/processed/dataset_for_clf.parquet",
                "CUTOFF": CUTOFF,
                "METRICS_PATH": "data/processed/metrics.json",
                "PRED_SAMPLE_PATH": "data/processed/predictions_sample.csv",
            }

        print(f"[papermill] {in_name} -> {out_name}")
        _run_one(in_path, out_path, params)

    print("\nDone.")
    print("Check outputs in: data/processed/ and notebooks/runs/")


if __name__ == "__main__":
    main()
