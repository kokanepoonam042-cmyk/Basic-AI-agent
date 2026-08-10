import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_agent(user_input):
    """Send a user's request to the AI model and return the response."""

    response = client.responses.create(
        model="gpt-5-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI Agent for a college project. "
                    "Give clear, simple, and useful answers."
                ),
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )

    return response.output_text


def main():
    print("================================")
    print("      Basic AI Agent")
    print("================================")
    print("Type 'exit' to stop the agent.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        try:
            answer = run_agent(user_input)
            print(f"Agent: {answer}\n")
        except Exception as error:
            print(f"Error: {error}\n")


if __name__ == "__main__":
    main()