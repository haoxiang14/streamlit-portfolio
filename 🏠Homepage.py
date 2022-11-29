import streamlit as st
import streamlit.components.v1 as com
import json
from streamlit_lottie import st_lottie

#font-family: “Cabin”, sans-serif;



def open_lottiefile(file):
    with open(file) as f:
        return json.load(f)
    
image_eth = open_lottiefile("eth.json")
image_programmer = open_lottiefile("programmer.json")



st.set_page_config(page_title="My Website", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.container():
    st.image("https://cdn.discordapp.com/attachments/966648657996828708/1041641148386639943/bpyc.jpeg", width=200)

    

with st.container():
    st.subheader("Hi, I'm Hao Xiang :wave:")
    st.write("""
             I'm a student in Asia Pacific University, Kuala Lumpur, Malaysia, majoring in Computer Science and currently in my 2nd year of study. 
             I'm interested in Data Science, Web and Software Development.  
             """)

with st.container():
    st.write("---")
    st.header("About Me")
    #st.subheader("Student in Asia Pacific University")
    col1, col2, col3= st.columns([2,1,3], gap= "small")
    with st.container():
        with col1:
            st.write("""
        I love programming, creating content, and doing research. 
        While I am free, I will do some research and create content for my Instagram account because it will help me and others at the same time. 
        My favorite programming languages are Python and HTML because Python is very easy to learn, and I like Web Development. 
        I am looking forward to learning more about JavaScript because it is important to build Web 3 products. 
        I am able to speak English, Malay, and Chinese well although Chinese is my mother tongue.\n
            """)
        
        with col2:
            st_lottie(image_programmer, height=200, key="coding")
            
        with col3:
            st.empty()

    with st.container():
        with col1:
            st.write("\n\n")
            st.write("""
        I am also a non stop learner that would like to improve and broaden my skill set through  doing some new and difficult tasks. 
        I enjoy working in teams but at the same time I am capable of handling tasks on my own. 
        Highly enthusiasts in Blockchain, Web 3, NFTs, cryptocurrency and etc which can be the technology of the future.
            """)

        with col2:
            st_lottie(image_eth, height=200, key="code")
        
        with col3:
            st.empty()



with st.container():
    st.write("---")
    st.header("My Experience")
    
    tab1, tab2 = st.tabs(["Work Experience", "Education"])
    with tab1:
        st.subheader("RND Lead and Community Manager(APU BCC) ")
        col1, col2 = st.columns([2,1], gap= "small")
        with col1:
            st.write("""
             APU Blockchain and Cryptocurrency Club (APUBCC) is the first and ever Blockchain and Cryptocurrency Club among Malaysia universities. 
             APU BCC aims to be the leading blockchain club in Malaysia to spread blockchain knowledge among students.
             """)
            st.image("https://cdn.discordapp.com/attachments/966648657996828708/1047045731166453802/Club_Logo_Dark_Background_2.png", width=300)
        
        with col2:
            st.empty()
        

        with col1:
            st.write("\n\n")
            st.subheader("Scholar(KopiDAO)")
            st.write("""
            KopiDAO is a decentralized autonomous organization that aims to create a learning and building community where anyone can contribute to growing the Web3 ecosystem through their diverse skill sets.
            """)
            st.image("https://cdn.discordapp.com/attachments/956021034367213568/1031559610190008340/kopidao-logo-v2.png", width=200)
        with col2:
            st.empty()
    
    with tab2:
        st.empty()
    
    
    
    
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
    with open("resume.pdf", "rb") as f:
        st.download_button(label="Download", data= f, file_name="resume.pdf", mime="application/pdf")
        
    

#streamlit run 🏠Homepage.py
