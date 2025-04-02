#
# import streamlit as st
# import os
# from main import app as fastapi_app, fetch_news, generate_final_output
# import uvicorn
# import threading
# import socket
#
# # Define BASE_URL globally with a default value
# BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # Overridden on Spaces or updated by run_fastapi
#
# # Streamlit frontend
# st.title("📰 News Summarizer & Sentiment Analysis")
# st.write("Enter a company name to get the latest news, sentiment, and summaries.")
#
# company_name = st.text_input("Enter Company Name (e.g., Tesla, Google, Apple)", "Tesla")
#
# if st.button("Fetch News"):
#     with st.spinner("Fetching news..."):
#         news_articles = fetch_news(company_name)
#         news_data = generate_final_output(news_articles, company_name)
#         if "Articles" in news_data:
#             st.subheader(f"📰 Latest News on {news_data['Company']}")
#             for idx, article in enumerate(news_data["Articles"]):
#                 st.markdown(f"### {idx + 1}. {article['Title']}")
#                 st.write(f"**Sentiment:** {article['Sentiment']}")
#                 st.write(f"**Topics:** {', '.join(article['Topics'])}")
#                 st.write(f"**Summary:** {article['Summary']}")
#                 st.write(f"🔗 [Read Full Article]({article['Link']})")
#                 if article["Audio"]:
#                     audio_url = f"{BASE_URL}{article['Audio']}"
#                     st.audio(audio_url, format="audio/mp3")
#                 st.markdown("---")
#         else:
#             st.error("❌ Failed to fetch news. Please try again.")
#
# def is_port_in_use(port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         return s.connect_ex(('0.0.0.0', port)) == 0
#
# def run_fastapi():
#     global BASE_URL  # Declare BASE_URL as global to modify it
#     port = 8000
#     if is_port_in_use(port):
#         port = 8001  # Fallback port
#         if is_port_in_use(port):
#             st.error("Ports 8000 and 8001 are in use. FastAPI cannot start.")
#             return
#     BASE_URL = os.getenv("BASE_URL", f"http://localhost:{port}")  # Update BASE_URL based on port
#     uvicorn.run(fastapi_app, host="0.0.0.0", port=port)
#
# if __name__ == "__main__":
#     threading.Thread(target=run_fastapi, daemon=True).start()

import streamlit as st
import os
from main import app as fastapi_app, fetch_news, generate_final_output
import uvicorn
import threading
import socket

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # Overridden on Spaces

st.title("📰 News Summarizer & Sentiment Analysis")
st.write("Enter a company name to get the latest news, sentiment, and summaries.")

company_name = st.text_input("Enter Company Name (e.g., Tesla, Google, Apple)", "Tesla")

if st.button("Fetch News"):
    with st.spinner("Fetching news..."):
        news_articles = fetch_news(company_name)
        news_data = generate_final_output(news_articles, company_name)
        if "Articles" in news_data:
            st.subheader(f"📰 Latest News on {news_data['Company']}")
            for idx, article in enumerate(news_data["Articles"]):
                st.markdown(f"### {idx + 1}. {article['Title']}")
                st.write(f"**Sentiment:** {article['Sentiment']}")
                st.write(f"**Topics:** {', '.join(article['Topics'])}")
                st.write(f"**Summary:** {article['Summary']}")
                st.write(f"🔗 [Read Full Article]({article['Link']})")
                if article["Audio"]:
                    audio_url = f"{BASE_URL}{article['Audio']}"
                    st.audio(audio_url, format="audio/mp3")
                st.markdown("---")
        else:
            st.error("❌ Failed to fetch news. Please try again.")

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('0.0.0.0', port)) == 0

def run_fastapi():
    global BASE_URL
    port = 8000
    if is_port_in_use(port):
        st.warning(f"Port {port} is in use, retrying once...")
        threading.Event().wait(2)  # Wait briefly and retry
        if is_port_in_use(port):
            st.error(f"Port {port} still in use. FastAPI cannot start.")
            return
    BASE_URL = os.getenv("BASE_URL", f"http://localhost:{port}")
    uvicorn.run(fastapi_app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    threading.Thread(target=run_fastapi, daemon=True).start()