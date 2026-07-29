import analysis.analyze as analyze

def main():
    while True:
       
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")
    

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEncrypt: Coming Soon")

        elif choice == "2":
            print("\nDecrypt: Coming Soon")

        elif choice == "3":
            print("\nAttack: Coming Soon")

        elif choice == "4":
            filename = input("Enter the file name: ")
            analyze.analyze_text_file(filename)

        elif choice == "5":
            print("\nExiting CryptoLabX. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()