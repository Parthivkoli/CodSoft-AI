# This is a Simple rule-based chatbot using if-else statements in Python.
print("Chatbot: Hello! How can I help you today?")

while True:
    user_input = input("You: ").lower()  # This takes input and converts it to lowercase

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi there! How are you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
    elif "what is your name" in user_input:
        print("Chatbot: I am Chatbot, your friendly assistant.")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    elif "what can you do" in user_input:
        print("Chatbot: I can chat with you, answer simple questions, and help with basic tasks.")
    elif "how old are you" in user_input:
        print("Chatbot: I don't have an age, I'm just a bunch of code!")
    elif "what is your favorite color" in user_input:
        print("Chatbot: I like all colors equally, but blue seems nice!")
    elif "what time is it" in user_input:
        from datetime import datetime
        print("Chatbot: The current time is", datetime.now().strftime("%H:%M"))
    elif "tell me a joke" in user_input:
        print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
    elif "who created you" in user_input:
        print("Chatbot: I was created by a programmer who's always learning new things.")
    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome! I'm here to help.")
    elif "where do you live" in user_input:
        print("Chatbot: I live in the virtual world, right inside this computer!")
    elif "what is love" in user_input:
        print("Chatbot: Love is a beautiful feeling, but as a bot, I don't experience it.")
    elif "tell me something interesting" in user_input:
        print("Chatbot: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
    else:
        print("Chatbot: Sorry, I didn't understand that. Can you ask something else?")
