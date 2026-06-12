# 🤖 AI Complaint Classifier

A Machine Learning-powered web application that analyzes customer complaints and automatically predicts the complaint category, confidence score, urgency level, and relevant keywords. The system also generates automated responses to assist customer support teams.

## 🚀 Features

* Complaint Classification using NLP
* Confidence Score Prediction
* Urgency Detection
* Keyword Extraction
* Automated Response Generation
* Interactive Flask Web Interface
* Real-Time Complaint Analysis

## 🛠️ Technologies Used

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* LinearSVC
* CalibratedClassifierCV
* TF-IDF Vectorization

### Data Processing

* Pandas
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
Complaint_Classifier/
│
├── app.py
├── train_model.py
├── customer_complaints_dataset_extended.csv
├── model.pkl
├── refined_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── complaint_classifier/
│   └── templates/
│       └── index.html
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jessysatwika03/Complaint_Classifier.git
cd Complaint_Classifier
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

---

## 🔍 Sample Input

```text
I received a damaged product and would like a replacement as soon as possible.
```

### Sample Output

```text
Predicted Category: Product Defect
Confidence : 97.7%
Urgency score: 20
Keywords: received, product, damaged
AI Response: Thank you. We are processing your request.
```

---

## 🔄 Machine Learning Workflow

1. Complaint Text Input
2. Text Preprocessing
3. TF-IDF Vectorization
4. Complaint Classification
5. Confidence & Urgency Analysis
6. Keyword Extraction
7. Automated Response Generation

---

## 📈 Future Enhancements

* Sentiment Analysis
* Complaint Analytics Dashboard
* User Authentication
* Multi-language Support
* Cloud Deployment

---

## 👩‍💻 Authors

* Sreethi
* Jessy Satwika

---

## 📜 License

This project was developed for educational and learning purposes.
