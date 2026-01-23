def get_bot_response(message):
    message = message.lower()

    if "balance" in message:
        return "Your current balance is SGD 10,000."
    elif "loan" in message:
        return "You are eligible for a personal loan up to SGD 50,000."
    elif "help" in message:
        return "I can help you with balance, loans, and account queries."
    else:
        return "Sorry, I didn't understand that. Please try again."
