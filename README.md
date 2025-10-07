# AI & Tech Careers: News Sentiment Dashboard (2025)

[![Live App](https://img.shields.io/badge/Live-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://ai-jobs-sentiment-7yvxgtyebegyncteakelep.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Stack](https://img.shields.io/badge/Stack-Streamlit%20|%20pandas%20|%20NLTK%20|%20Matplotlib%20|%20Seaborn-4c1)](#technologies-used)

An end-to-end project exploring how **Artificial Intelligence (AI)** is portrayed in technology and data-related career news.  
This project combines **data analysis**, **sentiment classification**, and **interactive visualization** to examine how news outlets describe AI’s impact on jobs in 2024–2025.

**Live Dashboard:** [AI & Tech Careers: News Sentiment Dashboard](https://ai-jobs-sentiment-7yvxgtyebegyncteakelep.streamlit.app/)

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Demo](#demo)
- [Data](#data)
- [Project Structure](#project-structure)
- [Quickstart](#quickstart)
- [Local Development](#local-development)
- [Configuration](#configuration)
- [Methodology](#methodology)
- [Key Insights](#key-insights)
- [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)
- [Author](#author)

---

## Overview

The integration of AI into the workforce has inspired both optimism and uncertainty.  
This project investigates **how AI-related job news headlines** reflect public perception by applying sentiment analysis and visualizing results in a live dashboard.  

By combining natural language processing (NLP), Python-based data analysis, and Streamlit, the project enables users to interact with news sentiment data and explore trends over time.

---

## Key Features

- **Automated Sentiment Analysis**  
  Headlines are labeled as *positive*, *neutral*, or *negative* using a natural language processing model (e.g., NLTK/VADER).

- **Interactive Streamlit Dashboard**  
  Explore sentiment distribution, filter by publisher or keyword, and track tone over time.

- **Reproducible Workflow**  
  Clean and transparent steps for data collection, preprocessing, classification, and visualization.

- **Lightweight, Visual, and Live**  
  A simple setup deployable to Streamlit Cloud with instant updates.

---

## Demo

**Live App:** [https://ai-jobs-sentiment-7yvxgtyebegyncteakelep.streamlit.app/](https://ai-jobs-sentiment-7yvxgtyebegyncteakelep.streamlit.app/)

The dashboard includes:
- Headline summary metrics (total, positive, negative, neutral)
- Sentiment distribution bar chart
- Filtering by publisher or search term
- Sentiment-over-time trend visualization

---

## Data

| File | Description |
|------|--------------|
| `ai_jobs_news_headlines.csv` | Raw scraped headlines and metadata |
| `ai_jobs_news_headlines_sentiment.csv` | Processed dataset with sentiment labels |
| `ai_impact_jobs_sentiment_analysis.ipynb` | Notebook for cleaning, analysis, and sentiment classification |
| `streamlit_app.py` | Streamlit dashboard for visualization |

Each record includes:
- `title` — headline text  
- `publisher` — news source  
- `published date` — date of publication  
- `search_term` — keyword or topic used for scraping  
- `sentiment` — sentiment category (*positive*, *neutral*, or *negative*)

---

## Project Structure

ai-jobs-sentiment/
├── ai_impact_jobs_sentiment_analysis.ipynb # Data analysis and sentiment modeling
├── ai_jobs_news_headlines.csv # Raw dataset
├── ai_jobs_news_headlines_sentiment.csv # Processed dataset
├── streamlit_app.py # Streamlit dashboard
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## Quickstart

To run this project locally:

```bash
# 1. Clone the repository
git clone https://github.com/Jae15/ai-jobs-sentiment.git
cd ai-jobs-sentiment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run streamlit_app.py

```
---
# Local Development

To reproduce or extend the analysis:

Open the notebook:
ai_impact_jobs_sentiment_analysis.ipynb

Run the data cleaning and sentiment classification steps.

Export the processed file as:
ai_jobs_news_headlines_sentiment.csv

Launch the dashboard:
streamlit run streamlit_app.py
---

# Pipeline Overview

Data Collection → Cleaning → Sentiment Classification → Export → Visualization


Data Collection
- Gather news headlines on AI and employment using topic-specific queries.

Preprocessing
- Remove duplicates, clean text, and standardize formatting.

Sentiment Analysis
- Apply rule-based or ML-driven sentiment scoring using NLP techniques.

Visualization
- Render insights interactively using Streamlit, Seaborn, and Matplotlib.

# Key Insights

- The majority of AI-related headlines display a neutral tone, suggesting balanced coverage.

- Positive sentiment has grown in 2024–2025, signaling increased optimism about AI’s potential in the workforce.

- A smaller segment of publishers consistently emphasizes automation risks and job displacement.

# Future Enhancements

- Integrate transformer-based sentiment models (e.g., BERT, RoBERTa) for higher precision.

- Expand data sources to include social media, tech blogs, and research reports.

- Automate data collection and dashboard refresh cycles.

- Add topic modeling and clustering to identify recurring AI-related themes.

- Incorporate geographic or publisher bias analysis for deeper insights.

# Technologies Used

- Python – Core programming language

- pandas – Data manipulation and analysis

- NLTK / VADER – Sentiment analysis

- Matplotlib / Seaborn – Visualization

- Streamlit – Interactive dashboard

- Google Colab / Jupyter – Notebook development environment

---

Author
- Jae Mwangi
- Data Professional – SQL | Python | AI Research | Web Development

GitHub: Jae15

Live App: AI Jobs Sentiment Dashboard




