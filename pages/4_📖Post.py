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
  st.title("My Educational Post")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048121548998967306/Crypto_wallet.png", width=200)
        
    with right_column:
        st.subheader("Crypto Wallets")
        st.write("This instagram post is mainly about the basics of crypto wallets 💰 and the types of crypto wallets.")
        st.write("[Learn More](https://www.instagram.com/p/Ck3jOOIvTOg/?utm_source=ig_web_copy_link)")
        
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048121549540036659/cilantro.crypts.png", width=200)
        
    with right_column:
        st.subheader("ERC standards")
        st.write("This instagram post is mainly about the basics of ERC standards 📄 and the types of ERC standards.")
        st.write("[Learn More](https://www.instagram.com/p/Cj4kdsgPT-y/?utm_source=ig_web_copy_link)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048122390795780116/Luna_.png", width=200)
        
    with right_column:
        st.subheader("The Defi Edge's lessons from Terra Luna Collapse (Part 1)")
        st.write("This instagram post is mainly about the lessons that we can learn from Terra Luna Collapse (by Defi'Edge).")
        st.write("[Learn More](https://www.instagram.com/p/CeIo-61PEla/?utm_source=ig_web_copy_link)")
        
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://cdn.discordapp.com/attachments/966648657996828708/1048122390397337660/Luna_2_.png", width=200)
        
    with right_column:
        st.subheader("The Defi Edge's lessons from Terra Luna Collapse (Part 2)")
        st.write("This instagram post is mainly about the lessons that we can learn from Terra Luna Collapse (by Defi'Edge).")
        st.write("[Learn More](https://www.instagram.com/p/CeWkb2Dv7OR/?utm_source=ig_web_copy_link)")
