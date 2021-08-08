"""
NAME: Caesar.py
AUTHOR: Vladimir Ravinsky
EMAIL: Ducanto11@yandex.ru
VERSION: 1.2

this module provides encryption and decryption of strings
 """

_eng_alphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
_rus_alphabet = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)]

_alphabets = {'en': _eng_alphabet, 'rus': _rus_alphabet}


def _add_encrypted_char(string, original_char, step):
    if char.isupper():
        required_index = (alphabet.index(char) + step) % (alphabet_len // 2)  + (alphabet_len // 2)
        encoded_str += alphabet[required_index]
    else:
        required_index = (alphabet.index(char) + step) % (alphabet_len // 2)
        encoded_str += alphabet[required_index]



def encode(original_str, lang='en', step=1):
    '''Return the string with encoding chars according the chosen language. 
    Numbers and other signs do not change.'''
    encoded_str = ''
    alphabet = _alphabets[lang]
    alphabet_len = len(alphabet)

    for char in original_str:
        if char in alphabet:
            add_encrypted_char(original_str, char, step)
        else:
            encoded_str += char

    return encoded_str


def encode_all_lang(original_str, step=1):
    '''Return the string with encoding chars.
    Numbers and other signs do not change.'''
    encoded_str = ''

    for char in original_str:

        if not char.isalpha():
            encoded_str += char

        for alphabet in _alphabets.values():
            if char in alphabet:
                alphabet_len = len(alphabet)
                add_encrypted_char(original_str, char, step=step)

    return encoded_str


def encode_pro(original_str, lang='en'):
    '''Return the string with encoding chars according the chosen language. 
    Numbers and other signs do not change.
    The shift to encode the chars of each word is the length of the word.'''
    encoded_str = ''
    for word in original_str.split():
        encoded_str += encode(word, lang=lang, step=len(word)) + ' '

    return encoded_str


def encode_pro_all_lang(original_str):
    '''Return the string with encoding chars. 
    Numbers and other signs do not change.
    The shift to encode the chars of each word is the length of the word.'''
    encoded_str = ''
    for word in original_str.split():
        encoded_str += encode_all_lang(word, step=len(word)) + ' '

    return encoded_str


def decode(original_str, lang='en', step=1):
    '''Return the string with decoding chars according the chosen language. 
    Numbers and other signs do not change.'''
    return encode(original_str, lang=lang, step=-step)


def decode_all_lang(original_str, step=1):
    '''Return the string with decoding chars. 
    Numbers and other signs do not change.'''
    return encode_all_lang(original_str, step=-step)


def decode_pro(original_str, lang='en'):
    '''Return the string with decoding chars according the chosen language. 
    Numbers and other signs do not change.
    The shift to encode the chars of each word is the length of the word.'''
    encoded_str = ''
    for word in original_str.split():
        encoded_str += encode(word, step=-len(word)) + ' '

    return encoded_str


def decode_pro_all_lang(original_str):
    '''Return the string with decoding chars according the chosen language. 
    Numbers and other signs do not change.
    The shift to encode the chars of each word is the length of the word.'''
    encoded_str = ''
    for word in original_str.split():
        encoded_str += encode_all_lang(word, step=-len(word)) + ' '

    return encoded_str