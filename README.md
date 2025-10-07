Project Overview

The rapid advancement of AI has generated both optimism and concern in the job market, particularly within technology and data-focused careers.
This project gathers recent news headlines about AI and employment, classifies their sentiment, and visualizes the trends through a Streamlit web app.

The repository includes:

ai_impact_jobs_sentiment_analysis.ipynb – notebook for data collection, cleaning, and sentiment analysis.

ai_jobs_news_headlines.csv – raw dataset containing collected headlines and metadata.

ai_jobs_news_headlines_sentiment.csv – processed dataset with sentiment classifications.

streamlit_app.py – interactive dashboard for visualizing sentiment data.

Features

Automated Sentiment Classification
Headlines are analyzed and labeled as positive, neutral, or negative using an NLP-based sentiment model.

Interactive Streamlit Dashboard
Users can explore overall sentiment, filter results by publisher or keyword, and view sentiment trends over time.

Trend Analysis
Visualizes how news sentiment changes by day or topic, allowing for exploration of shifts in tone over time.

Clean, Reproducible Workflow
The notebook contains the complete pipeline from data cleaning to model inference and export.

Dashboard Overview

The Streamlit dashboard provides:

Summary Metrics – total headlines and sentiment counts.

Sentiment Distribution Chart – a visual overview of how positive, neutral, and negative headlines compare.

Filtering Tools – explore results by publisher or search term.

Time-Series Trends – sentiment evolution by publication date.

Explore the live dashboard here:
https://ai-jobs-sentiment-7yvxgtyebegyncteakelep.streamlit.app/

Data
File	Description
ai_jobs_news_headlines.csv	Raw scraped headlines with publisher and date fields
ai_jobs_news_headlines_sentiment.csv	Processed dataset with sentiment scores
ai_impact_jobs_sentiment_analysis.ipynb	Notebook containing data preparation and analysis
streamlit_app.py	Streamlit dashboard for interactive visualization

Each record typically contains:

title – the headline text

publisher – the news outlet or website

published date – date of publication

search_term – the query used to find the article

sentiment – sentiment label: positive, neutral, or negative

Installation and Usage
1. Clone the repository
git clone https://github.com/Jae15/ai-jobs-sentiment.git
cd ai-jobs-sentiment

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app locally
streamlit run streamlit_app.py

4. Open in your browser

Go to: http://localhost:8501

Methodology

Data Collection – Gathered recent news headlines about AI and employment using search queries.

Text Preprocessing – Cleaned and standardized text data, removed duplicates and irrelevant entries.

Sentiment Analysis – Classified sentiment using a natural language processing approach (NLTK/VADER or similar).

Visualization – Built interactive data visualizations using Matplotlib, Seaborn, and Streamlit.

Technologies Used

Python

pandas

NLTK / VADER

Matplotlib

Seaborn

Streamlit

Google Colab

Insights and Observations

The majority of news headlines maintain a neutral tone toward AI’s effect on jobs.

Positive sentiment has increased, particularly in 2024–2025, highlighting growing optimism about AI-driven job creation.

Some publishers remain focused on automation risks, contributing to negative sentiment trends.

Future Improvements

Integrate transformer-based sentiment models (e.g., BERT, RoBERTa) for higher accuracy.

Expand data sources to include blogs and social media content.

Add topic modeling and keyword clustering to identify emerging themes.

Automate data updates and deploy continuous monitoring.

Author

Jae Mwangi
Data Professional – SQL | Python | AI Research | Web Development
GitHub: Jae15

Live App: AI Jobs Sentiment Dashboard
