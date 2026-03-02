import streamlit as st
import os
import json
from dotenv import load_dotenv

from agents.source_agent import SourceCollectorAgent
from agents.summarizer_agent import SummarizerAgent
from agents.style_agent import StyleAgent

load_dotenv()

RSS_SOURCES = [
    "https://techcrunch.com/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.coindesk.com/arc/outboundfeeds/rss/"
]


def load_profile():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "profiles", "techbro.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


st.set_page_config(page_title="AI Newsletter Agent", layout="wide")

st.title("🤖 AI Newsletter Agentic System")
st.write("Autonomous multi-agent AI newsletter generator")

if st.button("Generate Newsletter"):

    with st.spinner("Collecting and processing news..."):

        profile = load_profile()

        source_agent = SourceCollectorAgent(RSS_SOURCES)
        summarizer = SummarizerAgent()
        style_agent = StyleAgent(profile)

        articles = source_agent.collect(limit=3)

        for article in articles:
            st.subheader(article["title"])

            summary = summarizer.summarize(article["summary"])
            styled = style_agent.rewrite(summary)

            st.write("**Styled Version:**")
            st.write(styled)
            st.markdown("---")
