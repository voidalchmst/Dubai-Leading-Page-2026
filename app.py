import streamlit as st

# Page Configuration
st.set_page_config(page_title="Emirates Capital Leads 2026", layout="centered")

# Custom Styling for better look
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #004a99;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("🛡️ Emirates Capital Leads")
st.subheader("Connect with UAE's Top Regulated Trading Partners")
st.write("Stop searching and start investing. We bridge the gap between serious investors and world-class trading consultancies in Dubai.")

st.divider()

# Lead Capture Form
with st.form(key='lead_form'):
    st.write("### Get a Free Consultation Call")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    contact = st.text_input("WhatsApp Number (with country code)")
    
    investment_range = st.selectbox("Preferred Investment Volume", 
                                    ["Select Range", "AED 5k - 20k", "AED 20k - 50k", "AED 50k - 100k", "AED 100k+"])
    
    st.info("💡 Our partner firms will reach out to you within 24 hours.")
    
    submit = st.form_submit_button(label="CONNECT ME WITH AN EXPERT")

# Handling Form Submission
if submit:
    if name != "" and whatsapp != "" and investment_range != "Select Range":
        st.success(f"Excellent {name}! Your profile has been sent to our premium trading partners. Expect a call shortly.")
    else:
        st.error("Please provide your name, WhatsApp, and investment range to proceed.")

st.divider()

# Contact Section
st.subheader("📩 Business Inquiries")
st.write("Are you a trading firm looking for quality leads? Reach us at:")
st.markdown("📧 **asifanwar8152@gmail.com**")

st.divider()

# Legal Disclaimer - Small Font Size
st.markdown("""
<style>
.disclaimer {
    font-size: 10px;
    color: #666666;
    text-align: justify;
    line-height: 1.2;
}
</style>
<div class="disclaimer">
<b>Disclaimer:</b> Emirates Capital Leads operates strictly as a lead generation intermediary. We are NOT a financial advisory firm, broker, or fund manager. We do not provide direct investment advice or execute trades. Our role is to connect potential investors with third-party trading companies. We are not responsible for any investment decisions or losses incurred through our partner firms. All data is processed in accordance with UAE Federal Decree-Law No. 45 of 2021.
</div>
""", unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Emirates Capital Leads. Connecting Investors to Opportunities.")
