def get_name():
    name = input("👋 What's your name? → ").strip()

    if not name:
        print("⚠️ You didn't enter a name!")
    else:
        print(f"🎉 Hello, {name}! Nice to meet you!")

def main():
    get_name()

if __name__ == "__main__":
    main()