import random

# Define responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great, thanks for asking!", "I'm doing fine."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "I'm not sure what you mean."]
}

# Function to generate response
def get_response(message):
    # Convert message to lowercase for case-insensitive matching
    message = message.lower()
    
    # Check if message is in responses dictionary
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

# Main loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit if user types 'exit'
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    
    # Get response
    bot_response = get_response(user_input)
    
    # Print bot's response
    print("Bot:", bot_response)