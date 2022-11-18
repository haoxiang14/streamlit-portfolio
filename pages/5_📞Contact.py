import streamlit as st
st.set_page_config(page_title="My Website", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

with st.container():
    st.title("My Contact")

with st.container():
    st.header("Contact")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Phone: +6011-2776 8326")
        st.write("Email: haoxiangt.14@gmail.com")
        st.write("School Email: Tp060906@mail.apu.edu.my")
        st.write("WhatsApp: [+601127768326](https://wa.me/601127768326)")
    
    with right_column:
        st.empty()

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
    