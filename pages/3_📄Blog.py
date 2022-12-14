import streamlit as st
st.set_page_config(page_title="Hao Xiang's Portfolio", page_icon="https://cdn.discordapp.com/attachments/966648657996828708/1041641148386639943/bpyc.jpeg", layout="wide", initial_sidebar_state="expanded")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.container():
    st.title("My Blog")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://haoxiang.hashnode.dev/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1649925305921%2Fk34klX-j8.png%3Fw%3D1600%26h%3D840%26fit%3Dcrop%26crop%3Dentropy%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=1920&q=75", width=300)
        
    with right_column:
        st.subheader("NFTs: Non Fungible Tokens")
        st.write("This article is mainly about the basics of Non-Fungible Tokens (NFTs) and also the situation of the NFT market in Malaysia, is it profitable 🤔?")
        st.write("[Learn More](https://haoxiang.hashnode.dev/nfts-non-fungible-tokens)")
        
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://haoxiang.hashnode.dev/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1668622545374%2FSwDiHTOsl.jpeg%3Fw%3D1600%26h%3D840%26fit%3Dcrop%26crop%3Dentropy%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=1920&q=75", width=300)
        
    with right_column:
        st.subheader("How to use Discord to manage a DAO")
        st.write("This article is mainly about the basics of Non-Fungible Tokens (NFTs) and also the situation of the NFT market in Malaysia, is it profitable 🤔?")
        st.write("[Learn More](https://haoxiang.hashnode.dev/how-to-use-discord-to-manage-a-dao)")