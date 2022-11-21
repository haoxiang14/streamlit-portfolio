import streamlit as st
import streamlit.components.v1 as com
#font-family: “Cabin”, sans-serif;

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
        # #st.markdown("[![Foo](https://img.icons8.com/ios-glyphs/512/github.png)](https://github.com/haoxiang14)")
        # # st.image("https://img.icons8.com/ios-glyphs/512/linkedin-circled.png", width=50)
        # # st.image("https://img.icons8.com/ios-glyphs/512/github.png", width=50)
        # # st.image("https://img.icons8.com/color/512/hashnode.png", width=50)
        # # st.image("https://img.icons8.com/color-glass/512/interior-mirror.png", width=50)
        # # st.image("https://img.icons8.com/ios-glyphs/512/instagram-new.png", width=50)
        # # st.image("https://img.icons8.com/ios-glyphs/512/instagram-new.png", width=50)
        # # st.image("https://img.icons8.com/ios-glyphs/512/facebook-new.png", width=50)
        # # st.empty()
        
        # st.write("[LinkedIn](https://www.linkedin.com/in/tan-hao-xiang-845a4422a/)")
        # st.write("[GitHub](https://github.com/haoxiang14)")
        # st.write("[Hashnode](https://hashnode.com/@haoxiang14)")
        # st.write("[Twitter](https://twitter.com/SiLantroll14)")
        # st.write("[Mirror.xyz](https://mirror.xyz/silantroll.eth)")
        # st.write("[Instagram Personal](https://www.instagram.com/haoxiang.14/)")
        # st.write("[Instagram Education](https://www.instagram.com/cilantro.crypts/)")
        # st.write("[Facebook](https://www.facebook.com/hao.xiang.7796420/)")
        
    com.html("""
    
    <style>
    
    .links {
        text-decoration: none;
        text-align: left;
        margin-top: 20px;
        width: 300px;
        display: block;
        

    }
    
    .links:hover {
        color: grey;
    }
    

    .social {
        font-size: 30px;
        font-family: Cabin, Arial, sans-serif;
        
        
    }
    
    
    </style>

    <head>
        <script src="https://kit.fontawesome.com/289d4317a0.js" crossorigin="anonymous"></script>
    </head>

    <body>
        <div class = "social">
            <a href="https://twitter.com/SiLantroll14" target="_blank" class = "links">
                <i class="fa-brands fa-twitter-square"></i> Twitter
            </a> <br>
    
            <a href="https://www.instagram.com/haoxiang.14/" target="_blank" class = "links">
                <i class="fa-brands fa-instagram"></i> Instagram-Personal
            </a> <br>
    
            <a href="https://www.instagram.com/cilantro.crypts/" target="_blank" class = "links">
                <i class="fa-brands fa-instagram"></i> Instagram-Web3 
            </a> <br>
    
    
            <a href="https://www.facebook.com/hao.xiang.7796420/" target="_blank" class = "links">
                <i class="fa-brands fa-facebook"></i></i> Facebook
            </a> <br>
    
            <a href="https://www.linkedin.com/in/tan-hao-xiang-845a4422a/" target="_blank" class = "links">
                <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a> <br>
    
            <a href="https://github.com/haoxiang14" target="_blank" class = "links">
                <i class="fa-brands fa-github-square"></i> GitHub
            </a> <br>
    
            <a href="https://hashnode.com/@haoxiang14" target="_blank" class = "links">
                <i class="fa-brands fa-hashnode"></i> Hashnode        
            </a> <br>
    
            <a href="https://mirror.xyz/silantroll.eth" target="_blank" class = "links">
                <i class="fa-solid fa-book"></i> Mirror.xyz      
            </a> <br>
    
        </div>
    </body>
    """, height=800)
        

with st.container():
    st.write("---")
    st.header("My Resume")
    st.write("Download now for more information :point_down:")
    st.download_button("Download", "https://cdn.discordapp.com/attachments/966648657996828708/1041641148386639943/bpyc.jpeg", key="resume")
        
    

#streamlit run 🏠Homepage.py
