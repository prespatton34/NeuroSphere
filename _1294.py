# -*- coding: utf-8 -*-
""".1294

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18GMbHEjdUUsZiko73-qVxV-WVgsf5hgs
"""



import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import warnings

import warnings # Importing the warnings module
warnings.filterwarnings('ignore') # Calling the filterwarnings function

df = pd.read_csv("/content/shopping_trends (2).csv")

df.head()

df.sample(10)

df.info()

fig_age = px.histogram(
    df,
    x='Age',
    nbins= 50,
    title='Age Distribution of Customers',
    color_discrete_sequence=['cyan']
)

fig_age.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)
fig_age.show()

gender_counts = df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig_gender = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Gender Proportions of Customers',
    color_discrete_sequence=px.colors.sequential.RdBu
)
fig_gender.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)
fig_gender.show()

location_counts = df['Location'].value_counts().reset_index()
location_counts.columns = ['Location', 'Count']

fig_location = px.bar(
    location_counts,
    x='Location',
    y='Count',
    text='Count',
    title='Customer Count by Location',
    color_discrete_sequence=['lime']
)
location_counts = df['Location'].value_counts().reset_index()
location_counts.columns = ['Location', 'Count']

fig_location = px.bar(
    location_counts,
    x='Location',
    y='Count',
    text='Count',
    title='Customer Count by Location',
    color_discrete_sequence=['lime']
)
fig_location.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title="Location",
    yaxis_title="Number of Customers"
)
fig_location.show()
fig_location = px.bar(
    location_counts,
    x='Location',
    y='Count',
    text='Count',
    title='Customer Count by Location',
    color_discrete_sequence=['lime']
)
fig_location.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title="Location",
    yaxis_title="Number of Customers"
)
fig_location.show()

item_counts = df['Item Purchased'].value_counts().reset_index()
item_counts.columns = ['Item Purchased', 'Count']

fig_items = px.bar(
    item_counts,
    x='Item Purchased',
    y='Count',
    text='Count',
    title='Most Purchased Items',
    color_discrete_sequence=['orange']
)
fig_items.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Items',
    yaxis_title='Count of Purchases'
)
fig_items.show()

fig_amount = px.box(
    df,
    y='Purchase Amount (USD)', # Changed from 'Purchased Amount (USD)'
    title='Purchase Amount Distribution',
    color_discrete_sequence=['magenta']
)

fig_amount.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    yaxis_title='Purchase Amount (USD)'
)
fig_amount.show()

# Count popular sizes
size_counts = df['Size'].value_counts().reset_index()
size_counts.columns = ['Size', 'Count']

fig_sizes = px.bar(
    size_counts,
    x='Size',
    y='Count',
    text='Count',
    title='Preferred Sizes',
    color_discrete_sequence=['green']
)
fig_sizes.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Size',
    yaxis_title='Count of Purchases'
)
fig_sizes.show()

# Count popular colors
color_counts = df['Color'].value_counts().reset_index()
color_counts.columns = ['Color', 'Count']

fig_colors = px.bar(
    color_counts,
    x='Color',
    y='Count',
    text='Count',
    title='Preferred Colors',
    color_discrete_sequence=['teal']
)
fig_colors.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Color',
    yaxis_title='Count of Purchases'
)
fig_colors.show()

# Seasonal Trends
season_counts = df['Season'].value_counts().reset_index()
season_counts.columns = ['Season', 'Count']

fig_season = px.bar(
    season_counts,
    x='Season',
    y='Count',
    text='Count',
    title='Seasonal Trends in Purchases',
    color_discrete_sequence=['blue']
)
fig_season.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Season',
    yaxis_title='Count of Purchases'
)
fig_season.show()

# Frequency of Purchases
frequency_counts = df['Frequency of Purchases'].value_counts().reset_index()
frequency_counts.columns = ['Frequency', 'Count']

fig_frequency = px.bar(
    frequency_counts,
    x='Frequency',
    y='Count',
    text='Count',
    title='Frequency of Purchases',
    color_discrete_sequence=['red']
)
fig_frequency.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Frequency',
    yaxis_title='Count of Purchases'
)
fig_frequency.show()

payment_counts = df['Payment Method'].value_counts().reset_index()
payment_counts.columns = ['Payment Method', 'Count']

fig_payment = px.pie(
    payment_counts,
    names='Payment Method',
    values='Count',
    title='Popular Payment Methods',
    color_discrete_sequence=px.colors.sequential.Plasma
)
fig_payment.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)
fig_payment.show()

subscription_data = df.groupby('Subscription Status')['Purchase Amount (USD)'].sum().reset_index()

fig_subscription = px.bar(
    subscription_data,
    x='Subscription Status',
    y='Purchase Amount (USD)',
    text='Purchase Amount (USD)',
    title='Impact of Subscription on Purchases',
    color='Subscription Status',
    color_discrete_sequence=px.colors.sequential.Viridis
)
fig_subscription.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Subscription Status',
    yaxis_title='Total Purchase Amount (USD)'
)
fig_subscription.show()

discount_data = df['Discount Applied'].value_counts().reset_index()
discount_data.columns = ['Discount Applied', 'Count']

fig_discount = px.bar(
    discount_data,
    x='Discount Applied',
    y='Count',
    text='Count',
    title='Discount Usage Analysis',
    color='Discount Applied',
    color_discrete_sequence=px.colors.sequential.Cividis
)
fig_discount.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Discount Applied',
    yaxis_title='Number of Purchases'
)
fig_discount.show()

category_revenue = df.groupby('Category')['Purchase Amount (USD)'].sum().reset_index()

fig_category_revenue = px.treemap(
    category_revenue,
    path=['Category'],
    values='Purchase Amount (USD)',
    title='Category-Wise Revenue',
    color='Purchase Amount (USD)',
    color_continuous_scale=px.colors.sequential.Sunset
)
fig_category_revenue.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)
fig_category_revenue.show()

fig_ratings = px.histogram(
    df,
    x='Review Rating',
    nbins=10,
    title='Distribution of Review Ratings',
    color_discrete_sequence=['#FFA07A']
)
fig_ratings.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Review Rating',
    yaxis_title='Count'
)
fig_ratings.show()

shipping_data = df.groupby('Shipping Type')['Purchase Amount (USD)'].sum().reset_index()

fig_shipping = px.bar(
    shipping_data,
    x='Shipping Type',
    y='Purchase Amount (USD)',
    text='Purchase Amount (USD)',
    title='Shipping Types and Revenue Impact',
    color='Shipping Type',
    color_discrete_sequence=px.colors.sequential.Teal
)
fig_shipping.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Shipping Type',
    yaxis_title='Total Revenue (USD)'
)
fig_shipping.show()

customer_revenue = df.groupby('Customer ID')['Purchase Amount (USD)'].sum().reset_index()
customer_revenue = customer_revenue.sort_values(by='Purchase Amount (USD)', ascending=False)
customer_revenue['Cumulative Percentage'] = customer_revenue['Purchase Amount (USD)'].cumsum() / customer_revenue['Purchase Amount (USD)'].sum() * 100

fig_pareto = px.bar(
    customer_revenue,
    x='Customer ID',
    y='Purchase Amount (USD)',
    text='Purchase Amount (USD)',
    title='High-Spending Customers - Pareto Chart',
    color_discrete_sequence=['#FF7F50']
)
fig_pareto.add_scatter(
    x=customer_revenue['Customer ID'],
    y=customer_revenue['Cumulative Percentage'],
    mode='lines+markers',
    name='Cumulative Percentage',
    line=dict(color='cyan')
)
fig_pareto.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Customer ID',
    yaxis_title='Purchase Amount (USD)',
    yaxis2=dict(title='Cumulative Percentage', overlaying='y', side='right')
)
fig_pareto.show()

clustering_data = df.groupby('Customer ID').agg({
    'Purchase Amount (USD)': 'sum',
    'Frequency of Purchases': 'count',
    'Category': 'nunique'
}).reset_index()
clustering_data.columns = ['Customer ID', 'Total Purchase Amount', 'Purchase Frequency', 'Unique Categories']

# Standardize the data
scaler = StandardScaler()
clustering_data_scaled = scaler.fit_transform(clustering_data[['Total Purchase Amount', 'Purchase Frequency', 'Unique Categories']])

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clustering_data['Cluster'] = kmeans.fit_predict(clustering_data_scaled)

# Scatter plot
fig_clusters = px.scatter_3d(
    clustering_data,
    x='Total Purchase Amount',
    y='Purchase Frequency',
    z='Unique Categories',
    color='Cluster',
    title='Behavioral Clusters of Customers',
    symbol='Cluster',
    color_continuous_scale=px.colors.sequential.Viridis
)
fig_clusters.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    scene=dict(
        xaxis_title='Total Purchase Amount',
        yaxis_title='Purchase Frequency',
        zaxis_title='Unique Categories'
    )
)
fig_clusters.show()

fig_purchase_vs_rating = px.scatter(
    df,
    x='Purchase Amount (USD)',
    y='Review Rating',
    title='Purchase Amount vs. Review Rating',
    color='Review Rating',
    color_continuous_scale='Viridis'
)

# Add regression line
X = sm.add_constant(df['Purchase Amount (USD)'])  # Add constant for intercept
y = df['Review Rating']
model = sm.OLS(y, X).fit()
df['Regression Line'] = model.predict(X)

fig_purchase_vs_rating.add_scatter(
    x=df['Purchase Amount (USD)'],
    y=df['Regression Line'],
    mode='lines',
    name='Regression Line',
    line=dict(color='cyan')
)

fig_purchase_vs_rating.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Purchase Amount (USD)',
    yaxis_title='Review Rating'
)

fig_purchase_vs_rating.show()

fig_age_vs_spending = px.scatter(
    df,
    x='Age',
    y='Purchase Amount (USD)',
    title='Age vs. Spending Habits',
    color='Age',
    color_continuous_scale='Viridis'
)

fig_age_vs_spending.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Age',
    yaxis_title='Purchase Amount (USD)'
)

fig_age_vs_spending.show()

fig_category_vs_gender.update_layout(
    template='plotly_dark',  # Corrected the template name to 'plotly_dark'
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Product Category',
    yaxis_title='Count'
)
fig_category_vs_gender.show()

fig_discounts_vs_spending = px.box(
    df,
    x='Discount Applied',
    y='Purchase Amount (USD)',
    title='Effect of Discounts on Spending',
    color='Discount Applied',
    color_discrete_sequence=['#FF6347', '#20B2AA']
)

fig_discounts_vs_spending.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis_title='Discount Applied',
    yaxis_title='Purchase Amount (USD)'
)

fig_discounts_vs_spending.show()

fig_profitability_analysis = px.treemap(
    df,
    path=['Category', 'Size', 'Color'],  # Hierarchy: Category -> Size -> Color
    values='Purchase Amount (USD)',
    title='Profitability Analysis by Category, Size, and Color',
    color='Purchase Amount (USD)',  # Color by total purchase amount
    color_continuous_scale='Viridis'
)

fig_profitability_analysis.update_layout(
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)

fig_profitability_analysis.show()
