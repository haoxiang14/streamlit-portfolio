import streamlit as st
st.set_page_config(page_title="My Website", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.container():
    st.title("My Project")
    st.write("---")
    
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048141869357482046/Github_Repo_.jpg", width=300)
        
    with right_column:
        st.subheader("Discord Welcome Bot")
        st.write("This project is a Discord bot that welcomes new members😎. It is written in Python and uses the Discord.py library.")
        st.write("[Learn More](https://github.com/haoxiang14/APUBCC-Welcome-Bot)")
        
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048141868917071872/Github_Repo_1.jpg", width=300)
        
    with right_column:
        st.subheader("Streamlit Portfolio")
        st.write("This project is a portfolio website 🕸️ that is written in Python and uses the Streamlit library.")
        st.write("[Learn More](https://github.com/haoxiang14/streamlit-portfolio)")
    