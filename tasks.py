from textwrap import dedent
from crewai import Task
from crewai_tools import ScrapeWebsiteTool

from agents import ArticleAgents


class ArticleTasks:
    docs_scrape_tool = ScrapeWebsiteTool(
        website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
    )

    @classmethod
    def inquiry_resolution(cls):
        return Task(
            description=dedent("""
                {customer} just reached out with a super important ask:\n
                {inquiry}\n\n
                {person} from {customer} is the one that reached out. 
                Make sure to use everything you know 
                to provide the best support possible.
                You must strive to provide a complete 
                and accurate response to the customer's inquiry.
                """),
            expected_output=dedent("""
                A detailed, informative response to the 
                customer's inquiry that addresses 
                all aspects of their question.\n
                The response should include references 
                to everything you used to find the answer, 
                including external data or solutions. 
                Ensure the answer is complete, 
                leaving no questions unanswered, and maintain a helpful and friendly 
                tone throughout.
                """),
            agent=ArticleAgents.get_support_agent(),
            tools=[cls.docs_scrape_tool],
        )

    @classmethod
    def quality_assurance_review(cls):
        return Task(
            description=dedent("""
                Review the response drafted by the Senior Support Representative for {customer}'s inquiry. 
                Ensure that the answer is comprehensive, accurate, and adheres to the 
                high-quality standards expected for customer support.\n
                Verify that all parts of the customer's inquiry 
                have been addressed 
                thoroughly, with a helpful and friendly tone.\n
                Check for references and sources used to 
                 find the information, 
                ensuring the response is well-supported and 
                leaves no questions unanswered.
                """),
            expected_output=dedent("""
                A final, detailed, and informative response 
                ready to be sent to the customer.\n
                This response should fully address the 
                customer's inquiry, incorporating all 
                relevant feedback and improvements.\n
                Don't be too formal, we are a chill and cool company 
                but maintain a professional and friendly tone throughout.
                """),
            agent=ArticleAgents.get_support_quality_assurance_agent(),
        )
