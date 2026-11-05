# 1. Import pandas for data handling
import pandas as pd

# 2. Function to load data
def load_data(file):
    return pd.read_csv(file)

# 3. Function to detect ghosts
def detect_ghosts(df):
    # 4. Copy data to avoid changing original
    df = df.copy()
    # 5. Create empty list for reasons
    df['fraud_reason'] = ""
    # 6. Create fraud flag column
    df['is_fraud'] = 0

    # 7. Rule 1: Same Aadhaar used many times
    aadhaar_counts = df['aadhaar'].value_counts()
    # 8. Find duplicate aadhaar numbers
    duplicate_aadhaar = aadhaar_counts[aadhaar_counts > 1].index.tolist()
    # 9. Mark them as fraud
    for idx, row in df.iterrows():
        # 10. Check duplicate aadhaar
        if row['aadhaar'] in duplicate_aadhaar:
            df.at[idx, 'is_fraud'] = 1
            df.at[idx, 'fraud_reason'] += "Duplicate Aadhaar, "
        # 11. Rule 2: Age is impossible
        if row['age'] > 110 or row['age'] < 0:
            df.at[idx, 'is_fraud'] = 1
            df.at[idx, 'fraud_reason'] += "Invalid Age, "
        # 12. Rule 3: Same phone, different names
        if row['phone'] == "9999999999":
            df.at[idx, 'is_fraud'] = 1
            df.at[idx, 'fraud_reason'] += "Fake Phone, "
    
    # 13. Return only fraud rows
    return df[df['is_fraud'] == 1]