import streamlit as st
import pandas as pd
import google.generativeai as genai


# Set up Gemini API
genai.configure(api_key="AIzaSyDKv4gjBMYe_OszgWMz7Lcns4900oVBhP0")
model = genai.GenerativeModel('gemini-pro')

# Streamlit app
st.title("Data Analysis AI with Gemini")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display dataframe
    st.write(df)
    
    # User input for analysis
    user_question = st.text_input("What would you like to know about this data?")
    
    if user_question:
        # Generate prompt for Gemini
        prompt = f"Analyze the following data and answer the question: '{user_question}'\n\nData:\n{df.to_string()}"
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        
        # Display response
        st.write("AI Analysis:")
        st.write(response.text)

# Instructions
st.sidebar.header("Instructions")
st.sidebar.write("1. Upload a CSV file")
st.sidebar.write("2. Ask a question about the data")
st.sidebar.write("3. The AI will analyze and respond")