# -*- coding: utf-8 -*-
""".1402

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-MyRdtV24jTgS9BfGaWSD_PPnzPW5R3E
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('/content/psychological_state_dataset.csv')

data.sample(20)

data.info()

numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

print("Numerical Columns:", numerical_columns)
print("Categorical Columns:", categorical_columns)

for col in categorical_columns:
  print(f"Value counts for {col}:\n{data[col].value_counts()}\n")

for col in numerical_columns:
  sns.histplot(data[col], kde=True, bins=30)
  plt.title(f'Distribution of {col}')
  plt.show()

for col in numerical_columns:
  sns.boxplot(x=data[col])
  plt.title(f'Boxplot of {col}')
  plt.show()

for col in categorical_columns:
  sns.countplot(x=data[col], order=data[col].value_counts().index)
  plt.title(f'Distribution of {col}')
  plt.xticks(rotation=45)
  plt.show()

corr_matrix = data[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show

sns.pairplot(data[numerical_columns])
plt.show()

for cat_col in categorical_columns:
  if data[cat_col].nunique() < 5:
    g = sns.FacetGrid(data, col=cat_col, sharey=False)
    g.map(sns.histplot, "Skin Temp (°C)")
    plt.show()

if 'Time' in categorical_columns:
  data['Time'] = pd.to_datetime(data['Time'])

  for col in numerical_columns:
    sns.lineplot(x=data['Time'], y=data[col])
    plt.title(f'{col} Over Time')
    plt.show()

for col in ['Mood State', 'Psychological State']:
  if col in categorical_columns:
    sns.countplot(x=col, data=data, order=data[col].value_counts().index)
    plt.title(f'{col} Distribution')
    plt.show()

from math import pi

radar_data = data[numerical_columns].mean()
categories = radar_data.index
values = radar_data.values.tolist()
values += values[:1]

angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories)

ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, alpha=0.4)
plt.title('Radar Chart of Numerical Data')
plt.show()

if 'Cognitive Load' in numerical_columns:
  sns.scatterplot(x=data['Age'], y=data['Focus Duration (s)'], size=data['Cognitive Load'], sizes=(20, 200))

for cat_col in categorical_columns:
  grouped_stats = data.groupby(cat_col)[numerical_columns].mean()
  print(f"Grouped statistics for {cat_col}:\n", grouped_stats)

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numerical_columns])

kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_data)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=pca_data[:, 0], y=pca_data[:, 1], hue=data['Cluster'], palette='viridis', s=100)
plt.title('K-Means Clusters Visualized in 2D')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

from scipy.cluster.hierarchy import linkage, dendrogram

linked = linkage(scaled_data, method='ward')

plt.figure(figsize=(12, 6))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=False)
plt.title('Hierarchiacal Clustering Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=300)
tsne_results = tsne.fit_transform(scaled_data)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=tsne_results[:, 0], y=tsne_results[:,1], hue=data['Cluster'], palette='coolwarm', s=100)
plt.title('T-SNE Clustering Visualization')
plt.xlabel('TSNE Component 1')
plt.ylabel('TSNE Component 2')
plt.show()

for cat_col in categorical_columns:
  grouped_data = data.groupby(cat_col)[numerical_columns].mean()
  plt.figure(figsize=(12, 6))
  sns.heatmap(grouped_data, annot=True, fmt=".2f", cmap='coolwarm')
  plt.title(f'Mean Values of Numerical Features by {cat_col}')
  plt.ylabel(cat_col)
  plt.xlabel('Numerical Features')
  plt.show()

from pandas.plotting import parallel_coordinates

parallel_data = data[numerical_columns].copy()
parallel_data['Cluster'] = data['Cluster']

plt.figure(figsize=(12, 6))
parallel_coordinates(parallel_data, class_column='Cluster', colormap='viridis')
plt.title('Parallel Coordinates Plot by Clusters')
plt.xticks(rotation=45)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score

data_encoded = data.copy()
for col in categorical_columns:
  le = LabelEncoder()
  data_encoded[col] = le.fit_transform(data[col])

X = data_encoded.drop(['Cognitive Load'], axis=1)
y = data_encoded['Cognitive Load']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')

accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy_score: {accuracy * 100:.2f}%")

feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': clf.feature_importances_})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importances)
plt.title('Feature Importance')
plt.show()