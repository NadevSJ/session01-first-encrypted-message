message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext: str = ""
for character in message:
    shifted: int = ord(character) + key
    ciphertext += chr(shifted)

print(ciphertext)