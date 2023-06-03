# IMPORTS
import streamlit as st
from chat import *


st.set_page_config(
    page_title="PASS Lawyer Index",
    page_icon="https://abs.twimg.com/emoji/v1/72x72/1f916.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


task_selection = st.sidebar.selectbox(
    "Select task",
    [   "Intro",
        "Chat",         
    ],
)

if task_selection == "Intro": 
    st.markdown("""
    # 𐄷 PASS - Lawyer Index
    ## A chatbot for lawyers for querying the past cases with general question answering capability.

    ### How to use?
    - Select the task from the sidebar.
    - Enter the question in the text box.
    - Click on the send button.
    - The chatbot will respond to your question.
    - You can also ask follow up questions.
    - You can also ask general questions.
    - You can also ask for the past cases.
    
    """)
elif task_selection == "Chat":
    chat_interface()

