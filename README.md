Data Science Assignment: eCommerce Transactions Dataset
Overview
This repository contains the solution to the Data Science Assignment, which involves performing Exploratory Data Analysis (EDA), building a Lookalike Model, and conducting Customer Segmentation on an eCommerce transactions dataset. The dataset consists of three CSV files: Customers.csv, Products.csv, and Transactions.csv. The aim is to analyze the data, derive insights, build predictive models, and generate business strategies.

Dataset Description
The dataset comprises three files:

Customers.csv

CustomerID: Unique identifier for each customer.
CustomerName: Name of the customer.
Region: Continent where the customer resides.
SignupDate: Date when the customer signed up.
Products.csv

ProductID: Unique identifier for each product.
ProductName: Name of the product.
Category: Product category.
Price: Product price in USD.
Transactions.csv

TransactionID: Unique identifier for each transaction.
CustomerID: ID of the customer who made the transaction.
ProductID: ID of the product sold.
TransactionDate: Date of the transaction.
Quantity: Quantity of the product purchased.
TotalValue: Total value of the transaction.
Price: Price of the product sold.
Assignment Tasks
The project is divided into three main tasks:

Task 1: Exploratory Data Analysis (EDA) and Business Insights
Perform EDA on the provided dataset.
Derive at least 5 business insights based on the EDA.
Deliverables:

A Jupyter Notebook/Python script with EDA code.
A PDF report containing business insights (maximum 500 words).
Task 2: Lookalike Model
Build a Lookalike Model to recommend 3 similar customers based on their profile and transaction history.
Use both customer and product information for similarity scoring.
Deliverables:

Top 3 lookalike customers (with similarity scores) for the first 20 customers (CustomerID: C0001 - C0020) in a Lookalike.csv file.
A Jupyter Notebook/Python script explaining the model development.
Task 3: Customer Segmentation / Clustering
Perform customer segmentation using clustering techniques.
Use profile information (from Customers.csv) and transaction data (from Transactions.csv).
Evaluate the clusters using the DB Index.
Deliverables:

A report on clustering results, including:
Number of clusters formed.
DB Index value and other metrics.
Visual representation of clusters using relevant plots.
A Jupyter Notebook/Python script containing clustering code.
Setup Instructions
Follow these steps to run the code and explore the dataset:

Clone the repository:
bash
Copy
Edit
git clone https://github.com/<your-username>/Data_Science_Assessment.git
cd Data_Science_Assessment
Install the required Python libraries:
bash
Copy
Edit
pip install -r requirements.txt
Run the Jupyter Notebooks for each task:
Task 1: EDA.ipynb
Task 2: Lookalike_Model.ipynb
Task 3: Customer_Clustering.ipynb
Project Deliverables
Exploratory Data Analysis (EDA):

Insights derived from the dataset in EDA_Report.pdf.
Lookalike Model:

Recommendations for the first 20 customers in Lookalike.csv.
Customer Segmentation:

Cluster analysis results in Clustering_Report.pdf and visual plots.
