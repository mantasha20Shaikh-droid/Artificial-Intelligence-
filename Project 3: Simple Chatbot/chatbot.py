# Simple Chatbot
# A small rule-based chatbot

print("Simple Chatbot")
print("Type 'bye' to stop the chatbot.")

while True:
    message = input("You: ").lower().strip()

    if message == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    elif "hello" in message or "hi" in message:
        print("Bot: Hello! How are you?")

    elif "how are you" in message:
        print("Bot: I am fine. Thank you for asking.")

    elif "your name" in message:
        print("Bot: My name is Simple Chatbot.")

    elif "what can you do" in message:
        print("Bot: I can answer simple questions and greetings.")

    elif "thank" in message:
        print("Bot: You're welcome!")

    else:
        print("Bot: Sorry, I don't understand that question.")
      
