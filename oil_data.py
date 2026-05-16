import pandas as pd

print("--- RUNNING ENTERPRISE LAS WELL-LOG PARSER ---")

# Simulating raw, unformatted ASCII text lines straight from an oilfield LAS file
raw_las_file = [
    "~VERSION INFORMATION",
    "VERS.  2.0 : CWLS LOG ASCII STANDARD -VERSION 2.0",
    "~WELL INFORMATION",
    "WELL.   WELL-A1 : WELL NAME",
    "~CURVE INFORMATION",
    "DEPT.FT     : 1 DEPTH",
    "GR.API      : 2 GAMMA RAY",
    "~A LOG DATA",
    " 1000.00    45.20",
    " 1005.00    48.70",
    " 1010.00    120.30",
    " 1015.00    115.10"
]

print("\n[READ] Processing raw line-by-line ASCII string streams...")

data_lines = []
is_data_section = False

# Step 2: Architect logic to extract the matrix values automatically
for line in raw_las_file:
    if line.startswith("~A"):  # Detecting the data block start marker
        is_data_section = True
        continue
    if is_data_section:
        # Split the text line by spaces and convert strings to floating decimals
        values = [float(x) for x in line.split()]
        data_lines.append(values)

# Step 3: Map data to a clean structural matrix table
df = pd.DataFrame(data_lines, columns=['Depth (ft)', 'Gamma Ray (API)'])

print("\n[SUCCESS] Structural Conversion Complete:")
print(df.to_string(index=False))

# Export clean database assets to your computer directory
df.to_excel("Parsed_Well_Log_Data.xlsx", index=False)
print("\n[EXPORT] Generated structured master spreadsheet: Parsed_Well_Log_Data.xlsx")