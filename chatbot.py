import random

# Simple rule-based chatbot

# 1) Define triggers (words/phrases that indicate an intent)
TRIGGERS = {
    "greeting": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
    "how_are_you": ["how are you", "how are u", "how r you", "how's it going", "how are things"],
    "thanks": ["thanks", "thank you", "thx"],
    "goodbye": ["bye", "goodbye", "see you", "quit", "exit"]
}

# 2) Predefined replies for each intent
RESPONSES = {
    "greeting": ["Hi!", "Hello!", "Hey there!"],
    "how_are_you": ["I'm fine, thanks! How about you?", "Doing well — thanks for asking!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye — have a nice day!"],
    "fallback": ["Sorry, I didn't understand that.", "Hmm, I don't know how to reply to that yet."]
}

def find_intent(user_input: str) -> str:
    """
    Very simple intent detection:
    - looks for trigger substrings in the normalized input
    - returns the first matching intent, or 'fallback' if none match
    """
    text = user_input.lower().strip()
    # check each intent's triggers
    for intent, triggers in TRIGGERS.items():
        for trig in triggers:
            if trig in text:
                return intent
    return "fallback"

def chatbot():
    print("Chatbot: Hello! (type 'bye' or 'exit' to stop)")
    while True:
        user = input("You: ").strip()
        if not user:
            # ignore empty input
            print("Chatbot: Please type something.")
            continue

        intent = find_intent(user)
        reply = random.choice(RESPONSES.get(intent, RESPONSES["fallback"]))
        print("Chatbot:", reply)

        # stop if user said goodbye
        if intent == "goodbye":
            break

if __name__ == "__main__":
    chatbot()
