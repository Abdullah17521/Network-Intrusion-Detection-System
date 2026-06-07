# Network Intrusion Detection System

This repository contains code, notebooks, data, and trained models for building and evaluating a network intrusion detection system (NIDS) using machine learning. The project focuses on preprocessing the UNSW-NB15 dataset, training several classification models, and saving models for later use in an application.

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

## Overview

This project shows a practical workflow for network intrusion detection using classical machine learning:

- Data loading and preprocessing of the UNSW-NB15 dataset
- Feature engineering and scaling
- Training multiple classifiers and comparing performance
- Saving and loading trained models for inference
- A simple Streamlit app for demonstration and manual testing

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
