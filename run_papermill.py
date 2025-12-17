import papermill as pm
import os

os.makedirs("notebooks/runs", exist_ok=True)

pm.execute_notebook(
    "notebooks/preprocessing_and_eda.ipynb",
    "notebooks/runs/preprocessing_and_eda_run.ipynb",
    parameters=dict(
        USE_UCIMLREPO=False,
        RAW_ZIP_PATH="data/raw/PRSA2017_Data_20130301-20170228.zip",
        OUTPUT_CLEANED_PATH="data/processed/cleaned.parquet",
        LAG_HOURS=[1, 3, 24],
    ),
    language="python",
    kernel_name="beijing_env",
)

pm.execute_notebook(
    "notebooks/feature_preparation.ipynb",
    "notebooks/runs/feature_preparation_run.ipynb",
    parameters=dict(
        CLEANED_PATH="data/processed/cleaned.parquet",
        OUTPUT_DATASET_PATH="data/processed/dataset_for_clf.parquet",
        DROP_ROWS_WITHOUT_TARGET=True,
    ),
    language="python",
    kernel_name="beijing_env",
)

pm.execute_notebook(
    "notebooks/classification_modelling.ipynb",
    "notebooks/runs/classification_modelling_run.ipynb",
    parameters=dict(
        DATASET_PATH="data/processed/dataset_for_clf.parquet",
        CUTOFF="2017-01-01",
        METRICS_PATH="data/processed/metrics.json",
        PRED_SAMPLE_PATH="data/processed/predictions_sample.csv",
    ),
    language="python",
    kernel_name="beijing_env",
)

print("Đã chạy xong pipeline")
