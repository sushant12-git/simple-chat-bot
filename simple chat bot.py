import datetime
import random

print("🤖 ChatBot: Hello! I'm your assistant. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm just a program, but thanks for asking!")
    elif "your name" in user_input:
        print("Bot: I’m PyBot, your simple assistant.")
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M")
        print(f"Bot: Current time is {now}")
    elif "date" in user_input:
        today = datetime.date.today()
        print(f"Bot: Today's date is {today}")
    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the computer go to the doctor? Because it had a virus!"
        ]
        print("Bot:", random.choice(jokes))
    elif "weather" in user_input:
        print("Bot: I can't check real weather, but it's always sunny in Python land! 🌞")
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Talk to you later. 👋")
        break
    else:
        print("Bot: Sorry, I didn’t understand that. Can you rephrase?")
