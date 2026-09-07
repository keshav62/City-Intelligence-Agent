from app.agent import agent


def run_agent():

    print("=" * 50)
    print("🏙️ CITY INTELLIGENCE AGENT")
    print("=" * 50)

    print("\nType 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nGoodbye! 👋")
            break

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )

        final_message = result["messages"][-1]

        # Extract clean text from the response
        if isinstance(final_message.content, list):
            output = "\n".join(
                item["text"]
                for item in final_message.content
                if isinstance(item, dict) and item.get("type") == "text"
            )
        else:
            output = final_message.content

        print("\nAgent:")
        print(output)

        print("\n" + "-" * 50)


if __name__ == "__main__":
    run_agent()