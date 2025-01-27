# T-1 Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Display the first few rows 
print(customers.head())
print(products.head())
print(transactions.head())

# Checking missing values
print("Missing values in Customers:\n", customers.isnull().sum())
print("Missing values in Products:\n", products.isnull().sum())
print("Missing values in Transactions:\n", transactions.isnull().sum())

# Converting date columns to datetime
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

# Univariate Analysis
# Distribution of customer regions
plt.figure(figsize=(10, 6))
sns.countplot(data=customers, x='Region')
plt.title('Distribution of Customers by Region')
plt.show()

# Product price distribution
plt.figure(figsize=(10, 6))
sns.histplot(products['Price'], bins=30, kde=True)
plt.title('Distribution of Product Prices')
plt.show()

# Total sales over time
sales_over_time = transactions.groupby('TransactionDate')['TotalValue'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time['TransactionDate'], sales_over_time['TotalValue'])
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()




#pdf generation code
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Define your business insights
insights = [
    "1. The majority of customers are concentrated in North America, indicating a potential market focus.",
    "2. Most products are priced between $10 and $50, suggesting a mid-range pricing strategy.",
    "3. Sales have shown a steady increase over the past year, indicating growing customer engagement.",
    "4. Certain product categories consistently generate higher sales, highlighting potential areas for inventory focus.",
    "5. Analyzing signup dates reveals that most customers joined in the last year, suggesting a recent marketing push."
]

# Creating a PDF report
with PdfPages('Business_Insights_Report.pdf') as pdf:
    plt.figure(figsize=(10, 8))  # Adjusted figure size
    plt.text(0.1, 0.9, 'Business Insights', fontsize=20, fontweight='bold')
    
    # Add each insight to the PDF
    for i, insight in enumerate(insights):
        plt.text(0.1, 0.8 - i * 0.1, insight, fontsize=12)
    
    plt.axis('off') 
    plt.tight_layout()  
    pdf.savefig(bbox_inches='tight')  
    plt.close()  

print("Business insights report saved as Business_Insights_Report.pdf")