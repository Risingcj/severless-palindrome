import streamlit as st
import requests

st.markdown("""
# 🔁 Palindrome Checker

This simple app checks if the word you enter is a **palindrome** — a word, number or phrase that reads the same backward as forward.
""")

# Replace this with your actual API Gateway URL
API_URL = "https://vkp2yqey5ahph55y5zxf24pkou0aiutn.lambda-url.eu-north-1.on.aws/"


word = st.text_input("Enter a word to check:")

if st.button("Check"):
    if not word:
        st.warning("Please enter a word.")
    else:
        try:
            response = requests.get(API_URL, params={"word": word})
            if response.status_code == 200:
                result = response.json()
                if result.get("is_palindrome"):
                    st.success(f'"{result["word"]}" **is** a palindrome!')
                else:
                    st.error(f'"{result["word"]}" is **not** a palindrome.')
            else:
                st.error("Error from Lambda function.")
        except Exception as e:
            st.error(f"Failed to reach the server: {e}")
