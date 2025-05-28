class PlayfairCipher:
    def __init__(self):
        pass

    def pass__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong key
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key) + remaining_letters
        for i in range(len(matrix) - 25):
            matrix.pop()
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError("Character not found in matrix")

    def playfair_encrypt(self, plain_text, key):
        plain_text = plain_text.replace("J", "I")
        encrypted_text = ""
        playfair_matrix = self.create_playfair_matrix(key)
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
            row1, col1 = self.find_letter_coords(playfair_matrix, pair[0])
            row2, col2 = self.find_letter_coords(playfair_matrix, pair[1])
            if row1 == row2:
                encrypted_text += playfair_matrix[row1][(col1 + 1) % 5]
                encrypted_text += playfair_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += playfair_matrix[(row1 + 1) % 5][col1]
                encrypted_text += playfair_matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += playfair_matrix[row1][col2]
                encrypted_text += playfair_matrix[row2][col1]
        return encrypted_text.upper()

    def playfair_decrypt(self, cipher_text, key):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        playfair_matrix = self.create_playfair_matrix(key)
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(playfair_matrix, pair[0])
            row2, col2 = self.find_letter_coords(playfair_matrix, pair[1])
            if row1 == row2:
                decrypted_text += playfair_matrix[row1][(col1 - 1) % 5]
                decrypted_text += playfair_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += playfair_matrix[(row1 - 1) % 5][col1]
                decrypted_text += playfair_matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += playfair_matrix[row1][col2]
                decrypted_text += playfair_matrix[row2][col1]
        # Loại bỏ ký tự "X" nếu không phải là ký tự cuối cùng và không phải là ký tự đầu tiên
        banro = ""
        for i in range(0, len(decrypted_text), 2):
            if decrypted_text[i] == "X":
                banro += decrypted_text[i+1]
            else:
                banro += decrypted_text[i] + decrypted_text[i+1]
            if decrypted_text[i] == "X":
                banro += decrypted_text[i+1]
            else:
                banro += decrypted_text[i] + decrypted_text[i+1]
        return banro