from dotenv import load_dotenv
from crewai import Crew, Process
import agentops
from random import randint


from agents import ArticleAgents
from tasks import ArticleTasks


load_dotenv()
agentops.init(tags=["articles-crew"])


if __name__ == "__main__":
    crew = Crew(
        agents=[ArticleAgents.get_planner(), ArticleAgents.get_writer(),
                ArticleAgents.get_editor()],
        tasks=[ArticleTasks.plan(), ArticleTasks.write(), ArticleTasks.edit()],
        verbose=2,
    )

    result = crew.kickoff(inputs={"topic": "Bitcoin"})

    with open(f"output-{randint(0, 10000)}.md", "w") as f:
        f.write(result)
