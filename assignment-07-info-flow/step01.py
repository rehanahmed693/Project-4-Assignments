def greet(name):
    return f"Hello, {name}! Welcome to the program."

def main():
    name = input("Please enter your name: → ")
    greeting_message = greet(name)
    print(greeting_message)

if __name__ == "__main__":
    main()