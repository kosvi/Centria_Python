# Source: https://fi.wikipedia.org/wiki/S%C3%A4hk%C3%B6tys

data = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    'Å': '.--.-',
    'Ä': '.-.-',
    'Ö': '---.',
    '!':  '..--.',
    '?':  '..--..',
    '/':  '-..-.',
    '=':  '-...-',
    ':':  '---...',
    ',':  '--..--',
    '.':  '.-.-.-',
    '-':  '-....-',
    '(':  '-.--.',
    ')':  '-.--.-',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def text_to_morse(text):
    code = ''
    for letter in text.upper():
        if letter == ' ':
            code += ' / '
        else:
            code += data.get(letter, '') + ' '
    return code


def morse_to_text(morse):
    data2 = {}
    for key in data.keys():
        data2.update({data.get(key): key})
    text = ''
    for code in morse.split(' '):
        text += data2.get(code, ' ')
    return text
