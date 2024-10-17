import pandas as pd

# Tailoring the given input to our functionality
# Read the CSV file, skipping the first row
df = pd.read_csv('Hackathon_Oct_2024 - Sheet2.csv', skiprows=1)

# Display the dataframe (optional)
print(df)
