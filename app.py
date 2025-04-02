import streamlit as st
from fastapi import FastAPI
from main import app as fastapi_app, fetch_news, generate_final_output
import uvicorn
import threading

# Mount FastAPI app within Streamlit
st.title("📰 News Summarizer & Sentiment Analysis")
st.write("Enter a company name to get the latest news, sentiment, and summaries.")

company_name = st.text_input("Enter Company Name (e.g., Tesla, Google, Apple)", "Tesla")

if st.button("Fetch News"):
    with st.spinner("Fetching news..."):
        # Call FastAPI endpoint internally
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
                    st.audio(f"https://jahan0607-news-articles-summarizer.hf.space{article['Audio']}",
                             format="audio/mp3")
                # if article["Audio"]:
                #     st.audio(article["Audio"].replace("http://127.0.0.1:8000", ""), format="audio/mp3")
                st.markdown("---")
        else:
            st.error("❌ Failed to fetch news. Please try again.")

# Run FastAPI in a thread
def run_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    threading.Thread(target=run_fastapi, daemon=True).start()
    st.run(["--server.port", "7860", "--server.address", "0.0.0.0"])