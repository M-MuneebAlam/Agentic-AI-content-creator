from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Initialize page config
st.set_page_config(page_title="Agentic Research Assistant and Writer", page_icon=":computer:", layout="wide")
st.title("Content Research Assistant and Writer powered by CrewAI")
st.markdown("Generate a blog post based on a given topic using AI Agents.")

# Sidebar
with st.sidebar:
    st.header("Content Settings")

    # Make the text input take up more space
    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="Enter the topic"
    )

    # Add more sidebar controls if needed
    st.markdown("### LLM Settings")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

    # Add some spacing
    st.markdown("---")

    # Make the generate button more prominent in the side bar
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)

    # Add some helpful information
    with st.expander("How to use"):
        st.markdown("""
        1. Enter your desired content topic
        2. Play with the temperature
        3. Click 'Generate content' to start
        4. Wait for the AI to generate your article
        5. Download the result as a markdown file
        """)

def generate_content(topic):
    llm = LLM(model = "gpt-4o-mini")

    search_tool = SerperDevTool(n_results=5)

    # First Agent: Senior Research Analyst
    senior_research_analyst = Agent(
        role="Senior Research Analyst",
        goal=f"Research, analyze and synthesize the latest information about {topic} from reliable sources",
        backstory="You are a seasoned research analyst with a knack for finding and synthesizing information from various sources",
        allow_delegation=False,
        llm=llm, 
        tools=[search_tool],
        verbose=True
    )
    # Second Agent: Content Writer
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

    # Create the Crew
    crew = Crew(
        agents=[senior_research_analyst, content_writer],
        tasks=[research_task, write_blog_post],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})

    return result

# Main content area
if generate_button:
    with st.spinner('Generating content... This may take a moment'):
        try:
            result = generate_content(topic)
            st.markdown("### Generated Content")
            st.markdown(result)

            # Add download button
            st.download_button(
                label="Download Content",
                data=result.raw,
                file_name=f"{topic.lower().replace(' ', '_')}_atricle.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please try again or check your input")

# Add a footer
st.markdown("---")
st.markdown("Made with CrewAI, Streamlit and ChatGPT")


