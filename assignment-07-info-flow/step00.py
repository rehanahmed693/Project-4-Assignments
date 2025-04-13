def choose_return(option):
    if option == "A":
        return "You chose option A"
    elif option == "B":
        return "You chose option B"
    elif option == "C":
        return "You chose option C"
    else:
        return "Invalid option. Please choose A, B, or C."

def main():
    print("Choose one of the following options: A, B, C")
    option = input("Enter your choice: → ")

    result = choose_return(option)
    print(result)

if __name__ == "__main__":
    main()
