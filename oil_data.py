import pandas as pd
from datetime import datetime

print("--- INITIALIZING ENTERPRISE DATA ARCHITECT AUDITOR ---")

# Simulating a massive, corrupted corporate database file received from the field
faulty_data = {
    'Asset_ID': ['WELL-01', 'WELL-02', 'WELL-03', 'WELL-04', 'WELL-05'],
    'Operating_Pressure': [2500, -999, 2700, None, 2650],  # -999 and None are system errors
    'Status': ['Active', 'Active', 'Active', 'Unknown', 'Suspended']
}

df = pd.DataFrame(faulty_data)
print("\n[AUDIT] Raw System Anomalies Detected:")
print(df.to_string(index=False))

# === ARCHITECT FLOW LOGIC ===
# 1. Flag and isolate critical sensor failures
df['Pressure_Alert'] = df['Operating_Pressure'].apply(lambda x: 'CRITICAL: SENSOR ERROR' if x == -999 or pd.isna(x) else 'NORMAL')

# 2. Automatically heal data gaps using historical structural baselines
median_pressure = df[df['Operating_Pressure'] > 0]['Operating_Pressure'].median()
df['Healed_Pressure'] = df['Operating_Pressure'].apply(lambda x: median_pressure if x == -999 or pd.isna(x) else x)

print("\n[HEALED] Automated Architecture Repair Successful:")
print(df[['Asset_ID', 'Healed_Pressure', 'Pressure_Alert', 'Status']].to_string(index=False))

# Export the certified log to the corporate directory
output_report = "Certified_Asset_Audit_Report.xlsx"
df.to_excel(output_report, index=False)
print(f"\n[EXPORT] Generated compliance-ready file: {output_report}")