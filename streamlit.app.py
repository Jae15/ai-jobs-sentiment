
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="AI & Data Careers: News Sentiment", layout="wide")

# Title and Intro
st.title("AI & Tech Careers: News Sentiment Dashboard (2025)")
st.write(
    "An interactive dashboard analyzing recent news sentiment about the impact of AI on software and data jobs. "
    "Data is automatically scraped and classified for sentiment (positive/neutral/negative)."
)

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('ai_jobs_news_headlines_sentiment.csv')
df = load_data()

# Show headline count
st.subheader("Key Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Headlines", len(df))
col2.metric("Positive", (df['sentiment']=="positive").sum())
col3.metric("Negative", (df['sentiment']=="negative").sum())
col4.metric("Neutral", (df['sentiment']=="neutral").sum())

# Sentiment distribution bar chart
st.subheader("Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values,
            palette={"positive":"green", "negative":"red", "neutral":"gray"}, ax=ax)
ax.set_xlabel("Sentiment")
ax.set_ylabel("Number of Headlines")
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
    st.write(filtered[['title', 'sentiment', 'published date', 'publisher']].head(20))

# (Optional) Sentiment over time (if you have dates)
if 'published date' in df.columns:
    st.subheader("Sentiment Trends Over Time")
    df['published date'] = pd.to_datetime(df['published date'], errors='coerce')
    daily = df.groupby([pd.Grouper(key='published date', freq='D'),'sentiment']).size().unstack(fill_value=0)
    fig2, ax2 = plt.subplots()
    daily.plot(ax=ax2)
    ax2.set_ylabel("Number of Headlines")
    ax2.set_title("Sentiment by Day")
    st.pyplot(fig2)

st.markdown("---")
st.write("Built with Python, pandas, NLTK, matplotlib, seaborn, and Streamlit.")
