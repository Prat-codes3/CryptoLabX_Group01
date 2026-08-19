from shift_cipher import decrypt


def load_words(filename):
    file = open(filename, "r")
    words = file.read().split()
    file.close()

    return words


def score(text, words):
    count = 0

    for word in text.split():
        word = word.lower()

        if word in words:
            count += 1

    return count


def dictionary_attack(ciphertext, words):
    best_key = 0
    best_score = 0
    best_text = ""

    for key in range(26):
        text = decrypt(ciphertext, key)

        current_score = score(text, words)

        print(key, text, current_score)

        if current_score > best_score:
            best_score = current_score
            best_key = key
            best_text = text

    return best_key, best_text


# Load the dictionary
words = load_words("english.txt")

# Test ciphertext
ciphertext = "khoor zruog"

# Run dictionary attack
best_key, best_text = dictionary_attack(ciphertext, words)

print("\nBest key:", best_key)
print("Decrypted text:", best_text)
