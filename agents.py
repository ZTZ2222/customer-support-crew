import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq


class ArticleAgents:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = "llama3-70b-8192"

    _support_agent = None
    _support_quality_assurance_agent = None
    _editor = None

    @classmethod
    def get_support_agent(cls):
        if cls._support_agent is None:
            cls._support_agent = cls._create_agent(
                role="Senior Support Representative",
                goal="Be the most friendly and helpful support representative in your team",
                backstory=dedent("""
                    You work at crewAI (https://crewai.com) and 
                    You are now working on providing 
                    support to {customer}, a super important customer 
                    for your company.
                    You need to make sure that you provide the best support!
                    Make sure to provide full complete answers, 
                    and make no assumptions.
                    """),
                allow_delegation=False,
            )
        return cls._support_agent

    @classmethod
    def get_support_quality_assurance_agent(cls):
        if cls._support_quality_assurance_agent is None:
            cls._support_quality_assurance_agent = cls._create_agent(
                role="Support Quality Assurance Specialist",
                goal=dedent("""
                    Get recognition for providing the
                    best support quality assurance in your team
                    """),
                backstory=dedent("""
                    You work at crewAI (https://crewai.com) and 
                    are now working with your team 
                    on a request from {customer} ensuring that 
                    the support representative is 
                    providing the best support possible.\n
                    You need to make sure that the support representative 
                    is providing full
                    complete answers, and make no assumptions.
                    """)
            )
        return cls._support_quality_assurance_agent

    @classmethod
    def _create_agent(cls, **kwargs):
        return Agent(
            **kwargs,
            llm=ChatGroq(api_key=cls.GROQ_API_KEY, model=cls.MODEL),
            max_rpm=30,
            max_iter=5,
            verbose=True,
        )
