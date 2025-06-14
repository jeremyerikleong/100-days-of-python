print("Welcome to the Caesar Cipher!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Text your text\n").lower()
shift = int(input("Type your shift number\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode" or encode_or_decode == "encode":
        result = ""
        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter not in alphabet:
                result += letter
            else:
                shifted_pos = alphabet.index(letter) + shift_amount
                shifted_pos %= len(alphabet)
                result += alphabet[shifted_pos]

        print(f"Here is the {encode_or_decode} text: {result}")
    else:
        print("Please choose a valid cipher_mode")

caesar(original_text=text, shift_amount=shift, encode_or_decode=cipher_mode)
