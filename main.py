from agent import run_agent

if __name__ == "__main__":
    print("=== Weather Travel AI Agent ===")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = run_agent(user_input)
        print("Agent:", response)
