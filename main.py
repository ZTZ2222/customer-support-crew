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

    print("Welcome to the Articles Crew Setup")
    print("---------------------------------------")
    topic = input("Please enter the main topic of your research: ")

    result = crew.kickoff(inputs={"topic": topic})

    file_name = topic.lower().replace(" ", "_")
    with open(f"{file_name}.md", "w") as f:
        f.write(result)
