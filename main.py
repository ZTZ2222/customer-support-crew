from textwrap import dedent
from dotenv import load_dotenv
from crewai import Crew
import agentops


from agents import ArticleAgents
from tasks import ArticleTasks


load_dotenv()
agentops.init(tags=["customer-support-crew"])


if __name__ == "__main__":
    crew = Crew(
        agents=[ArticleAgents.get_support_agent(
        ), ArticleAgents.get_support_quality_assurance_agent()],
        tasks=[ArticleTasks.inquiry_resolution(
        ), ArticleTasks.quality_assurance_review()],
        verbose=2,
        memory=True,
    )

    result = crew.kickoff(inputs={
        "customer": "DeepLearningAI",
        "inquiry": dedent("""
            I need help with setting up a Crew 
            and kicking it off, specifically 
            how can I add memory to my crew? 
            Can you provide guidance?
            """),
        "person": "Andrew",
    })

    with open("output.md", "w") as f:
        f.write(result)
