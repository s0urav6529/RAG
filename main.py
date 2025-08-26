from src.core.pipeline import QuestionAnsweringPipeline
from src.pydantic_models.rag_model import State

def main():
    # Initialize the pipeline with the State model
    pipeline = QuestionAnsweringPipeline(State)

    print("🤖 Ask me anything! Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            input_message = input("❓ Your question: ").strip()
            if input_message.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            # Stream and print responses
            for response in pipeline.stream_responses(input_message):
                print(response, end="")
            print()  # For newline after the response

        except KeyboardInterrupt:
            print("\n👋 Exiting. Have a great day!")
            break
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    main()
