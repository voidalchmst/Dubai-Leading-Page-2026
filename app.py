import streamlit as st
import requests  # ഇതിനായി requirements.txt-ൽ requests ചേർക്കണം
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Emirates Capital Leads 2026", layout="centered", page_icon="🛡️")

# --- SHEETDB CONFIGURATION ---
# നിങ്ങളുടെ SheetDB API URL ഇവിടെ പേസ്റ്റ് ചെയ്യുക
SHEETDB_API_URL = "https://sheetdb.io/api/v1/rut2m0uvjnpoh" 

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #004a99;
        color: white;
        height: 3em;
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }
    .success-badge {
        background-color: #e8f4fd;
        color: #004a99;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        border: 1px solid #004a99;
        margin-bottom: 20px;
    }
    .biz-button {
        background-color: #ffffff;
        color: #004a99;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        border: 2px solid #004a99;
        text-decoration: none;
        display: block;
        font-weight: bold;
    }
    .disclaimer {
        font-size: 11px;
        color: #666666;
        text-align: justify;
        line-height: 1.4;
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("🛡️ Emirates Capital Leads 2026")
st.subheader("Stop Guessing. Start Investing.")

st.markdown('<div class="success-badge">✅ Trusted by 500+ Successful & Satisfied Investors in the UAE</div>', unsafe_allow_html=True)

st.write("""
We bridge the gap between serious investors and world-class trading consultancies in Dubai. 
Our mission is to connect you with the right experts based on your goals.
""")

st.divider()

# 4. Lead Capture Form for Clients
with st.form(key='lead_form'):
    st.write("### Get a Free Consultation Call")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    whatsapp_val = st.text_input("WhatsApp Number (with country code)")
    
    investment_range = st.selectbox("Preferred Investment Volume", 
                                    ["Select Range", "AED 5k - 20k", "AED 20k - 50k", "AED 50k - 100k", "AED 100k+"])
    
    st.info("💡 Join our community of 500+ successful clients.")
    submit = st.form_submit_button(label="CONNECT ME WITH AN EXPERT")

# --- HANDLING DATA SUBMISSION ---
if submit:
    if name != "" and whatsapp_val != "" and investment_range != "Select Range":
        # ഗൂഗിൾ ഷീറ്റിലേക്ക് അയക്കാനുള്ള ഡാറ്റ തയ്യാറാക്കുന്നു
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lead_data = {
            "data": [
                {
                    "Name": name,
                    "Email": email,
                    "WhatsApp": whatsapp_val,
                    "Investment_Range": investment_range,
                    "Date": current_time
                }
            ]
        }
        
        try:
            # SheetDB വഴി ഗൂഗിൾ ഷീറ്റിലേക്ക് ഡാറ്റ അയക്കുന്നു
            response = requests.post(SHEETDB_API_URL, json=lead_data)
            
            if response.status_code == 201:
                st.success(f"Excellent {name}! Your profile has been shared. Expect a call shortly.")
                # SheetDB ഡാഷ്‌ബോർഡിൽ 'Notifications' ഓൺ ചെയ്താൽ നിങ്ങൾക്ക് ഇമെയിൽ വരും
            else:
                st.error("Error saving data. Please contact support.")
        except Exception as e:
            st.error("Connection error. Please try again later.")
    else:
        st.error("Please provide all required details (Name, WhatsApp, and Investment Range).")

st.divider()

# 5. Business Inquiry Section
st.subheader("💼 Business Partnerships")
st.write("Are you a licensed trading firm or regulated broker looking for high-quality leads?")

business_form_url = "https://forms.gle/your_business_form_link" 
st.markdown(f'<a href="{business_form_url}" target="_blank" class="biz-button">APPLY AS A TRADING PARTNER</a>', unsafe_allow_html=True)

st.divider()

# 6. Legal Disclaimer Section
st.markdown("""
<div class="disclaimer">
<b>LEGAL DISCLAIMER:</b> Emirates Capital Leads is a lead generation intermediary. We are NOT a financial advisory firm. 
All data is collected with user consent and processed in compliance with <b>UAE Federal Decree-Law No. 45 of 2021</b>.
</div>
""", unsafe_allow_html=True)

st.divider()

# 7. Footer & Contact
st.caption("© 2026 Emirates Capital Leads. Connecting Investors to Opportunities.")

contact_email = "asifanwar8152@gmail.com"
st.markdown(f'<a href="mailto:{contact_email}" style="text-decoration:none;"><button style="background-color:#004a99; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer; width:100%;">Email Our Partnerships Team</button></a>', unsafe_allow_html=True)
