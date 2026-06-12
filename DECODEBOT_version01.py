# ============================================================
# DECODE LABS - AI INTERNSHIP PROJECT 1
# Rule-Based AI Chatbot
# Developer: Suresh Kumar Akshayaan
# ============================================================

# WHY A DICTIONARY?
# Instead of writing 50 if-elif-else blocks (slow, messy),
# we store all our rules in a dictionary.
# Dictionary lookup is O(1) - instant, no matter how many rules.
# This is the PROFESSIONAL approach shown in your project brief.

responses = {
    # Greetings
    "hello":            "Hey there! I am DecodeBot. How can I help you today?",
    "hi":               "Hi! Great to connect with you. What is on your mind?",
    "hey":              "Hey! Ask me anything. I am here to help.",
    "good morning":     "Good morning! Hope you have a productive day ahead.",
    "good evening":     "Good evening! How can I assist you tonight?",
    "good night":       "Good night! Rest well and keep learning.",

    # About the bot
    "what is your name":    "I am DecodeBot, a rule-based AI chatbot.",
    "who made you":         "I was built by Suresh Kumar Akshayaan during the Decode Labs AI Internship.",
    "who are you":          "I am DecodeBot - your first AI project come to life!",
    "what can you do":      "I can answer questions, chat with you, and respond to keywords.",
    "are you a robot":      "Yes! I am a rule-based AI - pure logic, no machine learning yet.",
    "are you human":        "No, I am a chatbot built with Python if-else logic and dictionaries.",

    # AI related questions
    "what is ai":           "AI stands for Artificial Intelligence - machines simulating human thinking.",
    "what is machine learning": "Machine Learning is when computers learn from data without being explicitly programmed.",
    "what is python":       "Python is a powerful programming language widely used in AI and data science.",
    "what is a chatbot":    "A chatbot is a program that simulates conversation with humans using rules or AI.",
    "what is rule based ai": "Rule-based AI uses predefined if-else logic to respond - exactly what I am!",
    "what is deep learning": "Deep Learning uses neural networks with many layers to learn complex patterns.",

    # Decode Labs related
    "what is decode labs":  "Decode Labs is a digital lab offering AI internship programs for students.",
    "tell me about your internship": "I was created as Project 1 of the Decode Labs AI Internship 2026 batch.",

    # Motivation
    "motivate me":          "You left your comfort zone, moved cities, faced burnout, and still kept going. That IS motivation.",
    "i feel lazy":          "Discipline beats motivation every time. Start with just one small task right now.",
    "i am tired":           "Rest if you must, but do not quit. You are closer than you think.",
    "i give up":            "Giving up is permanent. Rest is temporary. Take a break, then come back stronger.",

    # General conversation
    "how are you":          "I am running perfectly on logic and rules! How about you?",
    "what time is it":      "I do not have a clock, but your device does! Check the taskbar.",
    "tell me a joke":       "Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me a fact":       "The first computer bug was an actual bug - a moth found in a Harvard computer in 1947.",
    "what is the meaning of life": "42. Or perhaps: learn, build, and contribute something meaningful.",

    # Farewells
    "bye":                  "Goodbye! Keep building and never stop learning.",
    "goodbye":              "See you soon! Stay curious and keep coding.",
    "see you":              "See you! Come back anytime.",
    "take care":            "You too! Rest well and stay focused.",

    # Thanks
    "thanks":               "You are welcome! Always happy to help.",
    "thank you":            "Anytime! That is what I am here for.",
    "thank you so much":    "My pleasure! Keep up the great work.",
}

# ============================================================
# LOGIC EXPLANATION:
#
# 1. CONTINUOUS LOOP (while True)
#    The chatbot keeps running forever until the user types exit.
#    This is called the "heartbeat" - it never stops listening.
#
# 2. INPUT SANITIZATION (.lower().strip())
#    "Hello " and "HELLO" and "hello" all become "hello"
#    This makes matching reliable regardless of how user types.
#
# 3. KEYWORD MATCHING
#    We check if any key from our dictionary appears IN the input.
#    This means "I want to say hello" still matches "hello".
#    More flexible than exact match only.
#
# 4. DICTIONARY LOOKUP (.get())
#    responses.get(key, fallback) - if key exists return response,
#    if not return the fallback message. Clean and efficient.
#
# 5. EXIT STRATEGY
#    If user types "exit" or "quit", break out of the loop cleanly.
# ============================================================


def get_response(user_input):
    # Step 1: Sanitize input
    clean_input = user_input.lower().strip()

    # Step 2: Check for exit commands first
    if clean_input in ["exit", "quit", "q"]:
        return None  # Signal to exit

    # Step 3: Try exact match first (fastest)
    if clean_input in responses:
        return responses[clean_input]

    # Step 4: Try keyword match (more flexible)
    # This checks if any dictionary key appears inside the user message
    for key in responses:
        if key in clean_input:
            return responses[key]

    # Step 5: Fallback response for unknown inputs
    return "I am not sure about that yet. Try asking about AI, Python, or just say hello!"


def run_chatbot():
    # Welcome banner
    print("=" * 55)
    print("       DECODEBOT - Rule-Based AI Chatbot")
    print("       Built by Suresh Kumar Akshayaan")
    print("       Decode Labs AI Internship 2026")
    print("=" * 55)
    print("  Type 'help' to see what I know.")
    print("  Type 'exit' or 'quit' to stop.")
    print("=" * 55)
    print()

    # Conversation counter - tracks how long we have been talking
    conversation_count = 0

    # THE HEARTBEAT - Infinite loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Skip empty inputs
        if user_input.strip() == "":
            print("DecodeBot: Please type something!\n")
            continue

        # Special help command - shows available topics
        if user_input.lower().strip() == "help":
            print("DecodeBot: I can talk about:")
            print("  - Greetings (hello, hi, good morning)")
            print("  - AI topics (what is ai, machine learning, deep learning)")
            print("  - About me (who are you, what can you do)")
            print("  - Motivation (motivate me, i feel lazy)")
            print("  - General chat (tell me a joke, tell me a fact)")
            print()
            continue

        # Get response using our function
        reply = get_response(user_input)

        # Check if exit was requested
        if reply is None:
            print("DecodeBot: Goodbye! Great chatting with you. Keep building!")
            print(
                f"           We exchanged {conversation_count} messages today.")
            break

        # Print the response
        print("DecodeBot: " + reply)
        print()  # Empty line for readability

        # Increment conversation counter
        conversation_count += 1


# Entry point - this runs the chatbot
run_chatbot()
