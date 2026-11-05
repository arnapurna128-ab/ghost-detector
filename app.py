# 1. Import streamlit for dashboard
import streamlit as st
# 2. Import pandas
import pandas as pd
# 3. Import our detector
from fraude_detector import detect_ghosts

# 4. Page title
st.title("Ghost Beneficiary Detector - Odisha")
# 5. Subtitle
st.write("Detects fake / duplicate beneficiaries in govt schemes")

# 6. Upload button
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

# 7. If user uploads file
if uploaded_file is not None:
    # 8. Read CSV
    df = pd.read_csv(uploaded_file)
    # 9. Show total count
    st.write(f"Total Beneficiaries: {len(df)}")
    # 10. Run detection
    fraud_df = detect_ghosts(df)
    # 11. Show fraud count
    st.error(f"Ghost Found: {len(fraud_df)}")
    # 12. Show fraud table
    st.dataframe(fraud_df)
    # 13. Download button
    st.download_button("Download Fraud Report", fraud_df.to_csv(index=False), "fraud_report.csv")
# 14. If no file, show sample
else:
    st.info("Upload odisha_beneficiaries.csv to test")