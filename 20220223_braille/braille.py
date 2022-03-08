# Braille dictionlary
# https://stackoverflow.com/a/63595350/11755155

# Braille Capitalization mark
# https://brailleworks.com/reading-and-writing-braille/#:~:text=Braille%20Capitalization,in%20front%20of%20the%20word.

# Check if a string is uppercase
# str.isupper('A') # True
# str.isupper('a') # False

# Lower a uppercase letter
# 'A'.lower() # a

def solution(s):
    code_table = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    ' ': '000000',
    '#': '000001'
    }
    braille_dots = ''
    for letter in s:
        if str.isupper(letter):
            braille_dots += code_table['#']
            braille_dots += code_table[letter.lower()]
        else:
            braille_dots += code_table[letter]
    return braille_dots
