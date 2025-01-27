# T-2 Lookalike Model

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
customers = pd.read_csv('C:/Users/varun/Desktop/eCommerce_project/Customers.csv')
transactions = pd.read_csv('C:/Users/varun/Desktop/eCommerce_project/Transactions.csv')

# Merge customer and transaction data
customer_transactions = transactions.merge(customers, on='CustomerID')

# Create a feature set for customers
features = customer_transactions.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum',
    'Region': 'first'
}).reset_index()

# One-hot encode the region
features = pd.get_dummies(features, columns=['Region'])

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features.drop('CustomerID', axis=1))

# Calculate cosine similarity
similarity_matrix = cosine_similarity(scaled_features)

# Create a DataFrame for similarity scores
similarity_df = pd.DataFrame(similarity_matrix, index=features['CustomerID'], columns=features['CustomerID'])

# Get top 3 lookalikes for the first 20 customers
lookalike_results = {}
for customer in features['CustomerID'][:20]:
    similar_customers = similarity_df[customer].nlargest(4).iloc[1:]  # Exclude self
    lookalike_results[customer] = {
        'LookalikeID_1': similar_customers.index[0],
        'SimilarityScore_1': similar_customers.values[0],
        'LookalikeID_2': similar_customers.index[1],
        'SimilarityScore_2': similar_customers.values[1],
        'LookalikeID_3': similar_customers.index[2],
        'SimilarityScore_3': similar_customers.values[2],
    }

# Convert to DataFrame
lookalike_df = pd.DataFrame.from_dict(lookalike_results, orient='index')

# Save to CSV
lookalike_df.to_csv('Lookalike.csv', index=True)

print("Lookalike model results saved to Lookalike.csv")