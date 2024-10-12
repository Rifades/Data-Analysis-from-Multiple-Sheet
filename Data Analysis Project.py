
# Basic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('Jupiter Data 1.xlsx')
df1 = pd.read_excel('Info Table.xlsx')
df2 = pd.read_excel('Dispute.xlsx')

# Data Correction

df = df.dropna(subset=['db_code'])
df['db_code'] = df['db_code'].astype(int)

# Vlookup in Python

mapping_variable = df1.set_index('DB-Code')[['DB House Name', 'Business Unit', 'DB House Status','ROM/TM Name']]
mapping_variable1 = df2.set_index('loan_id')['Remarks']
df['DB House Name'] = df['db_code'].map(mapping_variable['DB House Name'])
df['Business Unit'] = df['db_code'].map(mapping_variable['Business Unit'])
df['ROM/TM Name'] = df['db_code'].map(mapping_variable['ROM/TM Name'])
df['DB House Status'] = df['db_code'].map(mapping_variable['DB House Status'])
df['Remarks'] = df['loan_id'].map(mapping_variable1)

# Filtering Out Data

df = df.drop(df[df['Remarks'] == 'Full Dispute'].index)
df = df.drop(df[df['DB House Status'] == 'Closed'].index)
df = df.drop(df[df['tag'] == 'OVERDUE'].index)

# Group By Function

test = df.groupby('Business Unit')['disbursed_amount'].sum()
business_unit = df['Business Unit'].unique()
business_unit = np.sort(business_unit)

# Bar Chart

for index, value in enumerate(test):
    plt.text(index, value, f"{value/10000000:.2f}", ha='center', va='bottom')
plt.bar(business_unit,test, color='red', linestyle = 'solid')
plt.xlabel('Business Unit')
plt.ylabel('Disbursed Amount')
plt.title('Disbursed Amount by Business Unit')
plt.grid(True)
plt.tight_layout()
plt.show()

# Pie Chart

plt.figure(figsize=(10,6))
plt.pie(test, labels = business_unit, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Disbursed Amount by Business Unit')
plt.grid(True)
plt.tight_layout()
plt.show()