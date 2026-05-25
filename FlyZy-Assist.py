# chatbot.py

import random
import string

print("Travel Chatbot: Hello! Ask me anything about travel or hotel services.")
print("Type 'bye' to exit.\n")

# Memory dictionary
memory = {}

# Counter for clearing memory
question_count = 0

# Intent keywords
intents = {
    "checkin": ["check-in", "checkin", "enter", "arrival"],
    "checkout": ["check-out", "checkout", "leave", "departure"],
    "cab": ["cab", "taxi", "ride", "uber", "ola"],
    "flight": ["flight", "plane"],
    "booking": ["book", "reserve", "reservation"],
    "cancel": ["cancel", "refund"],
    "food": ["food", "restaurant", "eat", "meal"],
    "wifi": ["wifi", "internet"],
    "payment": ["payment", "pay", "card", "upi"],
    "location": ["location", "address", "reach", "map"]
}

# Responses
responses = {
    "checkin": [
        "Check-in starts from 12 PM.",
        "Most hotels allow check-in after 12 PM.",
        "You can usually check in around noon."
    ],

    "checkout": [
        "Check-out is usually before 11 AM.",
        "Most hotels request guests to check out by 11 AM."
    ],

    "cab": [
        "Yes, a cab is available right now!",
        "Sure, I can arrange a ride for you.",
        "A taxi has been booked for you."
    ],

    "flight": [
        "Please check your airline website for live flight updates.",
        "Your airline app will show real-time flight status."
    ],

    "booking": [
        "Room booking is available online.",
        "You can reserve rooms through hotel websites."
    ],

    "cancel": [
        "You can cancel your booking from the app or website.",
        "Refund depends on the cancellation policy."
    ],

    "food": [
        "Yes, food service is available.",
        "The hotel has a restaurant and room service."
    ],

    "wifi": [
        "Free WiFi is available for guests.",
        "Please ask reception for the WiFi password."
    ],

    "payment": [
        "We accept UPI, cards, and cash.",
        "Online payment options are available."
    ],

    "location": [
        "Our hotel location is available on Google Maps.",
        "Directions are available through map services."
    ]
}

while True:

    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice trip.")
        break

    # Remove punctuation
    cleaned_input = user_input.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    words = cleaned_input.split()

    question_count += 1

    # Clear memory after 5 questions
    if question_count > 5:
        memory.clear()
        question_count = 1

    # Follow-up memory handling
    if "when" in words and "arrive" in words:

        if memory.get("last_request") == "cab":
            print("Chatbot: Since you asked about a cab earlier, it will arrive in 10 minutes.")
            continue

        elif memory.get("last_request") == "flight":
            print("Chatbot: Your flight is expected to arrive on time.")
            continue

    found_intent = None

    # Intent matching
    for intent, keywords in intents.items():

        for word in words:

            if word in keywords:
                found_intent = intent
                break

        if found_intent:
            break

    # Responding and storing memory
    if found_intent:

        print("Chatbot:", random.choice(responses[found_intent]))

        # Store recent request
        memory["last_request"] = found_intent

    else:

        print("Chatbot: Sorry, I didn’t understand that.")
        print("Chatbot: You can ask about check-in, flight status, cab booking, WiFi, food, or hotel location.")