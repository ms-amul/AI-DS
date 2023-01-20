
string = "aRTificial INTELLIgence"

while(True):
    print("1. convert the input string into upper case.")

    print("2. convert the input string into lower case.")

    print("3. Check whether all the character of the input string are in upper case.")

    print("4. Check whether all the character of the input string are in lower case.")

    print("5. Replace the string 'INTELLIgence' by 'Neural Network'.")

    print("6. Check whether the given string starts with 'T'.")

    print("7. Check whether the given string ends with 'e'.")

    print("8. Convert the first letter of the input string into capital letter.")

    print("9. Convert the lower-case characters to upper case and vice versa.")

    print("10. Exit")

    print("-" * 20)

    letter = input("Enter a letter corresponding to a string operation (1-10): ")
    result = None
    if letter == "1":
        result = string.upper()
    elif letter == "2":
        result = string.lower()
    elif letter == "3":
        result = string.isupper()
    elif letter == "4":
        result = string.islower()
    elif letter == "5":
        result = string.replace("INTELLIgence", "Neural Network")
    elif letter == "6":
        result = string.startswith("T")
    elif letter == "7":
        result = string.endswith("e")
    elif letter == "8":
        result = string.capitalize()
    elif letter == "9":
        result = string.swapcase()
    else:
        print("EXIT....")
        exit()
    if result is not None:
        print(f"Result: {result}")

