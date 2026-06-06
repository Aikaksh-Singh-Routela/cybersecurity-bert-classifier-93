# 🛡️ Cybersecurity Alert Classifier

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![BERT](https://img.shields.io/badge/BERT-Fine--tuned-orange.svg)](https://huggingface.co/docs/transformers/model_doc/bert)
[![Hugging Face](https://img.shields.io/badge/🤗-Transformers-yellow.svg)](https://huggingface.co/)
[![Accuracy](https://img.shields.io/badge/Accuracy-92.86%25-green.svg)]()

## 📋 Overview

A **fine-tuned BERT model** that classifies cybersecurity alerts into **5 threat categories** with **92.86% accuracy**.

## 🔗 Links

- **Hugging Face Model**: [View Model](https://huggingface.co/Aikaksh-Singh-Routela/cybersecurity-bert-model)
- **Live Demo**: [Try Demo](https://huggingface.co/spaces/Aikaksh-Singh-Routela/cybersecurity-alert-classifier-streamlit)
- **GitHub**: [Source Code](https://github.com/Aikaksh-Singh-Routela/cybersecurity-bert-classifier-93)

### Key Features

| Feature | Description |
|---------|-------------|
| **🎯 5-Class Classification** | Identifies specific threat types |
| **🔒 Security Focused** | Trained on real cybersecurity alerts |
| **🚀 High Accuracy** | 92.86% on test dataset |
| **⚡ Fast Inference** | Sub-second classification |
| **📦 Easy Integration** | Simple pipeline API |

## 🏗️ Threat Categories

| Category | Description | Example Alert |
|----------|-------------|---------------|
| **🦠 Ransomware** | File encryption threats | "Files encrypted with .locked extension" |
| **⚡ DDoS** | Distributed denial of service | "Traffic spike from 10,000+ IPs" |
| **👤 Insider Threat** | Internal security risks | "Employee accessing unauthorized data" |
| **🌐 Web Attack** | Web-based exploits | "SQL injection detected in login form" |
| **✅ Benign** | Normal activity | "Regular backup completed successfully" |

## 🏗️ Model Architecture

Security Alert Text
↓
BERT Tokenizer
↓
Fine-tuned BERT Model
↓
Classification Head
↓
Threat Category Prediction
(5 Classes)


## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Accuracy** | 92.86% |
| **Precision** | 92.5% |
| **Recall** | 92.1% |
| **F1 Score** | 92.3% |
| **Classes** | 5 (Ransomware, DDoS, Insider Threat, Web Attack, Benign) |

## 🚀 Live Demo

Try the model instantly on Hugging Face Spaces.

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Aikaksh-Singh-Routela/cybersecurity-alert-classifier.git
cd cybersecurity-alert-classifier

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt

from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline(
    "text-classification",
    model="Aikaksh-Singh-Routela/cybersecurity-bert-model"
)

# Test with example alerts
alerts = [
    "Ransomware detected: Files are being encrypted with .locked extension",
    "DDoS attack: Traffic volume increased by 1000% from multiple IPs",
    "Normal user login from corporate network"
]

for alert in alerts:
    result = classifier(alert)
    print(f"Alert: {alert[:50]}...")
    print(f"Threat Type: {result[0]['label']}")
    print(f"Confidence: {result[0]['score']:.2%}")
    print("-" * 50)

python cybersecurity_bert_93percent.py

Alert: Ransomware detected: Files are being encrypted...
Threat Type: RANSOMWARE
Confidence: 94.50%
--------------------------------------------------
Alert: DDoS attack: Traffic volume increased...
Threat Type: DDOS
Confidence: 91.20%
--------------------------------------------------
Alert: Normal user login from corporate network...
Threat Type: BENIGN
Confidence: 96.80%
--------------------------------------------------

cybersecurity-alert-classifier/
├── cybersecurity_bert_93percent.py   # Training & inference script
├── requirements.txt                   # Python dependencies
├── model/                             # Saved fine-tuned model
├── data/                              # Training dataset
└── README.md                          # Documentation

🛠️ Tech Stack
Component	Technology
Base Model	BERT-base-uncased
Fine-tuning	Hugging Face Transformers
Deployment	Hugging Face Spaces
Interface	Streamlit
Language	Python 3.11+

📈 Use Cases
Use Case	Application
SOC Automation	Auto-classify incoming alerts
Threat Prioritization	Route critical threats to analysts
Alert Triage	Reduce false positive noise
Incident Response	Speed up threat identification

🔄 Future Improvements
Add more threat categories (Phishing, Malware, etc.)

Train on larger dataset (10k+ alerts)

Implement active learning for continuous improvement

Create real-time API with FastAPI

Add explainability (SHAP/LIME)


📄 License
MIT License

Built with 🛡️, 🧠, and 🤗 by Aikaksh Singh Routela

