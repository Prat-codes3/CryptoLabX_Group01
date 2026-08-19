#Now the decryption part handled by PRATEEK 1813
def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 - key) % 26 + 65)
        else:
            result += ch

    return result


ciphertext = "KHOOR"

for key in range(26):
    plaintext = decrypt(ciphertext, key)
    print("Key", key, ":", plaintext)
