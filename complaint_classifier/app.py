from flask import Flask, request, jsonify, render_template
import pickle
import re

app = Flask(__name__)

with open('refined_model.pkl', 'rb') as f:
    model = pickle.load(f)

def analyze_metadata(text):
    # Advanced Urgency Logic
    urgency_score = 20 # Base score
    high_priority_terms = ['immediately', 'refund', 'legal', 'sue', 'worst', 'terrible', 'waiting', 'days']
    
    words = text.lower().split()
    for word in words:
        if word in high_priority_terms: urgency_score += 15
    
    # Extract Keywords (Words longer than 5 chars that aren't common)
    keywords = [w for w in words if len(w) > 5 and w not in ['please', 'customer', 'complaint']]
    
    return min(urgency_score, 100), keywords[:3]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    
    # 1. Prediction & True Confidence
    category = model.predict([text])[0]
    probabilities = model.predict_proba([text])
    confidence = probabilities.max() * 100

    # 2. Metadata Analysis
    urgency, keywords = analyze_metadata(text)

    # 3. Dynamic AI Response
    replies = {
        "Billing Issue": "I've flagged this for our Finance Team. They will audit the transaction and update your balance.",
        "Refund/Return": "Refund request received. Our system is calculating the eligible amount based on our 30-day policy.",
        "Technical Problem": "This looks like a system bug. I've sent the diagnostic logs to our Engineering department.",
        "Delivery Problem": "Logistics tracking initiated. We are contacting the local courier hub for an immediate update.",
        "Account Issue": "Security protocol triggered. Please check your registered email for a verification link.",
        "Service Issue": "I'm sorry for the frustration. I've escalated this to a Senior Manager for review."
    }
    
    ai_reply = replies.get(category, "Thank you. We are processing your request.")

    return jsonify({
        'category': category,
        'confidence': round(confidence, 1),
        'urgency': urgency,
        'keywords': keywords,
        'ai_reply': ai_reply
    })

if __name__ == '__main__':
    app.run(debug=True)