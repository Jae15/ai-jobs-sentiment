
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI & Tech Careers: News Sentiment Dashboard (2025)", layout="wide")

st.title("AI & Tech Careers: News Sentiment Dashboard (2025)")
st.write(
    "An interactive dashboard analyzing recent news headlines about the impact of AI on software and data jobs."
)

@st.cache_data
def load_data():
    return pd.read_csv('ai_jobs_news_headlines.csv')

df = load_data()

# Show headline count and basic stats
st.subheader("Key Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Headlines", len(df))
col2.metric("Unique Publishers", df['publisher'].nunique())
col3.metric("Search Terms", df['search_term'].nunique())
date_min = pd.to_datetime(df['published date']).min().strftime('%Y-%m-%d')
date_max = pd.to_datetime(df['published date']).max().strftime('%Y-%m-%d')
col4.metric("Date Range", f"{date_min} to {date_max}")

st.write("Available columns:", df.columns.tolist())
st.write("First few rows:")
st.write(df.head())

# Publisher distribution bar chart
st.subheader("Headline Distribution by Publisher")
publisher_counts = df['publisher'].value_counts()
fig, ax = plt.subplots()
publisher_counts.plot(kind='bar', ax=ax)
ax.set_xlabel("Publisher")
ax.set_ylabel("Number of Headlines")
plt.xticks(rotation=45)
st.pyplot(fig)

# Explore by search term or publisher
st.subheader("Explore Headlines")
with st.expander("Filter by"):
    filter_by = st.selectbox("Select filter:", ("search_term", "publisher"))
    options = df[filter_by].dropna().unique()
    selected = st.multiselect(f"Choose {filter_by}(s):", options, default=options[:1])
    filtered = df[df[filter_by].isin(selected)]

if filtered.empty:
    st.write("No results for this selection.")
else:
    st.write(filtered[['title', 'description', 'published date', 'publisher', 'search_term']].head(20))

# Headline frequency over time
if 'published date' in df.columns:
    st.subheader("Headline Frequency Over Time")
    df['published date'] = pd.to_datetime(df['published date'], errors='coerce')
    daily_count = df.groupby(pd.Grouper(key='published date', freq='D')).size()
    fig2, ax2 = plt.subplots()
    daily_count.plot(ax=ax2)
    ax2.set_ylabel("Number of Headlines")
    ax2.set_title("Headlines by Day")
    st.pyplot(fig2)

st.markdown("---")
st.write("Built with Python, pandas, matplotlib, seaborn, and Streamlit.")
