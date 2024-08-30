import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from your GitHub repository
url = "https://github.com/shamiim611/global_fertility_rate/upload/main"
df = pd.read_csv(url,on_bad_lines='skip')

# Rename 'Country Name' to 'Country_Name'
df.rename(columns={'Country Name': 'Country_Name'}, inplace=True)

# Streamlit App
st.title("Global Fertility Rate Analysis")
st.write("This app allows you to explore fertility rates across different countries and years.")

# Sidebar for user inputs
st.sidebar.header("User Input")
selected_country = st.sidebar.selectbox("Select a country", df['Country_Name'].unique())
selected_year = st.sidebar.selectbox("Select a year", df.columns[2:])

# Line Chart: Trend of fertility rates over the years for the selected country
st.subheader(f"Fertility Rate Trend for {selected_country}")
country_data = df[df['Country_Name'] == selected_country].set_index('Country_Name').T[2:]
country_data.columns = [selected_country]
st.line_chart(country_data)

# Bar Chart: Fertility rates across different countries for the selected year
st.subheader(f"Fertility Rates Across Countries in {selected_year.split()[0]}")
sorted_df = df[['Country_Name', selected_year]].sort_values(by=selected_year, ascending=False)
st.bar_chart(sorted_df.set_index('Country_Name'))

# Heatmap: Fertility rates over time for all countries
st.subheader("Heatmap of Fertility Rates Over Time")
heatmap_data = df.set_index('Country_Name').drop(columns=['Country Code']).T
fig, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(heatmap_data, cmap="YlGnBu", ax=ax)
st.pyplot(fig)
