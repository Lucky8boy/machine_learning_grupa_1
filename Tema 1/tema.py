import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os.path
import random

if not os.path.isfile('airbnb.csv'):  # if dataset exists, it means that I only need to read it
    np.random.seed(42)
    record_to_gen = 100

    data = {'Neighborhood': [], 'Price': [], 'Occupancy': [], 'Review_Score': []}

    for _ in range(record_to_gen):
        data['Neighborhood'].append(random.choice(['A', 'B', 'C', 'D', 'E']))
        data['Price'].append(random.choice([100, 120, 80, 150, 90]))
        data['Occupancy'].append(random.choice([80, 60, 90, 50, 70]))
        data['Review_Score'].append(random.choice([4.5, 4.2, 4.8, 3.9, 4.6]))

    df = pd.DataFrame(data)
    print(df)

    df.to_csv('airbnb.csv', index=False)
else:  # dataset already exists
    df = pd.read_csv('airbnb.csv')

df = df.sort_values(by='Neighborhood')

# plots
# prices in neighborhoods
plt.figure(figsize=(13, 7))
hmap_price = df.pivot_table(values='Price', index='Neighborhood', aggfunc='mean')
sns.heatmap(hmap_price, annot=True, cmap='flare', fmt='.1f', linewidths=.8)
plt.title('Heatmap for prices in different neighborhoods')
plt.show()

# occupancy in neighborhoods
plt.figure(figsize=(13, 7))
hmap_occupancy = df.pivot_table(values='Occupancy', index='Neighborhood', aggfunc='mean')
sns.heatmap(hmap_occupancy, annot=True, cmap='crest', fmt=".1f", linewidths=.8)
plt.title('Heatmap for occupancy in different neighborhoods')
plt.show()

# review scores in neighborhoods
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Review_Score', y='Price', data=df, hue='Neighborhood', palette='mako', s=200)
plt.title('The influences of reviews in different neighborhoods')
plt.show()

# plot for prices / neighborhood
plt.figure(figsize=(13, 7))
sns.lineplot(x='Neighborhood', y='Price', data=df)
plt.title('Prices depending on the neighborhoods')
plt.xlabel('Price')
plt.ylabel('Neighborhood')
plt.show()

# neighborhood distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Neighborhood'], bins=20, kde=True, color='skyblue')
plt.title('Neighborhoods distribution')
plt.xlabel('Neighborhood')
plt.ylabel('Number of places per neighborhoods')
plt.show()
