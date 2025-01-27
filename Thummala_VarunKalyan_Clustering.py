# T-3 Clustering

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from sklearn.preprocessing import StandardScaler

# Load the datasets
customers = pd.read_csv('C:/Users/varun/Desktop/eCommerce_project/Customers.csv')
transactions = pd.read_csv('C:/Users/varun/Desktop/eCommerce_project/Transactions.csv')

# Features for clustering
# Aggregate transaction data by CustomerID
transaction_data = transactions.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum'
}).reset_index()

# Merge with customer profile data
customer_data = transaction_data.merge(customers, on='CustomerID')

# Select relevant features for clustering
features = customer_data[['TotalValue', 'Quantity', 'Region']]

# One-hot encode the categorical variable 'Region'
features = pd.get_dummies(features, columns=['Region'])

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow method
inertia = []
db_index_scores = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)
    db_index = davies_bouldin_score(scaled_features, kmeans.labels_)
    db_index_scores.append(db_index)

# Plot the Elbow method
plt.figure(figsize=(12, 6))
plt.plot(range(2, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(range(2, 11))
plt.grid()
plt.show()

# Plot the Davies-Bouldin Index
plt.figure(figsize=(12, 6))
plt.plot(range(2, 11), db_index_scores, marker='o')
plt.title('Davies-Bouldin Index for Different k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Davies-Bouldin Index')
plt.xticks(range(2, 11))
plt.grid()
plt.show()

# Choose the optimal number of clusters (let's say k=4 based on the elbow method)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_features)

# Calculate DB Index for the chosen number of clusters
db_index = davies_bouldin_score(scaled_features, customer_data['Cluster'])
print(f'Davies-Bouldin Index for {optimal_k} clusters: {db_index}')

# Visualize the clusters
plt.figure(figsize=(12, 8))
sns.scatterplot(x=customer_data['TotalValue'], y=customer_data['Quantity'], hue=customer_data['Cluster'], palette='viridis', s=100)
plt.title('Customer Segmentation Clusters')
plt.xlabel('Total Value (USD)')
plt.ylabel('Quantity Purchased')
plt.legend(title='Cluster')
plt.grid()
plt.show()

# Save the clustered data to a CSV file
customer_data.to_csv('Customer_Segmentation.csv', index=False)
print("Customer segmentation results saved to Customer_Segmentation.csv")