from crewai import Task

def create_tasks(researcher, summarizer):
    t1 = Task(
        description="Search online news and extract latest 5 headlines using the Firecrawl tool",
        expected_output="Raw scraped content from trending news websites",
        agent=researcher,
        tools_used=[ "firecrawl_search" ]  
    )

    t2 = Task(
        description="Summarize the headlines into short bullet points",
        expected_output="5 bullet point summary of current news",
        agent=summarizer
    )

    return [t1, t2]
