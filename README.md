
# News Articles Summarizer

Extracts, summarizes, and analyzes news articles for a company with sentiment analysis, comparative insights, and Hindi TTS.

## Features
- Scrapes 10+ articles with **BeautifulSoup**.
- Summarizes using **BART (Hugging Face)**.
- Sentiment & comparative analysis.
- Hindi TTS output.
- **Streamlit** UI with **FastAPI** backend.
- For **Hugging Face Spaces**.

## Setup
1. Clone: `git clone https://github.com/jahannasrat0607/news-articles-summarizer.git`
2. Install: `pip install -r requirements.txt`
3. Run FastAPI: `uvicorn api:app --host 0.0.0.0 --port 8000`
4. Run Streamlit: `streamlit run app.py --server.port 8501 --server.address 0.0.0.0`

## License
This project is for educational purposes only. Feel free to modify and enhance it.

---
For any issues, contact [Nasrat Jahan](https://huggingface.co/jahan0607).
