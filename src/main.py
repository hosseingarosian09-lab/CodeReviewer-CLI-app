import ollama   
from ollama import chat
import textwrap

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
    user_input = input("Do you want to review some code? (yes/no): ").strip().lower()
    if user_input not in ["yes", "y"]:
        break

    code = input("Paste your Python code below:\n")
    print("Processing...")

    stream = chat(
        model='phi3:mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": code},
        ],
        stream=True,
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

print("Goodbye!")
