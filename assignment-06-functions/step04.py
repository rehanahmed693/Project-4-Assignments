def double_numbers(numbers):
    return [num * 2 for num in numbers]

def main():
    print("Enter numbers separated by commas to double them:")
    user_input = input("→ ")

    try:
        number_list = [int(num.strip()) for num in user_input.split(",")]
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
        return

    doubled = double_numbers(number_list)
    print(f"✅ Doubled numbers: {doubled}")

if __name__ == "__main__":
    main()
     