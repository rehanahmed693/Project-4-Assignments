def count_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return len(even_numbers), even_numbers

def main():
    print("Enter numbers separated by commas:")
    user_input = input("→ ")

    try:
        number_list = [int(num.strip()) for num in user_input.split(",")]
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
        return

    count, evens = count_even_numbers(number_list)
    print(f"✅ Total even numbers: {count}")
    print(f"Even numbers: {evens}")

if __name__ == "__main__":
    main()