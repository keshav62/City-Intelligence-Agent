from langchain.agents import create_agent

from langchain_google_genai import ChatGoogleGenerativeAI

from app.tools.weather import get_weather
from app.tools.news import get_city_news

from app.prompts.system_prompt import SYSTEM_PROMPT


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


tools = [
    get_weather,
    get_city_news
]


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)