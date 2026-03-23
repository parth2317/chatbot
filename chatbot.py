import random

def chatbot_response(user_input):
    responses = {
        "hi": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thanks!", "Doing well, how about you?"],
        "bye": ["Goodbye!", "See you later!"]
    }
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")