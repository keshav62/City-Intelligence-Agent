from langchain_core.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()


@tool
def get_city_news(city: str):
    """
    Get the latest news and current events about a city.
    """

    tavily = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    query = f"Latest news and current events in {city}"

    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    results = []

    for item in response["results"]:

        results.append({
            "title": item["title"],
            "content": item["content"],
            "url": item["url"]
        })

    return results