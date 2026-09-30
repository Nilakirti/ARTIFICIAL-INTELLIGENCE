import random
intents = {
    'greeting': ['Hello!', 'Hi!', 'Hey!'],
    'goodbye': ['See you later!', 'Bye!', 'Goodbye!'],
    'thanks': ['You\'re welcome!', 'No problem!', 'Anytime!']
}
def match_intent(message):
    message = message.lower()
    if 'hello' in message or 'hi' in message:
        return 'greeting'
    elif 'bye' in message or 'goodbye' in message:
        return 'goodbye'
    elif 'thank' in message:
        return 'thanks'
    else:
        return None
def respond(message):
    intent = match_intent(message)
    if intent:
        return random.choice(intents[intent])
    else:
        return 'I didn\'t understand that.'
def chatbot():
    print('Welcome to the chatbot!')
    while True:
        message = input('User: ')
        response = respond(message)
        print('Chatbot:', response)
        if match_intent(message) == 'goodbye':
            break
chatbot()