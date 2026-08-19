from shift_cipher_bruteforce import encrypt
from dictionary_scoring import load_words
from dictionary_scoring import dictionary_attack
from chi_square_attack import chi_square_attack


def main():

    print("SHIFT CIPHER CRYPTANALYSIS")
    print("--------------------------")

    text = input("Enter plaintext: ")

    key = int(input("Enter key: "))

    encrypted = encrypt(text, key)

    print("\nEncrypted text:", encrypted)

    print("\nDictionary Attack")
    print("-----------------")

    words = load_words("../dictionary/english_words.txt")

    dictionary_key, dictionary_text = dictionary_attack(
        encrypted,
        words
    )

    print("\nBest Dictionary Result:")
    print("Key:", dictionary_key)
    print("Text:", dictionary_text)

    print("\nChi-Square Attack")
    print("-----------------")

    chi_key, chi_text = chi_square_attack(encrypted)

    print("\nBest Chi-Square Result:")
    print("Key:", chi_key)
    print("Text:", chi_text)

    print("\nFinal Results")
    print("-------------")

    print("Actual Key:", key)
    print("Dictionary Key:", dictionary_key)
    print("Chi-Square Key:", chi_key)


if __name__ == "__main__":
    main()