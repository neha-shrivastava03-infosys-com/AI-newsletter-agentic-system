# agents/source_agent.py

import feedparser
from typing import List, Dict


class SourceCollectorAgent:
    def __init__(self, sources: List[str]):
        self.sources = sources

    def collect(self, limit: int = 5) -> List[Dict]:
        articles = []

        for url in self.sources:
            feed = feedparser.parse(url)

            for entry in feed.entries[:limit]:
                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.get("summary", "")
                })

        return articles