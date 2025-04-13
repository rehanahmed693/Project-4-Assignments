def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("Enter numbers separated by commas:")
    user_input = input("→ ")

    # Convert string input to list of numbers
    try:
        number_list = [float(num.strip()) for num in user_input.split(",")]
    except ValueError:
        print("Invalid input! Please enter valid numbers separated by commas.")
        return

    avg = calculate_average(number_list)
    print(f"Average of the given numbers: {avg:.2f}")

if __name__ == "__main__":
    main()