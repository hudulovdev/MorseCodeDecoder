# Morse code dictionary (reverse mapping of Morse code to characters)
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
}

def decode_morse_code(morse_code):
    decoded_text = ""
    words = morse_code.split(' / ')
    for word in words:
        characters = word.split(' ')
        for char in characters:
            if char in morse_code_dict:
                decoded_text += morse_code_dict[char]
            else:
                decoded_text += '?'
        decoded_text += ' '

    return decoded_text.strip()

# Example usage
morse_code = input("Enter Morse code")
decoded_text = decode_morse_code(morse_code)
print("Decoded Text:", decoded_text)
