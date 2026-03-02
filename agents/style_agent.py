# agents/style_agent.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class StyleAgent:
    def __init__(self, influencer_profile: dict):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

        self.profile = influencer_profile

        self.prompt = ChatPromptTemplate.from_template("""
You are a content rewriting agent.

Rewrite the news summary in the voice of this influencer:

INFLUENCER NAME: {name}

TONE:
{tone}

STYLE RULES:
{style_rules}

VOCABULARY CONSTRAINTS:
- Must use these words frequently: {must_words}
- Avoid these words entirely: {avoid_words}

CONTENT TO REWRITE:
{content}

Rules:
- Keep under 150 words
- Maintain factual accuracy
- Follow tone strictly
""")

        self.chain = self.prompt | self.llm | StrOutputParser()

    def rewrite(self, content: str):
        return self.chain.invoke({
            "name": self.profile["name"],
            "tone": self.profile["tone"],
            "style_rules": self.profile["style_rules"],
            "must_words": ", ".join(self.profile["must_words"]),
            "avoid_words": ", ".join(self.profile["avoid_words"]),
            "content": content
        })