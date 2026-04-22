import streamlit as st

# Page Configuration
st.set_page_config(page_title="Dubai Investment Guide 2026", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main { text-align: center; }
    .stButton>button { width: 100%; background-color: #FFD700; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("🚀 Smart Investing in UAE Stocks")
st.subheader("Join our exclusive network of successful investors.")
st.write("Get a FREE expert analysis of the top 5 stocks to watch this month.")

st.divider()

# Lead Capture Form
with st.form("lead_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    contact = st.text_input("Email Address")
    whatsapp = st.text_input("WhatsApp Number (with country code)")
    investment_range = st.selectbox("Monthly Investment Capacity", ["Under AED 5k", "AED 5k - 20k", "AED 20k - 50k", "AED 50k+"])
    
    submit = st.form_submit_button("SEND ME THE FREE GUIDE")

# Handling Form Submission
if submit:
    if name and whatsapp:
        # ഇവിടെ നിങ്ങൾക്ക് ഈ ഡാറ്റ ഒരു Google Sheet-ലേക്കോ Database-ലേക്കോ സേവ് ചെയ്യാം
        st.success(f"Thanks {name}! We will send the guide to {whatsapp} shortly.")
        # Data storage logic goes here
    else:
        st.error("Please fill in your name and WhatsApp number.")

st.divider()
st.caption("© 2026 EmiratesCapital. Your data is safe with us.")