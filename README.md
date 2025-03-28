# Data Analysis from Multiple xlsx using Python

## Table of Contents

- [Proect Overview](#project-overview)
- [Expected Outcome](#ecpected-outcome)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Limitations](#limitations)

### Project Overview

This project aims to streamline the analysis and visualization of current credit due across multiple Excel (.xlsx) files. Leveraging the power of Python's data manipulation and visualization libraries, we will develop a robust solution to consolidate data from disparate sources into a unified, insightful representation.

### Expected Outcome

- A fully automated Python script capable of consolidating credit due data from multiple .xlsx files.
- Interactive or static visualizations that effectively communicate the overall credit due status.
- Comprehensive reports that provide actionable insights and support informed decision-making.

### Data Sources

- Dispute Data [Dispute.xlsx](Data-Analysis-from-Multiple-Sheet/Dispute.xlsx)
- DB House Details [Info Table.xlsx](Data-Analysis-from-Multiple-Sheet/Info-Table.xlsx)
- Loan Database [Jupiter Data 1.xlsx](Data-Analysis-from-Multiple-Sheet/Jupiter-Data-1.xlsx)

### Tools

- Numpy and Pandas - Data Cleaning
- Pandas - Data Analysis
- Matplotlib - Data Visualization

### Steps Followed

#### Data Aggregation
Implemented efficient Python scripts to automatically extract and combine relevant credit due information from multiple .xlsx files, irrespective of file structure variations.

```python
df = pd.read_excel('Jupiter Data 1.xlsx')
df1 = pd.read_excel('Info Table.xlsx')
df2 = pd.read_excel('Dispute.xlsx')
```

#### Data Transformation
Clean, transform, and standardize the aggregated data to ensure consistency and accuracy for subsequent analysis.

```python
df = df.dropna(subset=['db_code'])
df['db_code'] = df['db_code'].astype(int)
mapping_variable = df1.set_index('DB-Code')[['DB House Name', 'Business Unit', 'DB House Status', 'ROM/TM Name']]
mapping_variable1 = df2.set_index('loan_id')['Remarks']
df['DB House Name'] = df['db_code'].map(mapping_variable['DB House Name'])
df['Business Unit'] = df['db_code'].map(mapping_variable['Business Unit'])
df['ROM/TM Name'] = df['db_code'].map(mapping_variable['ROM/TM Name'])
df['DB House Status'] = df['db_code'].map(mapping_variable['DB House Status'])
df['Remarks'] = df['loan_id'].map(mapping_variable1)
```

#### Visualization Development
Construct clear and concise visualizations (e.g., bar charts, line graphs, dashboards) to effectively communicate the overall credit due status, highlighting key trends and potential areas of concern.

```python
df = df.drop(df[df['Remarks'] == 'Full Dispute'].index)
df = df.drop(df[df['DB House Status'] == 'Closed'].index)
df = df.drop(df[df['tag'] == 'OVERDUE'].index)
```


#### Automation and Scalability
Design the solution to be easily automated and scalable, allowing for seamless integration with existing workflows and future expansion.

```python
test = df.groupby('Business Unit')['disbursed_amount'].sum()
business_unit = df['Business Unit'].unique()
business_unit = np.sort(business_unit)
```

#### Reporting and Insights
Generate comprehensive reports that provide actionable insights into the current credit due situation, enabling informed decision-making.

```python
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
```

### Limitations
- xlsx file name should be exactly same to run this script.
- Each of the three .xlsx files must contain a consistent set of base columns.
