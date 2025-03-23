import streamlit as st

def apply_styles():
    """Apply custom CSS styles to the Streamlit app"""
    st.markdown("""
    <style>
    body {
        color: #f0f2f6;
        background-color: #0e1117;
    }
    .centered {
        display: flex;
        justify-content: center;
        margin: 0 auto;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        color: white;
    }
    .sub-title {
        font-size: 25px;
        font-weight: 500;
        margin-top: 30px;
        margin-bottom: 15px;
        color: #66b3ff;
    }
    .card {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #4da6ff;
        color: #f0f2f6;
    }
    .sentiment-positive {
        background-color: rgba(0, 128, 0, 0.2);
        border-left: 5px solid #00cc00;
        color: #ffffff;
    }
    .sentiment-negative {
        background-color: rgba(255, 105, 180, 0.2);
        border-left: 5px solid #ff69b4;
        color: #ffffff;
    }
    .sentiment-neutral {
        background-color: rgba(70, 130, 180, 0.2);
        border-left: 5px solid #4682b4;
        color: #ffffff;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .search-container {
        max-width: 300px;
        margin: 0 auto;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)