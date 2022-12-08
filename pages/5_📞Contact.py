import streamlit as st
import streamlit.components.v1 as com


st.set_page_config(page_title="Hao Xiang's Portfolio", page_icon="https://cdn.discordapp.com/attachments/966648657996828708/1041641148386639943/bpyc.jpeg", layout="wide", initial_sidebar_state="expanded")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.container():
    st.title("My Contact")
    st.write("---")

with st.container():
    # st.header("Contact")
    left_column, right_column = st.columns(2)
    with left_column:
        # st.write("Phone: +6011-2776 8326")
        # st.write("Email: haoxiangt.14@gmail.com")
        # st.write("School Email: Tp060906@mail.apu.edu.my")
        # st.write("WhatsApp: [+601127768326](https://wa.me/601127768326)")
        com.html("""
        
        <style>
            .contacts{
                font-size: 20px;
                font-family: Cabin, Arial, sans-serif;
                color: #E8C4C4;
            }
            .contacts:hover {
                color: grey;
            }
    
        </style>       
        
        
        <head>
            <script src="https://kit.fontawesome.com/289d4317a0.js" crossorigin="anonymous"></script>
        </head>


        <body>
            <div class="contact">
                <p class="contacts"> <i class="fa-solid fa-phone"></i> Phone: +601127768326 </p>

                <p class="contacts"> <i class="fa-solid fa-envelope"></i> Email: <a href= "mailto: haoxiangt.14@gmail.com"> haoxiangt.14@gmail.com </a></p>

                <p class = "contacts"> <i class="fa-solid fa-inbox"></i> School Mail: <a href= "mailto: Tp060906@mail.apu.edu.my"> Tp060906@mail.apu.edu.my </a></p>

                <p class = "contacts"> <i class="fa-brands fa-discord"></i> Discord: haoxiang #1513</p>

                <p class = "contacts"> <i class="fa-brands fa-whatsapp"></i> WhatsApp: <a href="https://wa.me/601127768326" target="_blank"> +601127768326 </a> </p>

                <p class = "contacts"> <i class="fa-brands fa-telegram"></i> Telegram: <a href= "https://t.me/haoxiang_14" target="_blank"> @haoxiang_14 </a></p>

            </div>

        </body>

        """, height=300,width=800)
            
            
            
            
            
            
            
            
            
        


file_name = "style.css"
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css(file_name)

with st.container():
   st.write("---")
   st.header("Get in Touch with Me!")
   st.write("##")
   contact_form = """
    <form action="https://formsubmit.co/tp060906@mail.apu.edu.my" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder = "Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
   """
   left_column, right_column = st.columns(2)
   with left_column:
       st.markdown(contact_form, unsafe_allow_html=True)
   with right_column:
       st.empty()
    