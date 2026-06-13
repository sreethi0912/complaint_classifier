# 🤖 Customer Complaint Classification System 

A Machine Learning-powered web application that analyzes customer complaints and automatically predicts the complaint category, confidence score, urgency level, and relevant keywords. The system also generates automated responses to assist customer support teams.

---

## 🚀 Features

- Complaint Classification using NLP  
- Confidence Score Prediction  
- Urgency Detection  
- Keyword Extraction  
- Automated Response Generation  
- Interactive Flask Web Interface  
- Real-Time Complaint Analysis  

---

## 🛠️ Technologies Used

### Backend
- Python  
- Flask  

### Machine Learning
- Scikit-learn  
- LinearSVC  
- CalibratedClassifierCV  
- TF-IDF Vectorization  

### Data Processing
- Pandas  
- NumPy  

### Frontend
- HTML  
- CSS  
- JavaScript  

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
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jessysatwika03/Complaint_Classifier.git
cd Complaint_Classifier
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔍 Sample Input

```
I received a damaged product and would like a replacement as soon as possible.
```

---

## 📊 Sample Output

```
Predicted Category: Product Defect  
Confidence: 97.7%  
Urgency Score: High  
Keywords: received, product, damaged  
AI Response: Thank you. We are processing your request.
```

---

## 🔄 Machine Learning Workflow

1. Input Complaint Text  
2. Text Preprocessing  
3. TF-IDF Vectorization  
4. Model Prediction (LinearSVC)  
5. Confidence Score Calculation  
6. Urgency Detection  
7. Keyword Extraction  
8. Automated Response Generation  

---

## 📈 Future Enhancements

- Sentiment Analysis  
- Complaint Analytics Dashboard  
- User Authentication  
- Multi-language Support  
- Cloud Deployment  

---

## 👩‍💻 Authors

- Jessy Satwika  
- Sreethi  

---

## 📜 License

This project is for educational and learning purposes.
