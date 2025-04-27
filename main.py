# import tools
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns

# file origin
folder_path = r"C:\Users\S Das\Downloads\archive (1)\*.csv"

# Read and combine all CSVs in folder
df = pd.concat([pd.read_csv(f) for f in glob.glob(folder_path)], ignore_index=True)

# Make sure 'Date' is in datetime format (optional but good)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Calculate top 10 countries by New Cases
top_country = df.groupby('Country/Region')['New cases'].sum().sort_values(ascending=False).head(10).index

# Create subplots
fig, ax = plt.subplots(1, 4, figsize=(20, 6))  # wider figure for better view

# --- New Cases ---
df_new_cases = df[df['Country/Region'].isin(top_country)]
df_new_cases_grouped = df_new_cases.groupby('Country/Region')['New cases'].sum().sort_values(ascending=False)
df_new_cases_grouped.plot(kind='bar', ax=ax[0], color='skyblue')
ax[0].set_title('New Cases - D[1]')
ax[0].set_xlabel('Country')
ax[0].set_ylabel('Cases')

# --- Total Cases ---
df_total_cases = df[df['Country/Region'].isin(top_country)]
df_total_cases_grouped = df_total_cases.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
df_total_cases_grouped.plot(kind='bar', ax=ax[1], color='orange')
ax[1].set_title('Total Cases - D[2]')
ax[1].set_xlabel('Country')
ax[1].set_ylabel('Cases')

# --- New Deaths ---
df_new_deaths = df[df['Country/Region'].isin(top_country)]
df_new_deaths_grouped = df_new_deaths.groupby('Country/Region')['New deaths'].sum().sort_values(ascending=False)
df_new_deaths_grouped.plot(kind='bar', ax=ax[2], color='red')
ax[2].set_title('New Deaths - D[3]')
ax[2].set_xlabel('Country')
ax[2].set_ylabel('Deaths')

# --- New Recovered ---
df_new_recovered = df[df['Country/Region'].isin(top_country)]
df_new_recovered_grouped = df_new_recovered.groupby('Country/Region')['New recovered'].sum().sort_values(ascending=False)
df_new_recovered_grouped.plot(kind='bar', ax=ax[3], color='green')
ax[3].set_title('New Recovered - D[4]')
ax[3].set_xlabel('Country')
ax[3].set_ylabel('Recovered')

# Adjust layout
plt.tight_layout()
plt.show()




# HEATMAP:

# Load
df = pd.read_csv(r"C:\Users\S Das\Downloads\archive (1)\usa_county_wise.csv")

# Fix date
df['date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')

# Make sure correct column names
print(df.columns)

# Pick top 10 countries
top_country = df.groupby('Country_Region')['Confirmed'].sum().sort_values(ascending=False).head(10).index

# Filter
df_top = df[df['Country_Region'].isin(top_country)]

# Pivot
pivot = df_top.pivot_table(values='Confirmed', index='Country_Region', columns='date', aggfunc='sum')

# Plot heatmap
plt.figure()
sns.heatmap(pivot, cmap='YlGnBu', cbar_kws={'label': 'Confirmed Cases'})
plt.title(' Top 10 Countries Over Time - Heat Map')
plt.xlabel('Date')
plt.ylabel('Country')
plt.show()
