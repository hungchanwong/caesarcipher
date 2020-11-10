alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text, key):
    encrypted_text = ""
    key = key % 25
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + key
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    print(f"The encrypted message is {encrypted_text}")
   
def decrypt(text, key):
    decrypted_text = ""
    key = key % 25
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - key
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    print(f"The decrypted message is {decrypted_text}")

print("Welcome to Caesar Cipher")
rule = input("Type 'encode' to Encode, type 'decode' to Decode: \n").lower()
if rule == "encode":
    plaintxt = input("Type your text: \n").lower()
    key = int(input("Key number: \n"))
    encrypt(plaintxt, key)
elif rule == "decode":
    plaintxt = input("Type your text: \n").lower()
    key = int(input("Key number: \n"))
    decrypt(plaintxt, key)
# else:
#     print("Please try again. \nQuitting...")



    
