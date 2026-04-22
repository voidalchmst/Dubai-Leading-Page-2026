import streamlit as st


# 1. Page Configuration

st.set_page_config(page_title="Emirates Capital Leads 2026", layout="centered", page_icon="🛡️")


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

    .stButton>button:hover {

        background-color: #003366;

        color: #FFD700;

    }

    .success-badge {

        background-color: #e8f4fd;

        color: #004a99;

        padding: 12px;

        border-radius: 10px;

        text-align: center;

        font-weight: bold;

        border: 1px solid #004a99;

        margin-top: 10px;

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

        margin-top: 10px;

    }

    .biz-button:hover {

        background-color: #004a99;

        color: white;

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

    

    st.info("💡 Join our community of 500+ successful clients who have found their ideal trading partners through us.")

    

    submit = st.form_submit_button(label="CONNECT ME WITH AN EXPERT")


# Handling Form Submission

if submit:

    if name != "" and whatsapp_val != "" and investment_range != "Select Range":

        st.success(f"Excellent {name}! Your profile has been shared with our premium partners. Expect a call shortly.")

    else:

        st.error("Please provide all required details (Name, WhatsApp, and Investment Range).")


st.divider()


# 5. Business Inquiry Section

st.subheader("💼 Business Partnerships")

st.write("Are you a licensed trading firm or regulated broker looking for high-quality leads in the UAE?")


business_form_url = "https://forms.gle/your_business_form_link" 

st.markdown(f'<a href="{business_form_url}" target="_blank" class="biz-button">APPLY AS A TRADING PARTNER</a>', unsafe_allow_html=True)


st.divider()


# 6. Legal Disclaimer Section

st.markdown("""

<div class="disclaimer">

<b>LEGAL DISCLAIMER:</b> Emirates Capital Leads operates strictly as a lead generation and marketing intermediary. 

We are NOT a financial advisory firm, licensed broker, or fund manager. We do not provide direct investment advice.

All data is collected with explicit user consent and processed in compliance with <b>UAE Federal Decree-Law No. 45 of 2021</b>.

</div>

""", unsafe_allow_html=True)


st.divider()


# 7. Footer & Contact

st.caption("© 2026 Emirates Capital Leads. Connecting Investors to Opportunities.")


contact_email = "asifanwar8152@gmail.com"

st.markdown(f'<a href="mailto:{contact_email}" style="text-decoration:none;"><button style="background-color:#004a99; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer; width:100%;">Email Our Partnerships Team</button></a>', unsafe_allow_html=True)
