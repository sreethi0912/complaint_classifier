import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.pipeline import Pipeline

def train_advanced_model():
    # Load your dataset
    df = pd.read_csv('customer_complaints_dataset_extended.csv')
    df = df.dropna(subset=['Complaint_Text', 'Category'])
    
    # Advanced Pipeline: TF-IDF with sublinear scaling (better for text)
    # CalibratedClassifierCV ensures "Confidence %" is realistic
    base_model = LinearSVC(C=1.0, class_weight='balanced', max_iter=2000)
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            stop_words='english', 
            ngram_range=(1, 2), 
            sublinear_tf=True
        )),
        ('clf', CalibratedClassifierCV(base_model, cv=3))
    ])

    print("🚀 Training Advanced Calibrated Model...")
    pipeline.fit(df['Complaint_Text'], df['Category'])

    with open('refined_model.pkl', 'wb') as f:
        pickle.dump(pipeline, f)
    print("✅ Advanced Model Saved.")

if __name__ == "__main__":
    train_advanced_model()