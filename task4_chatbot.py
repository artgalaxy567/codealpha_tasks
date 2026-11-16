def get_reply(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("Chatbot ready. Say hello, how are you, or bye.")
    while True:
        user = input("You: ")
        reply = get_reply(user)
        print("Bot:", reply)
        if user.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()