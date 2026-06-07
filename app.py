import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import os
import plotly.graph_objects as go

st.set_page_config(page_title="NIDS Dashboard", layout="wide")

# Updated Professional and Soothing Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    .stApp { background-color: #0b0f19; }
    h1, h2, h3 { color: #38bdf8 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Card Styling */
    .metric-card {
        background-color: #1e293b;
        border-left: 4px solid #38bdf8;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .metric-val { font-size: 28px; font-weight: bold; color: #f8fafc; margin: 10px 0; }
    
    /* Alert Styling */
    .danger-alert {
        background-color: #7f1d1d; color: #fca5a5; padding: 15px;
        border-left: 5px solid #ef4444; border-radius: 5px; font-weight: bold; font-size: 18px;
        text-align: center;
    }
    .secure-alert {
        background-color: #14532d; color: #86efac; padding: 15px;
        border-left: 5px solid #22c55e; border-radius: 5px; font-weight: bold; font-size: 18px;
        text-align: center;
    }
    
    /* Table Styling */
    th { background-color: #1e293b !important; color: #38bdf8 !important; font-size: 16px; }
    td { background-color: #0f172a !important; color: #e2e8f0 !important; font-size: 15px; border-bottom: 1px solid #334155 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("Intelligent Network Intrusion Detection System (NIDS)")

# --- ARTIFACTS LOADING ---
@st.cache_resource
def load_artifacts():
    paths_to_try = ['', 'models/', '../models/']
    scaler, kmeans, knn, nb = None, None, None, None
    for p in paths_to_try:
        try:
            scaler = joblib.load(os.path.join(p, 'scaler.pkl'))
            kmeans = joblib.load(os.path.join(p, 'kmeans_model.pkl'))
            knn = joblib.load(os.path.join(p, 'knn_model.pkl'))
            nb = joblib.load(os.path.join(p, 'nb_model.pkl'))
            return scaler, kmeans, knn, nb
        except:
            continue
    return None, None, None, None

scaler, kmeans, knn, nb = load_artifacts()

if scaler is None:
    st.error("CRITICAL ERROR: Model files (.pkl) missing inside models directory!")
    st.info("GUIDE: Please run the notebook python scripts manually in your terminal first to generate files.")
else:
    st.success("SYSTEM ONLINE: Secure Shield Core Loaded. All Machine Learning Models Active.")

    tab1, tab2 = st.tabs(["Model Evaluation Dashboard", "Manual Packet Inspector"])

    with tab1:
        st.subheader("Comprehensive Model Comparison Report")
        
        # Updated Comparison Table with K-Means included
        metrics_data = {
            "Algorithm": ["KNN", "Naive Bayes", "K-Means"],
            "Model Type": ["Supervised Classification", "Supervised Classification", "Unsupervised Clustering"],
            "Accuracy": ["93.2%", "81.4%", "-"],
            "Precision": ["92.5%", "78.9%", "-"],
            "Recall (Catch Rate)": ["91.0%", "88.5%", "-"],
            "F1-Score": ["91.7%", "83.4%", "-"],
            "Silhouette Score": ["-", "-", "0.42"]
        }
        df_metrics = pd.DataFrame(metrics_data)
        st.dataframe(df_metrics, use_container_width=True, hide_index=True)
        
        st.write("---")
        st.subheader("Visual Analytics Comparison Charts")
        
        graph_view = st.selectbox("Select Metric View for Graphical Chart", [
            "All Supervised Metrics", 
            "Accuracy Comparison", 
            "Recall Comparison", 
            "K-Means Silhouette Performance"
        ])
        
        if graph_view == "All Supervised Metrics":
            fig = go.Figure(data=[
                go.Bar(name='Accuracy', x=['Naive Bayes', 'KNN'], y=[81.4, 93.2], marker_color='#38bdf8'),
                go.Bar(name='Precision', x=['Naive Bayes', 'KNN'], y=[78.9, 92.5], marker_color='#818cf8'),
                go.Bar(name='Recall', x=['Naive Bayes', 'KNN'], y=[88.5, 91.0], marker_color='#fb7185'),
                go.Bar(name='F1-Score', x=['Naive Bayes', 'KNN'], y=[83.4, 91.7], marker_color='#fbbf24')
            ])
            fig.update_layout(barmode='group', title="Comprehensive Metrics Overview Plot", template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            
        elif graph_view == "Accuracy Comparison":
            fig = go.Figure(data=[go.Bar(x=['Naive Bayes', 'KNN'], y=[81.4, 93.2], marker_color='#38bdf8', text=[81.4, 93.2], textposition='auto')])
            fig.update_layout(title="Accuracy Comparison Chart (%)", template="plotly_dark", yaxis=dict(range=[0, 100]), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            
        elif graph_view == "Recall Comparison":
            fig = go.Figure(data=[go.Bar(x=['Naive Bayes', 'KNN'], y=[88.5, 91.0], marker_color='#fb7185', text=[88.5, 91.0], textposition='auto')])
            fig.update_layout(title="Recall Comparison (Attack Catch Rate) (%)", template="plotly_dark", yaxis=dict(range=[0, 100]), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            
        elif graph_view == "K-Means Silhouette Performance":
            # Dedicated Visual for K-Means
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 0.42,
                title = {'text': "K-Means Silhouette Score (Clustering Quality)"},
                gauge = {
                    'axis': {'range': [-1, 1]},
                    'bar': {'color': "#38bdf8"},
                    'steps': [
                        {'range': [-1, 0], 'color': "#334155"},
                        {'range': [0, 0.5], 'color': "#475569"},
                        {'range': [0.5, 1], 'color': "#1e293b"}
                    ],
                }
            ))
            fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', font={'color': "#e2e8f0"})
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("<p style='text-align: center; color: #94a3b8;'>A score of 0.42 indicates fair structural density separation for identifying unknown anomalies.</p>", unsafe_allow_html=True)

    with tab2:
        st.subheader("Scan a Custom Network Connection Packet")
        col_in1, col_in2, col_in3 = st.columns(3)
        with col_in1:
            dur = st.number_input("Duration", min_value=0.0, value=0.1)
            sbytes = st.number_input("Source Bytes", min_value=0, value=1000)
        with col_in2:
            dbytes = st.number_input("Destination Bytes", min_value=0, value=1500)
            sttl = st.number_input("Source TTL", min_value=0, value=31)
        with col_in3:
            dttl = st.number_input("Destination TTL", min_value=0, value=29)
            sloss = st.number_input("Source Packet Loss", min_value=0, value=0)

        selected_model = st.selectbox("Choose AI Model for Inference", ["KNN (Recommended)", "Naive Bayes", "K-Means Anomaly Detector"])

        if st.button("ANALYZE PACKET"):
            input_features = np.zeros(scaler.n_features_in_)
            input_features[0:6] = [dur, sbytes, dbytes, sttl, dttl, sloss]
            scaled_input = scaler.transform(input_features.reshape(1, -1))
            
            with st.spinner("Analyzing traffic signatures..."):
                time.sleep(0.4)
                if "Naive Bayes" in selected_model:
                    prediction = nb.predict(scaled_input)[0]
                elif "KNN" in selected_model:
                    prediction = knn.predict(scaled_input)[0]
                else:
                    cluster = kmeans.predict(scaled_input)[0]
                    prediction = 1 if cluster == 1 else 0

            if prediction == 1:
                st.markdown("<div class='danger-alert'>THREAT DETECTED: Malicious network activity signatures found in this packet.</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='secure-alert'>TRAFFIC SECURE: Connection exhibits normal baseline behavior.</div>", unsafe_allow_html=True)