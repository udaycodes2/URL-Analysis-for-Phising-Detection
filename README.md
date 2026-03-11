🔐 Phishing URL Detection using Machine Learning
📌 Overview

Phishing attacks are a major cybersecurity threat where attackers create fraudulent websites that mimic legitimate ones in order to steal sensitive information such as passwords, banking details, and personal data.

This project builds a machine learning based phishing detection system that analyzes a website URL and predicts whether it is phishing or legitimate.

The model is trained using URL structural features and deployed through an interactive Streamlit web application that allows users to test URLs in real time.

🎯 Project Objectives

The main goals of this project are:

Detect phishing websites using URL-based features

Train multiple machine learning models and compare performance

Select the best performing model

Deploy the model as an interactive web application

Provide real-time phishing detection from user input

📊 Dataset

The dataset used contains 100,077 URLs with 19 feature variables describing the structure of each URL.

Each record represents a website URL labeled as:

0 → Legitimate website

1 → Phishing website

Dataset Features

The model uses 19 URL characteristics, including:

Feature	Description
url_length	Total number of characters in the URL
n_dots	Number of dots in the URL
n_hyphen	Count of hyphens (-)
n_underline	Count of underscores (_)
n_slash	Count of slashes (/)
n_questionmark	Number of question marks
n_equal	Number of equal signs
n_at	Number of @ symbols
n_and	Number of & characters
n_exclamation	Number of !
n_space	Spaces in URL
n_tilde	~ characters
n_comma	, characters
n_plus	+ characters
n_asterisk	* characters
n_hashtag	# characters
n_dollar	$ characters
n_percent	% characters
n_redirection	Number of URL redirections

These structural characteristics often appear in malicious URLs attempting to disguise themselves as legitimate sites.

🔍 Exploratory Data Analysis

Several visualizations were performed to understand patterns in phishing URLs.

Key observations:

Phishing URLs tend to be longer than legitimate URLs.

They contain more dots and special characters.

They often include multiple query parameters to hide malicious code.

Rare characters such as *, #, and $ appeared mostly in phishing URLs.

Example visualizations included:

Boxplots comparing URL length between classes

Feature distribution analysis

Correlation heatmap

Feature importance analysis

These insights helped identify which features contribute most to phishing detection.

⚙️ Machine Learning Models Used

Several models were tested:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

XGBoost

Neural Network (Final Model)

The neural network performed best in capturing complex feature interactions.

🧠 Neural Network Architecture

The final deep learning model used the following architecture:

Input Layer: 19 features
Hidden Layer 1: 128 neurons (ReLU)
Hidden Layer 2: 64 neurons (ReLU)
Output Layer: 1 neuron (Sigmoid)


Loss Function:

Binary Crossentropy


Optimizer:

Adam

📈 Model Performance

The neural network achieved:

Accuracy: 89%
AUC Score: ~0.96


Performance highlights:

High true positive rate for phishing detection

Reduced false negatives compared to other models

Strong ROC curve performance

This indicates the model can effectively differentiate between legitimate and phishing URLs.

🖥️ Streamlit Web Application

A Streamlit web interface was built to allow real-time phishing detection.

Users simply paste a URL, and the application:

Extracts the 19 URL features

Scales them using the trained scaler

Runs them through the neural network

Displays the prediction and confidence score

Example Output
Prediction Confidence: 82%

⚠️ Phishing Website Detected


or

Prediction Confidence: 93%

✅ Legitimate Website

📂 Project Structure
phishing-url-detector
│
├── app
│   └── streamlit_app.py
│
├── models
│   ├── phishing_nn_model.h5
│   └── scaler.pkl
│
├── data
│   └── web-page-phishing.csv
│
├── advanced-url-analysis-for-phishing-detection.ipynb
│
├── requirements.txt
└── README.md

🚀 Running the Project
Install dependencies
pip install -r requirements.txt

Run the Streamlit app
streamlit run app/streamlit_app.py


Open the browser:

http://localhost:8501

💡 Key Learnings

This project demonstrates several important machine learning concepts:

Data preprocessing and feature engineering

Exploratory data analysis

Model comparison and evaluation

Deep learning with neural networks

Model deployment using Streamlit

🔮 Future Improvements

Possible improvements include:

Adding domain reputation checks

Using DNS and SSL certificate features

Integrating WHOIS domain age information

Using content-based phishing detection

Deploying the application online

🧑‍💻 Author

Developed by Uday

Machine Learning | Data Science | Cybersecurity Applications
