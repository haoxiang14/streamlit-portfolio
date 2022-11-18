import streamlit as st

st.set_page_config(page_title="My Website", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

with st.container():
    st.image("https://cdn.discordapp.com/attachments/966648657996828708/1041641148386639943/bpyc.jpeg", width=200)

    

with st.container():
    st.subheader("Hi, I'm Hao Xiang :wave:")

    
with st.container():
    st.write("---")
    st.header("About Me")
    #st.subheader("Student in Asia Pacific University")
    st.write("""        
        A non stop learner that would like to improve and broaden my skill set through  doing some new and difficult tasks. 
        I enjoy working in teams but at the same time I am capable of handling tasks on my own. 
        Highly enthusiasts in Blockchain, Web 3, NFTs, cryptocurrency and etc which can be the technology of the future.
        """)

with st.container():
    st.write("---")
    st.header("My Experience")
    
    
    
with st.container():
    st.write("---")
    st.header("Check these out :point_down:")
    left_column, right_column = st.columns(2)
    with left_column:
        #st.markdown("[![Foo](https://img.icons8.com/ios-glyphs/512/github.png)](https://github.com/haoxiang14)")
        # st.image("https://img.icons8.com/ios-glyphs/512/linkedin-circled.png", width=50)
        # st.image("https://img.icons8.com/ios-glyphs/512/github.png", width=50)
        # st.image("https://img.icons8.com/color/512/hashnode.png", width=50)
        # st.image("https://img.icons8.com/color-glass/512/interior-mirror.png", width=50)
        # st.image("https://img.icons8.com/ios-glyphs/512/instagram-new.png", width=50)
        # st.image("https://img.icons8.com/ios-glyphs/512/instagram-new.png", width=50)
        # st.image("https://img.icons8.com/ios-glyphs/512/facebook-new.png", width=50)
        # st.empty()
        
        st.write("[LinkedIn](https://www.linkedin.com/in/tan-hao-xiang-845a4422a/)")
        st.write("[GitHub](https://github.com/haoxiang14)")
        st.write("[Hashnode](https://hashnode.com/@haoxiang14)")
        st.write("[Twitter](https://twitter.com/SiLantroll14)")
        st.write("[Mirror.xyz](https://mirror.xyz/silantroll.eth)")
        st.write("[Instagram Personal](https://www.instagram.com/haoxiang.14/)")
        st.write("[Instagram Education](https://www.instagram.com/cilantro.crypts/)")
        st.write("[Facebook](https://www.facebook.com/hao.xiang.7796420/)")
    

#streamlit run 🏠Homepage.py
