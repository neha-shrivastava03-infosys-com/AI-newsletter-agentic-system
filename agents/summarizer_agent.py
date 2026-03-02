# agents/summarizer_agent.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class SummarizerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

        self.prompt = ChatPromptTemplate.from_template("""
You are a professional news analyst.

Summarize the following news article in:
- 3 bullet points
- Maximum 100 words
- Clear and neutral tone

ARTICLE:
{article}
""")

        self.chain = self.prompt | self.llm | StrOutputParser()

    def summarize(self, article_text: str):
        return self.chain.invoke({"article": article_text})