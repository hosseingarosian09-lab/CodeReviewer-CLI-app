# CodeReviewer-CLI-app

A simple CLI tool in Python that acts as your personal code reviewer, powered by Ollama’s `mistral:7b` model. Dubbed "Jarvis," it helps spot typos, rates code cleanliness, and fixes syntax errors—perfect for offline practice after my Python basics.

## Features
- Interactive code review via terminal input.
- Detects and fixes typos (e.g., misspelled variables).
- Rates cleanliness (1-10) based on readability and PEP 8.
- Corrects syntax errors for executable code.
- Streams real-time AI feedback.
- Runs locally with Ollama—no cloud needed.

## Prerequisites
- Python 3.8+ (check with `python --version`).
- Ollama installed from [ollama.com](https://ollama.com). Pull `mistral:7b`:
  ```sh
  ollama pull mistral:7b
  ```
- Start server: `ollama serve` before running.

Note about the Ollama app and server:
- If you use the Ollama desktop app, close the app before running this CLI to avoid port or process conflicts. Keep the desktop app closed unless you encounter HTTP 503 errors from the local Ollama server.
- Always run `ollama serve` in a separate terminal window (not inside the same session where you run the CLI) so the server stays active while you use this tool.

## Installation
1. Clone the repo:
   ```sh
   git clone https://github.com/hosseingarosian09-lab/CodeReviewer-CLI-app.git
   cd CodeReviewer-CLI-app
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the app:
   ```sh
   python main.py
   ```
2. Follow prompts:
   - Enter `yes` or `y` to review code.
   - Paste your Python code.
   - See output (typos, rating, fixes).

Example:
```
This is Jarvis. I will help you write better Python code.
Do you want to review some code? (yes/no): yes
Paste your Python code below:
print("Hello, world"
Processing...
Typos Fixed: No typos found.
Cleanliness Rating: 8/10 - Readable, but add a closing parenthesis for PEP 8.
Syntax Errors Fixed: Added closing parenthesis on line 1: print("Hello, world").
Goodbye!
```
Exit with `no`.

## Project Structure
```
CodeReviewer-CLI-app/
├── main.py          # Core script
├── README.md        # This file
└── requirements.txt # Dependencies
```

## About
By Hossein Garossian. Feedback welcome—next up, I’ll test it on my to-do code!