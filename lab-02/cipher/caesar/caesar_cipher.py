from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypt_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            out_index = (letter_index + key) % alphabet_len
            out_letter = self.alphabet[out_index]
            encrypt_text.append(out_letter)
        return "".join(encrypt_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypt_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            out_index = (letter_index - key) % alphabet_len
            out_letter = self.alphabet[out_index]
            decrypt_text.append(out_letter)
        return "".join(decrypt_text)