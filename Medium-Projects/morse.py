# This program will translate any message to morse code

# Dictionary representing the morse code chart
MORSE_CODE_DICTIONARY = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def messageToMorse(message):
    messageToEncrypt = message.upper()
    encrypted = ''
    for item in messageToEncrypt:
        if item != ' ':
            encrypted += MORSE_CODE_DICTIONARY[item]
            encrypted += ' '
        else:
            encrypted += '/ '
    return encrypted

def centralize():
    print(f"\n\n\n")

print(f"------------- WELCOME TO MARCOS' MORSE CODE GENERATOR -------------")
print(f"Please, tell me the message that you wish to transform into morse code")

message = input('> ')
centralize()
print(messageToMorse(message))
print()