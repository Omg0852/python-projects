
# a dictionary containing the symbols and Their morse code
# added an extra morse code for white spaces/space : '.-.--.--' though it's my own
morse_code = {
    'A': '.-',    '1': '.----',   ', ': '--..--',
    'B': '-...',  '2': '..---',    '.': '.-.-.-',
    'C': '-.-.',  '3': '...--',    '?': '..--..',
    'D': '-..',   '4': '....-',    '/': '-..-.',
    'E': '.',     '5': '.....',    '-': '-....-',
    'F': '..-.',  '6': '-....',    '(': '-.--.',
    'G': '--.',   '7': '--...',    ')': '-.--.-',
    'H': '....',  '8': '---..',
    'I': '..',    '9': '----.',
    'J': '.---',  '0': '-----',
    'K': '-.-',   ' ': '.-.--.--',
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

}

# the dictionary which will map the morse code to the Symbol
# it's just a dictionary with key=morse_code and value = symbols

reverse_morse_code_dict = {value: key for key, value in morse_code.items()}


# function to convert the simple text message into the morse code
def encoding_function(string1):
    coded_string = ' '.join(morse_code.get(char) for char in string1)
    return coded_string


# function to convert the morse code into simple text message

def decode_function(morse_coded_message):
    words = morse_coded_message.split(' ')
    decoded_string = ''.join(reverse_morse_code_dict.get(code, '') for code in words)
    return decoded_string


# main block
# carry would make the program running according to user's wish
carry = True

while carry:
    operation = int(input("What Kind Of Operation Do You Want To Perform \n1. Encoding The Message\n2.Decoding The Message\n"))
    string = input("\nPlese Enter the String To get Morse Equivalent : ").upper()

    # handling symbols that are not in the morse code dictionary
    if operation == 1:
        print(f"\nThe MORSE CODED STRING : '{encoding_function(string)}'")
    elif operation == 2:
        print(f"\nThe DECODED MESSAGE IS : '{decode_function(string)}'")
    carry = bool(int((input('\nDo You Want To Continue : 0->End/1->Continue \n'))))




