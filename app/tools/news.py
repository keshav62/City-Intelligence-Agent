import os

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool

load_dotenv()


@tool
def get_city_news(city: str) -> str:
    """
    Get the latest news and recent events about a city.

    Use this tool when the user asks about:
    latest news, current events, recent developments,
    or what is happening in a city.
    """

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return "Error: TAVILY_API_KEY is missing."

    try:

        tavily = TavilyClient(api_key=api_key)

        query = f"""
        Latest news and current events about {city}.
        Focus specifically on recent developments in the city.
        """

        response = tavily.search(
            query=query,
            search_depth="basic",
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return f"No recent news found for {city}."

        news = []

        for i, item in enumerate(results, start=1):

            news.append(
                f"""
                  News {i}
                  Title: {item.get("title")}
                  Content: {item.get("content")}
                  Source: {item.get("url")}
                """
            )

        return "\n".join(news)

    except Exception as e:
        return f"Unable to get news: {str(e)}"