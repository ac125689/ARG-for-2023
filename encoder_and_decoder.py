import base64
import streamlit as st
import urllib.parse

#1-------------------------------------------morse_code---------------------------
def morse_code_decoder(code):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/',
        '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
        '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@',
        '...---...': 'SOS', '/': ' '
    }
    
    words = code.split(' / ')
    decoded_message = ''
    
    for word in words:
        letters = word.split()
        for letter in letters:
            decoded_message += morse_code_dict.get(letter, '?')
        # Only add a space if it's not the last letter in a word
        decoded_message += ' '
    
    return decoded_message.strip()
def morse_code_encoder(message):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
        '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        'SOS': '...---...', ' ' : '/'
    }

    encoded_message = ''
    for char in message:
        if char.upper() in morse_code_dict:
            encoded_message += morse_code_dict[char.upper()] + ' '
        else:
            encoded_message += ' '
    
    return encoded_message.strip()
#2-------------------------------------------base64-------------------------------
def base64_encode(message):
    encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")
    return encoded_message
def base64_decode(encoded_message):
    try:
        decoded_message = base64.b64decode(encoded_message).decode("utf-8")
        return decoded_message
    except Exception as e:
        st.error("Error decoding message. Please make sure the input is a valid Base64 encoded string.")
        return ""
#3-------------------------------------------Url----------------------------------
def url_encoder(message):
    encoded_message = urllib.parse.quote(message)
    return encoded_message
def url_decoder(encoded_message):
    decoded_message = urllib.parse.unquote(encoded_message)
    return decoded_message
#4-------------------------------------------Hex----------------------------------
def encode_to_hex(message):
    encoded_message = message.encode().hex()
    return encoded_message
def decode_from_hex(encoded_message):
    decoded_message = bytes.fromhex(encoded_message).decode()
    return decoded_message
#5-------------------------------------------Unicode------------------------------
def encode_Unicode(message):
    encoded_message = ""
    for char in message:
        encoded_message += str(ord(char)) + " "
    return encoded_message.strip()
def decode_Unicode(encoded_message):
    decoded_message = ""
    encoded_chars = encoded_message.split()
    for char in encoded_chars:
        try:
            decoded_message += chr(int(char))
        except ValueError:
            decoded_message += char
    return decoded_message
#6------------------------------------------Binary--------------------------------
def encode_binary(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message
def decode_binary(binary_message):
    decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return decoded_message


