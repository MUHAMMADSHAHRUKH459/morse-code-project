#  Morse code translator

# step 1: Dictionary for Morse code
english_to_morse = {

   # string
   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

   # Number
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

   # Special Characters
    ',': '--..--',      # Comma
    '.': '.-.-.-',      # Period
    "'": '.----.',      # Apostrophe
    ';': '-.-.-.',      # Semicolon
    ':': '---...',      # Colon
    '?': '..--..',      # Question Mark
    '-': '-....-',      # Hyphen/Minus
    '/': '-..-.',       # Slash
    '(': '-.--.',       # Left Parenthesis
    ')': '-.--.-',      # Right Parenthesis
    '&': '.-...',       # Ampersand
    '"': '.-..-.',      # Double Quotation Mark
    '=': '-...-',       # Equal Sign
    '@': '.--.-',       # At Sign
    '!': '-.-.--',      # Exclamation Mark
    '+': '.-.-.',       # Plus Sign
    '_': '..--.-',      # Underscore
    '"': '.-..-.',      # Quotation Mark
    '$': '...-..-',     # Dollar Sign
    '(': '-.--.',       # Left Parenthesis
    ')': '-.--.-',      # Right Parenthesis
    '&': '.-...',       # Ampersand
    '/': '-..-.',       # Slash
    '=': '-...-',       # Equal Sign
    '?': '..--..',      # Question Mark
    '!': '-.-.--',      # Exclamation Mark
    '@': '.--.-'        # At Sign 
}

# step 2: get user input
print("Welcome to the Morse Code Translator!")
user_string = input("Enter a Random English Text: ")

# step 3: write a function to translate the text base to user choice
def translate(text):
   # step 3.1: convert the text to uppercase
   text = text.upper()
   # step 3.2: initialize an empty string
   morse_string = ""
   # step 3.3: loop through each character in the text
   

   for char in text:
       # step 3.4: check if the character is in the dictionary
      try:
         if char == " ":
            morse_string += "  " # add a space between words 
         else:
           morse_string += english_to_morse[char] + " "
      except KeyError:
         # step 3.4.1: if the character is not in the dictionary, print an error message
         print("Sorry, I can't translate this character: " + char)
         morse_string += char + " " # add the character to the string "" 


   # step 3.5: return the translated text
   return morse_string

# step 4: print the translated text
print(translate(user_string))