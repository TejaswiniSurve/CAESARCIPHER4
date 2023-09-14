
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position+shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"\tHEYYY!! Here's the text after encryption: {cipher_text}\n")

def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position-shift_key)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"\tHEYYY!! Here's the text after decryption:{plain_text}\n")

want_to_end = False
while not want_to_end:
    what_to_do = input("\tType 'encrypt' for encryption, type 'decrypt' for decryption:  \n")
    message = input("\tType your message: \n").lower()
    shift = int(input("\tenter the shift number: \n"))

    if what_to_do=="encrypt":
        encryption(plain_text= message,shift_key=shift)

    elif what_to_do=="decrypt":
        decryption(cipher_text=message,shift_key=shift)

    play_again = input("Type 'yes' to play again, else 'no' to quit: \n")
    if play_again=="no":
        want_to_end=True
        print("HAVE A NICE DAY BYEE!!")


