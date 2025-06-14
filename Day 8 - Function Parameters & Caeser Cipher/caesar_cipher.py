print("Welcome to the Caesar Cipher!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Text your text\n").lower()
shift = int(input("Type your shift number\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_pos = alphabet.index(letter) + shift_amount

        shifted_pos %= len(alphabet)
        cipher_text += alphabet[shifted_pos]

    print(f"Here is the encoded result: {cipher_text}")


def decrypt(shifted_text, unshift_amount):
    original_text = ""
    for letter in shifted_text:
        unshifted_pos = alphabet.index(letter) - unshift_amount

        unshifted_pos %= len(alphabet)
        original_text += alphabet[unshifted_pos]

    print(f"Here is the encoded result: {original_text}")



# encrypt(original_text = text, shift_amount = shift)
decrypt(shifted_text = text, unshift_amount = shift)
