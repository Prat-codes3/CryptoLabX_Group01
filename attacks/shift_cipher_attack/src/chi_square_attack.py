from library import decrypt


frequency = {
    'A': 8.2,
    'B': 1.5,
    'C': 2.8,
    'D': 4.3,
    'E': 12.7,
    'F': 2.2,
    'G': 2.0,
    'H': 6.1,
    'I': 7.0,
    'J': 0.2,
    'K': 0.8,
    'L': 4.0,
    'M': 2.4,
    'N': 6.7,
    'O': 7.5,
    'P': 1.9,
    'Q': 0.1,
    'R': 6.0,
    'S': 6.3,
    'T': 9.1,
    'U': 2.8,
    'V': 1.0,
    'W': 2.4,
    'X': 0.2,
    'Y': 2.0,
    'Z': 0.1
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
