# 🛡️ Network Intrusion Detection System (NIDS)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-FF9900?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-000000?style=for-the-badge)

## 📌 Overview
The **Network Intrusion Detection System (NIDS)** is an interactive web-based dashboard built to analyze network traffic and detect potential security threats. Leveraging various **Machine Learning algorithms** (including K-Means, Naive Bayes, and K-Nearest Neighbors), this Streamlit application evaluates and classifies network anomalies, providing an intuitive interface for monitoring network health and identifying malicious activities.

## 🏗️ Architecture & Data Flow

Below is the workflow of how network data is processed and evaluated by the ML models:

```mermaid
graph TD;
    A[Network Traffic Data] -->|Import| B[Data Preprocessing];
    B -->|Feature Extraction| C{Machine Learning Models};
    C -->|Algorithm Evaluation| D[Anomaly Classification];
    D -->|Results Display| E[Streamlit Dashboard];
    E -->|Visual Analytics| F[User / Security Analyst];

## Project contents

- `app.py` - Streamlit application to interact with the trained models.
- `train_and_save_models.py` - Script to train models and save them to the `models/` folder.
- `requirements.txt` - Python package dependencies required to run the project.
- `models/` - Directory containing serialized model files produced by training.
- `UNSW_NB15_training-set.csv` - Training dataset (UNSW-NB15).
- `UNSW_NB15_testing-set.csv` - Testing dataset (UNSW-NB15).
- Jupyter notebooks:
  - `1_kmeans_clustering.ipynb`
  - `2_knn_classification.ipynb`
  - `3_naive_bayes_classification.ipynb`
  - `comparison.ipynb`


## Quick start

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Train models (optional if pre-trained models exist in `models/`):

```powershell
python train_and_save_models.py
```

4. Run the Streamlit application:

```powershell
streamlit run app.py
```

## Notes and recommendations

- The training scripts may take significant time depending on available CPU and data size. Use a subset of the data for quick experiments.
- Review `requirements.txt` and pin versions if reproducible environments are required.
- Keep the `models/` directory in `.gitignore` for large files if you plan to store models in an external artifact store.

## Structure for contributions

- Use branches for features: `feature/<name>`
- Provide clear commit messages and tests for changed logic

## License

This project does not include a license file. Add a license if you plan to make the code public.
