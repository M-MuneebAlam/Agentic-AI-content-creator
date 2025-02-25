from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

topic = "Anthropic agentic design patterns and Langgraph Functional API"

#Tool 1
llm = LLM(model="gpt-4o-mini")

#Tool 2
serper_tool = SerperDevTool(n=5)

#Agent 1
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal=f"Research, analyze and synthesize the latest information about {topic} from reliable sources",
    backstory="You are a seasoned research analyst with a knack for finding and synthesizing information from various sources",
    allow_delegation=False,
    llm=llm, 
    tools=[serper_tool],
    verbose=True
)

#Agent 2
content_writer = Agent(
    role="Content Writer",
    goal="Transform research findings into a comprehensive and engaging blog post while maintaining accuracy and clarity",
    backstory="You are a content writer with a knack for writing engaging and informative blog posts",
    allow_delegation=False,
    llm=llm,
    verbose=True
)


#Task 1
research_task = Task(
    description=("""
        1. Conduct thorough research on the {topic} including:
            - Recent developments and new
            - Key industry trends and innovations
            - Expert opinions and insights
            - Any other relevant information
        2. Evaluate the credibility of each source and ensure they are reliable and authoritative
        3. Summarize the findings in a structured manner
        4. Provide a list of references and sources used
    """),
    expected_output="""A research report containing:
        - Executive summary of key findings
        - Comprehensive analysis of the latest trends and innovations
        - List of verified facts and statistics
        - All citations and links to original sources
        - Clear categorization of main themes and patterns
        Please format with clear sections and bullet points for easy reference
    """,
    agent = senior_research_analyst

)

#Task 2
write_blog_post = Task(
    description=("""
        Using the research findings provided, create an engaging blog post that:
        1. Transforms technical concepts into accessible and engaging content
        2. Maintains all factual accuracy and citations from the research
        3. Includes:
            - Attention-grabbing introduction
            - Well-structured body sections with clear headings
            - Examples, case studies, and practical applications
            - Compelling conclusion with takeaways
        4. Presents complex ideas in a clear and concise manner 
        5. Uses a conversational tone and engaging writing style
        6. Includes a call to action for readers to learn more"""),
        expected_output="""A well-written blog post with:
            - Clear and engaging introduction
            - Structured body sections with examples and case studies
            - Compelling conclusion with actionable insights
            - All citations and references to original sources
            - Engaging writing style and conversational tone
            - Follows proper markdown formatting, use H1 for the title and H3 for the subheadings
        """,
        agent = content_writer
)

crew = Crew(
    agents=[senior_research_analyst, content_writer],
    tasks=[research_task, write_blog_post],
    verbose=True
)

result = crew.kickoff(inputs={"topic": topic})

print(result)
