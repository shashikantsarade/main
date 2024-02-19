import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="YOUR_API_KEY")

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
st.title("Chat with Gemini Pro")

# User input field with improved clarity and placeholder text
user_input = st.text_input("Ask a question or provide a prompt:", placeholder="Type your message here")

if user_input:
    convo.send_message(user_input)
    response = convo.last.text
    st.write(f"Gemini Pro: {response}")

# Enhance clarity and visual appeal with markdown formatting
st.markdown("""
---

**Note:**

* Replace `YOUR_API_KEY` with your actual Gemini API key.
* Customize the configuration and safety settings as needed.
* Explore Streamlit's widgets (e.g., buttons, sliders) for further interaction.
""")
