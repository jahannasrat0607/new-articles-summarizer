---
title: News Articles Summarizer
emoji: 📰
colorFrom: blue
colorTo: green
sdk: docker
app_file: Dockerfile
pinned: false
---

# News Articles Summarizer

## Overview
This application extracts, summarizes, and analyzes news articles related to a given company. It also performs sentiment analysis, comparative analysis, and converts the summary into Hindi speech.

## Features
- Extract news articles using NewsAPI.
- Perform text summarization using a Transformer model.
- Conduct sentiment analysis and comparative insights.
- Convert summarized content into Hindi speech using a TTS model.
- Provide a web-based UI using Streamlit.
- Backend API using FastAPI.
- Deployable on Hugging Face Spaces.

## Project Structure
```
news-article-summarizer/
│── api/
│   ├── main.py  # FastAPI backend
│   ├── static/
│   │   ├── audio/  # Stores generated audio files
│── frontend/
│   ├── app.py  # Streamlit frontend
│── utils/
│   ├── news_utils.py  # Helper functions
│── Dockerfile
│── requirements.txt
│── README.md
```

## Installation
### Prerequisites
- Python 3.9+
- Pip
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://huggingface.co/spaces/jahan0607/news-articles-summarizer
   cd news-articles-summarizer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the backend (FastAPI):
   ```sh
   uvicorn api.main:app --host 0.0.0.0 --port 7860
   ```

4. Run the frontend (Streamlit):
   ```sh
   streamlit run frontend/app.py --server.port 7861 --server.address 0.0.0.0
   ```

## API Usage
### Fetch News
Endpoint: `GET /fetch_news?company=Tesla`

Response:
```json
{
  "Company": "Tesla",
  "Articles": [
    {
      "Title": "Tesla's Market Performance",
      "Summary": "Tesla's stock surged...",
      "Sentiment": "Positive",
      "Topics": ["Stock Market", "Innovation"],
      "Audio": "<audio-url>",
      "Link": "<full-article-link>"
    }
  ]
}
```

## Deployment on Hugging Face Spaces
1. Ensure all required files exist (`Dockerfile`, `requirements.txt`).
2. Push changes to the Hugging Face Space:
   ```sh
   git add .
   git commit -m "Deploying news summarizer"
   git push
   ```
3. The application should be live on Hugging Face Spaces.

## License
This project is for educational purposes only. Feel free to modify and enhance it.

---
For any issues, contact [Nasrat Jahan](https://huggingface.co/jahan0607).
