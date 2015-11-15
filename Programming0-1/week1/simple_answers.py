text = input('Enter your text: ')
if 'hello' in text or 'Hello' in text:
    print('Hello there, good stranger!')
elif 'how are you' in text:
    print('I\'m fine, thanks. How are you?')
    input('your answer: ')
elif 'feelings' in text:
    print('I am a machine. I have no feelings')
elif 'age' in text:
    print('I have no age. Only current timestamp')
else:
    print('I have no answer')
