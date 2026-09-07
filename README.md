<div align="center">

# 🏙️ City Intelligence Agent

### *Your AI-powered city companion — real-time weather, live news, instant answers.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-EB6E4B?style=for-the-badge&logo=openweathermap&logoColor=white)](https://openweathermap.org/)
[![Tavily](https://img.shields.io/badge/Tavily-Search-6C63FF?style=for-the-badge)](https://tavily.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **Ask anything about any city in the world.**
> Get live weather forecasts, breaking news, and intelligent summaries — all in a single natural-language conversation.

<br/>

</div>

---

## ✨ What Is City Intelligence Agent?

**City Intelligence Agent** is a conversational AI assistant built with **LangChain** and powered by **Google Gemini**. It uses a multi-tool agent architecture to answer your questions about any city in the world — from current temperature and humidity to the latest breaking news — all through a simple, natural chat interface.

No dashboards. No forms. Just ask.

```
You: What is the weather like in Tokyo right now?

Agent:
  City: Tokyo
  Temperature: 28°C (Feels Like: 31°C)
  Humidity: 78%
  Weather: light rain
  Wind Speed: 4.2 m/s
```

```
You: What is happening in Mumbai today?

Agent:
  News 1 — Heavy monsoon rains disrupt local transport across the city...
  News 2 — Mumbai stock exchange hits record high amid FII inflows...
  News 3 — City announces major infrastructure expansion for 2027...
```

---

## 🧠 How It Works

The agent follows a **Reason → Act → Observe** loop powered by LangChain's agent executor:

```
User Input
    │
    ▼
┌─────────────────────────────────┐
│         Google Gemini LLM       │  ◄── Thinks, plans, decides
│    (Reasoning & Orchestration)  │
└────────────┬────────────────────┘
             │ Selects Tool
    ┌────────┴────────┐
    ▼                 ▼
┌─────────┐     ┌──────────┐
│ Weather │     │  News    │
│  Tool   │     │  Tool    │
│(OpenWX) │     │ (Tavily) │
└────┬────┘     └────┬─────┘
     └───────┬───────┘
             ▼
     Structured Response
             │
             ▼
      Final Answer to User
```

1. **User sends a natural-language query**
2. **Gemini AI reasons** about what information is needed
3. **Tools are called** automatically — weather API, news search, or both
4. **Results are synthesized** into a clean, readable response
5. **Conversation continues** — the agent remembers context

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🤖 **AI Model** | Google Gemini (`gemini-flash`) | Core reasoning & language understanding |
| 🔗 **Agent Framework** | LangChain | Tool orchestration & agent loop |
| 🌦️ **Weather Data** | OpenWeatherMap API | Real-time weather conditions |
| 📰 **News Search** | Tavily Search API | Live news & web intelligence |
| 🐍 **Runtime** | Python 3.10+ | Core application language |
| ⚙️ **Config** | python-dotenv | Secure API key management |

---

## 📁 Project Structure

```
City Intelligence Agent/
│
├── app/
│   ├── main.py                  # Entry point — CLI chat loop
│   ├── agent.py                 # LangChain agent initialization
│   │
│   ├── tools/
│   │   ├── weather.py           # 🌦️ OpenWeatherMap tool
│   │   └── news.py              # 📰 Tavily news search tool
│   │
│   ├── config/
│   │   └── settings.py          # App configuration & constants
│   │
│   └── prompts/
│       └── system_prompt.py     # Agent personality & instructions
│
├── .env                         # 🔐 API keys (never commit this!)
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
└── README.md                    # You are here
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/city-intelligence-agent.git
cd city-intelligence-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
OPENWEATHER_API_KEY=your_openweathermap_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

### 5. Run the Agent

```bash
python -m app.main
```

You will see:

```
==================================================
🏙️ CITY INTELLIGENCE AGENT
==================================================

Type 'exit' to quit.

You:
```

Start chatting!

---

## 🔑 Getting API Keys

| Service | Free Tier | Get Key |
|---------|-----------|---------|
| **Google Gemini** | ✅ Yes — generous free quota | [aistudio.google.com](https://aistudio.google.com/app/apikey) |
| **OpenWeatherMap** | ✅ Yes — 60 calls/min free | [openweathermap.org/api](https://openweathermap.org/api) |
| **Tavily** | ✅ Yes — 1,000 free searches/month | [tavily.com](https://tavily.com/) |

---

## 💬 Example Conversations

```
You: What is the weather in London?

Agent: Here is the current weather in London:
  🌡️ Temperature: 15°C (Feels Like: 13°C)
  💧 Humidity: 82%
  🌤️ Conditions: Overcast clouds
  💨 Wind Speed: 5.1 m/s
```

```
You: Any big news in New York today?

Agent: Here are the latest developments from New York:
  📰 News 1 — City Council passes landmark housing bill...
  📰 News 2 — Transit authority announces subway expansion...
  📰 News 3 — Wall Street ends session at record highs...
```

```
You: Is it a good day to visit Paris?

Agent: Based on current conditions in Paris:
  🌦️ Weather: Light drizzle, 18°C — bring an umbrella!
  📰 Latest: The Louvre is hosting a special exhibition this week.

  Overall, it is a decent day to visit — the rain is light
  and the city is buzzing with cultural events!
```

---

## 📦 Dependencies

```txt
langchain                # Agent framework
langchain-google-genai   # Google Gemini integration
langchain-community      # Community tool integrations
langchain-tavily         # Tavily search integration
requests                 # HTTP requests (weather API)
python-dotenv            # Environment variable management
tavily-python            # Tavily client SDK
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔒 Security & Best Practices

- ✅ All API keys stored in `.env` — never hardcoded
- ✅ `.env` excluded from version control via `.gitignore`
- ✅ Request timeouts enforced on all API calls
- ✅ Graceful error handling for all external service failures
- ✅ No sensitive data logged or printed to console

---

## 🗺️ Roadmap

- [ ] 🌐 Web UI with FastAPI + streaming responses
- [ ] 📍 GPS-based auto city detection
- [ ] 🌐 Multi-language support
- [ ] 🗓️ Weather forecasts (5-day / 7-day)
- [ ] 📊 City statistics — population, air quality, traffic
- [ ] 💾 Conversation history & memory persistence
- [ ] 🐳 Docker containerization

---

## 🤝 Contributing

Contributions are welcome! Here is how to get started:

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a **Pull Request**

Please make sure your code follows the existing style and includes appropriate error handling.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Built with ❤️ as part of a **Generative AI learning journey**.

> *"The city has always been the place where information flows fastest.*
> *Now, intelligence flows with it."*

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[![GitHub stars](https://img.shields.io/github/stars/your-username/city-intelligence-agent?style=social)](https://github.com/your-username/city-intelligence-agent)

</div>
