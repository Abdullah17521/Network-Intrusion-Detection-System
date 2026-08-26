🛡️ Network Intrusion Detection System (NIDS)
📌 Overview
The Network Intrusion Detection System (NIDS) is an interactive web-based dashboard built to analyze network traffic and detect potential security threats. Leveraging various Machine Learning algorithms (including K-Means, Naive Bayes, and K-Nearest Neighbors), this Streamlit application evaluates and classifies network anomalies, providing an intuitive interface for monitoring network health and identifying malicious activities.

🏗️ Architecture & Data Flow
Below is the workflow of how network data is processed and evaluated by the ML models:

Code snippet
graph TD;
    A[Network Traffic Data] -->|Import| B[Data Preprocessing];
    B -->|Feature Extraction| C{Machine Learning Models};
    C -->|Algorithm Evaluation| D[Anomaly Classification];
    D -->|Results Display| E[Streamlit Dashboard];
    E -->|Visual Analytics| F[User / Security Analyst];
⚙️ Features
Real-time Evaluation: Test and compare different ML algorithms on network datasets.

Interactive Dashboard: Built with Streamlit for a user-friendly and responsive experience.

Anomaly Detection: Classifies traffic as normal or malicious to prevent intrusions.

🚀 Setup & Installation
1. Clone the repository:

Bash
git clone [https://github.com/M-Abdullah-Shahzad/Network-Intrusion-Detection-System.git](https://github.com/M-Abdullah-Shahzad/Network-Intrusion-Detection-System.git)
cd Network-Intrusion-Detection-System
2. Create a Virtual Environment (Recommended):

Bash
python -m venv venv
# On Windows use:
venv\Scripts\activate
# On Mac/Linux use:
source venv/bin/activate
3. Install the required dependencies:

Bash
pip install -r requirements.txt
4. Run the Streamlit Dashboard:

Bash
streamlit run app.py
📂 Project Structure
Plaintext
Network-Intrusion-Detection-System/
├── app.py                 # Main Streamlit dashboard application
├── models/                # Machine learning algorithms and pre-trained weights
├── data/                  # Network datasets for training and evaluation
├── requirements.txt       # Project dependencies
└── README.md
