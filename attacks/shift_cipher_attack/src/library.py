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

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 - key) % 26 + 65)
        else:
            result += ch

    return result
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
frequency = {
    'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3,
    'E': 12.7, 'F': 2.2, 'G': 2.0, 'H': 6.1,
    'I': 7.0, 'J': 0.2, 'K': 0.8, 'L': 4.0,
    'M': 2.4, 'N': 6.7, 'O': 7.5, 'P': 1.9,
    'Q': 0.1, 'R': 6.0, 'S': 6.3, 'T': 9.1,
    'U': 2.8, 'V': 1.0, 'W': 2.4, 'X': 0.2,
    'Y': 2.0, 'Z': 0.1
}

def chi_square(text):
    letters = ""

    for ch in text.upper():
        if ch.isalpha():
            letters += ch

    total = len(letters)

    if total == 0:
        return 999999

    result = 0

    for letter in frequency:
        observed = letters.count(letter)
        expected = frequency[letter] * total / 100
        result += (observed - expected) ** 2 / expected

    return result
def chi_square_attack(ciphertext):

    best_key = 0
    best_score = 999999
    best_text = ""

    for key in range(26):

        text = decrypt(ciphertext, key)

        score = chi_square(text)

        print("Key", key, "Score", round(score, 2))

        if score < best_score:

            best_score = score
            best_key = key
            best_text = text

    return best_key, best_text
