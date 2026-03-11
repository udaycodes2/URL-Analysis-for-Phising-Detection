import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# rebuild model architecture
model = Sequential([
    Dense(128, activation='relu', input_shape=(19,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])


model.load_weights("models/phishing_nn_model.h5")

# load scaler
scaler = joblib.load("models/scaler.pkl")



st.markdown("<h1 style='text-align:center;'> Phishing Website Detector</h1>", unsafe_allow_html=True)

st.write("")
st.write("Paste a URL below to check if it is **Phishing or Legitimate**.")

url = st.text_input("Enter URL")



def extract_features(url):

    features = [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('_'),
        url.count('/'),
        url.count('?'),
        url.count('='),
        url.count('@'),
        url.count('&'),
        url.count('!'),
        url.count(' '),
        url.count('~'),
        url.count(','),
        url.count('+'),
        url.count('*'),
        url.count('#'),
        url.count('$'),
        url.count('%'),
        url.count('//')
    ]

    return np.array(features).reshape(1,-1)



if st.button("Detect Website"):

    if url == "":
        st.warning("Please enter a URL")
    else:

        features = extract_features(url)
        features = scaler.transform(features)

        prediction = model.predict(features)[0][0]

        probability = prediction * 100

        st.subheader(f"Prediction Confidence: {probability:.2f}%")

        st.progress(int(probability))

        if prediction > 0.5:
            st.error(" This website is likely **PHISHING**")
        else:
            st.success("This website appears **LEGITIMATE**")
