from shift_cipher import decrypt


def load_words(filename):

    file = open(filename, "r")

    words = file.read().split()

    file.close()

    return words


def dictionary_score(text, words):

    score = 0

    for word in text.split():

        word = word.lower()

        if word in words:
            score += 1

    return score


def dictionary_attack(ciphertext, words):

    best_key = 0
    best_score = 0
    best_text = ""

    for key in range(26):

        text = decrypt(ciphertext, key)

        score = dictionary_score(text, words)

        print("Key", key, "Score", score, ":", text)

        if score > best_score:

            best_score = score
            best_key = key
            best_text = text

    return best_key, best_text