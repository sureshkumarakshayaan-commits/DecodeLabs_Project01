# Rule-Based AI Chatbot

A simple command-line chatbot built in Python as Project 1 of the DecodeLabs AI Engineering Internship (2026). This project focuses on foundational control flow and logic — the building blocks behind any AI system, before introducing machine learning or generative models.

## What It Does

The chatbot runs in a continuous loop, accepting user input and responding based on predefined rules. It:

- Handles greetings and common conversational inputs
- Recognizes an exit command to end the session cleanly
- Sanitizes input (lowercasing and trimming whitespace) for consistent matching
- Falls back to a default response when it doesn't recognize the input

## How It Works

Instead of a long chain of `if-elif` statements (which becomes slow and hard to maintain as more rules are added), this project uses a Python dictionary to map inputs directly to responses:

```python
responses = {
    'hello': 'Hi there!',
    'bye': 'Goodbye!'
}

reply = responses.get(user_input, "I do not understand.")
```

This approach is faster and cleaner — dictionary lookups run in constant time, while an `if-elif` ladder gets slower as more rules are added.

## Tech Stack

- Python 3
- Core concepts: control flow, loops, dictionaries, string handling

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/sureshkumarakshayaan-commits/DecodeLabs_Project01.git
   ```
2. Navigate into the folder:
   ```
   cd DecodeLabs_Project01
   ```
3. Run the script:
   ```
   python3 chatbot.py
   ```
4. Type a message and press enter. Type the exit command to quit.

## What I Learned

This project taught me the fundamentals of building deterministic, traceable logic — an important foundation before working with probabilistic AI models like LLMs. It also introduced me to why rule-based systems are still used today, particularly in AI guardrails and safety-critical applications where predictable behavior matters.

## About

Built as part of the DecodeLabs AI Engineering Internship, Batch 2026.
