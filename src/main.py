import ollama
from ollama import chat

# Define the system prompt for the model
system_prompt = """You are an expert Python code reviewer. I will provide you with Python code, and your task is to:
Fix Typos: Identify and correct any typographical errors in the code (e.g., misspelled keywords, variable names, or incorrect punctuation).
Rate Code Cleanliness: Evaluate the code's cleanliness on a scale of 1 to 10 (1 = very messy, 10 = extremely clean). Consider factors like readability, consistent indentation, clear variable names, proper commenting, and adherence to PEP 8 style guidelines. Provide a brief explanation for your rating.
Fix Syntax Errors: Identify and correct any syntax errors in the code to make it executable. If the code is syntactically correct, state so.
Output Format: Return the results in the following format:

- Typos Fixed: List any typos found and the corrections made. If none, state "No typos found."
- Cleanliness Rating: Provide the cleanliness score (1-10) with a brief explanation.
- Syntax Errors Fixed: List any syntax errors found and the corrections made. If none, state "No syntax errors found."
"""
