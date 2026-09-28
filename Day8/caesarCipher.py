from cipher_art import logo

alphabet = [
                'a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z'
            ]

print(logo)

#def encrypt(original_text, shift_amount):
#    encrypted_text = ""
#    for letter in original_text:
#        shifted_position = alphabet.index(letter) + shift_amount
#        shifted_position %= len(alphabet)
#        encrypted_text += alphabet[shifted_position]
#    print(f"The encoded text is: {encrypted_text}")

#def decrypt(original_text, shift_amount):
#   decrypted_text = ""
#   for letter in original_text:
#        de_shifted_position = alphabet.index(letter) - shift_amount
#        de_shifted_position %= len(alphabet)
#        decrypted_text += alphabet[de_shifted_position]
#    print(f"The decrypted text is: {decrypted_text}")

def ceasar(original_text, shift_amount, encode_decode):                #"hello", 2, encode
    output_text = ""
    if encode_decode == "decode":                               
                    shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount    # = 7 + 2
            shifted_position %= len(alphabet)                           #to handle out of range error
            output_text += alphabet[shifted_position]                   # aplhabet[9] = j
    print(f"The {encode_decode}d text is: {output_text}")

restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("Invalid option.")
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(original_text = text, shift_amount = shift, encode_decode = direction)
    restart = input("Do you want to go again? Type 'yes' to continue. \n").lower()    
    
    