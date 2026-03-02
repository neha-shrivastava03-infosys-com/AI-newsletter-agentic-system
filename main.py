# main.py
import os
import json
from dotenv import load_dotenv

load_dotenv()

from agents.source_agent import SourceCollectorAgent
from agents.summarizer_agent import SummarizerAgent
from agents.style_agent import StyleAgent


RSS_SOURCES = [
    "https://techcrunch.com/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.coindesk.com/arc/outboundfeeds/rss/"
    "https://feeds.arstechnica.com/arstechnica/index"
    "https://www.medicalnewstoday.com/rss"
    "https://www.sciencedaily.com/rss/top/science.xml"
    "https://www.defensenews.com/arc/outboundfeeds/rss/"
    "https://cleantechnica.com/feed/"
    "https://feeds.feedburner.com/TheHackersNews"
    "https://www.nature.com/nature.rss"

]


def load_profile():

    base_dir = os.path.dirname(__file__)

    path = os.path.join(base_dir, "profiles", "techbro.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    


def run_newsletter_pipeline():

    influencer_profile = load_profile()

    # Initialize agents
    source_agent = SourceCollectorAgent(RSS_SOURCES)
    summarizer = SummarizerAgent()
    style_agent = StyleAgent(influencer_profile)

    print("Collecting news...")
    articles = source_agent.collect(limit=3)

    final_newsletter = []

    for article in articles:

        print(f"\nProcessing: {article['title']}")

        summary = summarizer.summarize(article["summary"])

        styled_version = style_agent.rewrite(summary)

        final_newsletter.append({
            "title": article["title"],
            "original_summary": summary,
            "styled_version": styled_version,
            "link": article["link"]
        })

    return final_newsletter
def generate_newsletter():
    """Wrapper function for Streamlit UI"""
    newsletter = run_newsletter_pipeline()

    # Convert to UI-friendly format
    formatted = []

    for item in newsletter:
        formatted.append({
            "title": item["title"],
            "styled": item["styled_version"],
            "link": item["link"]
        })

    return formatted

if __name__ == "__main__":

    newsletter = run_newsletter_pipeline()

    for item in newsletter:

        print("\n=============================")

        print(item["title"])

        print("\nStyled Version:\n")

        print(item["styled_version"])

