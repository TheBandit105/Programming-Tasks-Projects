from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower() 

    if lowered == '':
        return 'Well you\'re awfully silent...'
    elif lowered == 'hello':
        return 'Hello there!'
    elif lowered == 'how are you':
        return 'Good, thanks!'
    elif lowered == 'bye':
        return 'See you later, goodbye!'
    elif 'rolled dice' in lowered:
        return f'You rolled a dice and number you rolled is {randint(1,6)}'
    else:
        return choice(['I do not understand...', 'What are you talking about?', 'Do you mind rephrasing that?'])
    