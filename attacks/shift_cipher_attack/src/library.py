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
