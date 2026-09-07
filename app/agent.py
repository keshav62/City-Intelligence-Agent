from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.prebuilt import create_react_agent

from app.tools.weather import get_weather
from app.tools.news import get_city_news


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


tools = [
    get_weather,
    get_city_news
]


agent = create_agent(
    model=llm,
    tools=tools
)