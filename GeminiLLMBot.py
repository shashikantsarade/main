import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCkImAMySg8CswcGujDsDLys3M5LT8Ljcc")

# Set up model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    # ... other safety settings
]
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Initialize chat history
convo = model.start_chat(history=[
    {"role": "user", "parts": ["date?"]},
    {"role": "model", "parts": ["March 8, 2023"]},
])

# Create Streamlit app layout
st.title("Search your doubts...")

# User input field with improved clarity and placeholder text
user_input = st.text_input("Ask a question or provide a prompt:", placeholder="Type your message here")

# Create Streamlit app layout
st.title("तुमची संदेहं शोधा...")

# User input field with improved clarity and placeholder text
user_input = st.text_input("एक प्रश्न विचारा किंवा प्रोंप्ट प्रदान करा:", placeholder="येथे तुमचा संदेश टाइप करा")

if user_input:
    # convo.send_message(user_input)
    # response = convo.last.text
    response = "आपला उत्तर येथे आहे"
    st.write(f"Gemini Pro: {response}")

# Add custom CSS styling
st.markdown("""
<style>
/* Custom CSS for input */
div.stTextInput>div>div>div>input {
    background-color: #f0f0f0 !important;
    color: #333 !important;
    border-radius: 5px;
    border: 1px solid #ccc !important;
    padding: 0.5rem;
}

/* Custom CSS for output */
div.stMarkdown {
    animation: fadeIn 1s;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
---
**Note:**

* Enter question and type enter to search
* Built on Gemini model
* @ShashiSar""")
