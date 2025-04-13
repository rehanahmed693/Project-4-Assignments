def subtract_seven(number):
    return number - 7

def main():
    try:
        num = float(input("🔢 Enter a number: → "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    result = subtract_seven(num)
    print(f"✅ After subtracting 7, the result is: {result}")

if __name__ == "__main__":
    main()