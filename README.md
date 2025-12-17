# Beijing Air Quality — Classification Pipeline (Papermill)

Bài toán: phân lớp chất lượng không khí theo **AQI class** (6 lớp) dựa trên **PM2.5 24h mean** (làm nhãn),
còn feature dùng các chất khác + khí tượng + đặc trưng thời gian/lag (không dùng PM2.5 để tránh leakage).

## Project Structure

    beijing_air_quality_classification/
    ├── data/
    │   ├── raw/
    │   └── processed/
    │       ├── cleaned.parquet
    │       ├── dataset_for_clf.parquet
    │       ├── metrics.json
    │       └── predictions_sample.csv
    ├── notebooks/
    │   ├── preprocessing_and_eda.ipynb
    │   ├── feature_preparation.ipynb
    │   ├── classification_modelling.ipynb
    │   └── runs/
    ├── src/
    │   └── classification_library.py
    ├── run_papermill.py
    └── requirements.txt

## Run

    pip install -r requirements.txt
    python run_papermill.py

## Notes

- Nếu `USE_UCIMLREPO=True` thì cần internet để tải dataset từ UCI bằng `ucimlrepo`.
- Nếu bạn tải ZIP thủ công, đặt vào `data/raw/` và set `RAW_ZIP_PATH` trong `run_papermill.py`.
