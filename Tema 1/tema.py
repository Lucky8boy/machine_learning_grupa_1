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
        data['Price'].append(random.randint(80, 150))
        data['Occupancy'].append(random.randint(50, 90))
        data['Review_Score'].append(round(random.uniform(3.5, 5.0), 1))

    df = pd.DataFrame(data)
    print(df)

    df.to_csv('airbnb.csv', index=False)
else:  # dataset already exists
    df = pd.read_csv('airbnb.csv')

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
