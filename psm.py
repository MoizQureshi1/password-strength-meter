import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown(""" 
<style>
    .main{ text-align: center; }
    .stTextInput{ width: 60%; !important; }
    .stButton Button { width: 50%; background-color: green; color: #fff; color: white; font-size: 18px; }
    .stButton Button:hover { background-color: #45a049; color: white; }
</style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🔐 Password Strength Generator")
st.write("Enter Your Password to Check its Security Level. 🔎")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password Should Include **both uppercase and lowercase letters**.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password Should Include **at least one number (0-9)**.")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")
    
    # Strength Rating
    if score == 4:
        st.success("✅ **Strong Password!** - Your Password is Strong and Secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider Improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Foolow the suggestions below to improve strength it.")


    # Feedback 
    if feedback:
        with st.expander("🔎**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Inter Your Password:", type="password", help="Ensure your password is strong and secure 🔐.")


# Button Working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password First 🔑.") # Warning Message if password entered
