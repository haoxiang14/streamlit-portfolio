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
    

# with st.container():
#     st.write("---")
#     embed = """
    
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(embed, unsafe_allow_html=True)
#     with right_column:
#         st.empty()
    