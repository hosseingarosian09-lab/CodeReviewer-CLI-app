import ollama
from ollama import chat
import textwrap
import sys

system_prompt = textwrap.dedent("""
You are an expert Python code reviewer. I will provide you with Python code, and your task is to:
Fix Typos: Identify and correct any typographical errors in the code (e.g., misspelled keywords, variable names, or incorrect punctuation).
Rate Code Cleanliness: Evaluate the code's cleanliness on a scale of 1 to 10 (1 = very messy, 10 = extremely clean). Consider factors like readability, consistent indentation, clear variable names, proper commenting, and adherence to PEP 8 style guidelines. Provide a brief explanation for your rating.
Fix Syntax Errors: Identify and correct any syntax errors in the code to make it executable. If the code is syntactically correct, state so.
Output Format: Return the results in the following format:

- Typos Fixed: List any typos found and the corrections made. If none, state "No typos found."
- Cleanliness Rating: Provide the cleanliness score (1-10) with a brief explanation.
- Syntax Errors Fixed: List any syntax errors found and the corrections made. If none, state "No syntax errors found."
""")


print("This is Jarvis. I will help you write better Python code.")

while True:
    try:
        user_input = input("\nDo you want to review some code? (yes/no): ").strip().lower()
        if user_input in ["no", "n", "q", "quit", "exit"]:
            print("Goodbye!")
            break
        if user_input not in ["yes", "y"]:
            print("Please type 'yes' or 'no'.")
            continue

        code = input("Paste your Python code below:\n")
        if not code.strip():
            print("No code provided. Please paste some Python code.")
            continue

        print("Processing...")
        stream = chat(
            model='mistral:7b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": code},
            ],
            stream=True,
        )

        print("\nReview:\n" + "-"*50)
        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)
        print("\n" + "-"*50)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
        sys.exit(0)
    except ollama.ResponseError as e:
        print(f"\nError communicating with Ollama: {e}")
        print("Make sure Ollama is running and the model 'mistral:7b' is pulled.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print() 
