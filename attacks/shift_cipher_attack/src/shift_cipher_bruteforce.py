# File encryption handled by Jahnvi Purohit 1902

def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    print("Encrypted text:", result)
    return result
text = input("Enter the text: ")
key = int(input("Enter the key (0-25): "))

result = encrypt(text, key)

# Now the decryption part handled by PRATEEK 1813

def decrypt(result, key):
    Result = ""

    for ch in result:
        if ch.isalpha():
            Result += chr((ord(ch.upper()) - 65 - key) % 26 + 65)
        else:
            Result += ch

    return Result

print("\nBrute Force Results:")

for key in range(26):
    plaintext = decrypt(result, key)
    print("Key", key, ":", plaintext)
