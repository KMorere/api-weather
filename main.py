

def main():
    choice = get_choice()

    if choice == "1":
        print() # TODO: Get Toulouse weather forecast.
        get_choice()

    elif choice == "2":
        print() # TODO: Get Merignac weather forecast.
        get_choice()

    elif choice == "3":
        print() # TODO: Get Saint-Geours weather forecast.
        get_choice()

    elif choice == "0":
        print("Leaving...")
    else:
        print("Unvalid choice, select a number between 0-3")
        get_choice()


def get_choice():
    print()
    print("=====Weather MENU=====")
    print("1 - Display Toulouse weather forecast")
    print("2 - Display Merignac weather forecast")
    print("3 - Display Saint-Geours weather forecast")
    print("0 - Leave")
    print()

    return input("Select a choice: ")


if __name__ == "__main__":
    main()