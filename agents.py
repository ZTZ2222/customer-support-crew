import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq


class ArticleAgents:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = "llama3-70b-8192"

    _planner = None
    _writer = None
    _editor = None

    @classmethod
    def get_planner(cls):
        if cls._planner is None:
            cls._planner = cls._create_agent(
                role="Content Planner",
                goal="Plan engaging and factually accurate content on {topic}",
                backstory=dedent("""
                    You're working on planning a blog article 
                    about the topic: {topic}.
                    You collect information that helps the 
                    audience learn something 
                    and make informed decisions. 
                    Your work is the basis for 
                    the Content Writer to write an article on this topic.
                    """)
            )
        return cls._planner

    @classmethod
    def get_writer(cls):
        if cls._writer is None:
            cls._writer = cls._create_agent(
                role="Content Writer",
                goal=dedent("""
                    Write insightful and factually accurate 
                    opinion piece about the topic: {topic}
                    """),
                backstory=dedent("""
                    You're working on a writing 
                    a new opinion piece about the topic: {topic}. 
                    You base your writing on the work of 
                    the Content Planner, who provides an outline 
                    and relevant context about the topic. 
                    You follow the main objectives and 
                    direction of the outline, 
                    as provide by the Content Planner. 
                    You also provide objective and impartial insights 
                    and back them up with information 
                    provide by the Content Planner. 
                    You acknowledge in your opinion piece 
                    when your statements are opinions 
                    as opposed to objective statements.
                    """)
            )
        return cls._writer

    @classmethod
    def get_editor(cls):
        if cls._editor is None:
            cls._editor = cls._create_agent(
                role="Editor",
                goal=dedent("""
                    Edit a given blog post to align with 
                    the writing style of the organization. 
                    """),
                backstory=dedent("""
                    You are an editor who receives a blog post 
                    from the Content Writer. 
                    Your goal is to review the blog post 
                    to ensure that it follows journalistic best practices,
                    provides balanced viewpoints 
                    when providing opinions or assertions, 
                    and also avoids major controversial topics 
                    or opinions when possible.
                    """)
            )
        return cls._editor

    @classmethod
    def _create_agent(cls, **kwargs):
        return Agent(
            **kwargs,
            allow_delegation=False,
            llm=ChatGroq(api_key=cls.GROQ_API_KEY, model=cls.MODEL),
            max_rpm=30,
            max_iter=5,
            verbose=True,
        )
