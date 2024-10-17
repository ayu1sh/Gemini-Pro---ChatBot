
# Import necessary libraries
import streamlit as st
import google.generativeai as gen_ai

# Load API key from Streamlit's secret management
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro",
    page_icon="🤖",
    layout="centered"
)

# Setup Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display title
st.title("🤖 Gemini Pro - ChatBot")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field
user_prompt = st.chat_input("Ask Gemini Pro...")
if user_prompt:
    # Add user's message and display it
    st.chat_message("user").markdown(user_prompt)

    # Send message to Gemini-Pro and get response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

