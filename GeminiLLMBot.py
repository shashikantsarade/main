import streamlit as st
import google.generativeai as genai
import ChatGoogleGenerativeAI from genai
# Define custom CSS styles
custom_css = """
<style>
body {
    font-family: Arial, sans-serif;
}
.container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
}
.user-message {
    background-color: #f0f0f0;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
}
.bot-message {
    background-color: #e2f3ff;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Rest of your Streamlit app
from google.generativeai import ChatGoogleGenerativeAI

# Set up authentication (replace with your API key)
api_key = "AIzaSyCkImAMySg8CswcGujDsDLys3M5LT8Ljcc"
llm = ChatGoogleGenerativeAI(model_name="gemini-pro")

def main():
    st.title("Gemini Pro Bot")
    chat_history = st.session_state.get("chat_history", [])
    user_input = st.text_input("Ask me anything...")

    if user_input:
        chat_history.append({"user": user_input})
        response = llm.invoke(inputs=user_input)
        chat_history.append({"bot": response.content})

    st.session_state["chat_history"] = chat_history

    for message in chat_history:
        if "user" in message:
            st.markdown(f'<div class="user-message">{message["user"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message["bot"]}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
