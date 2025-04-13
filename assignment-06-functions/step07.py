def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"➤ {i}")

def main():
    try:
        num = int(input("Enter a number to find its divisors: → "))
        if num <= 0:
            print("Please enter a positive integer greater than 0.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return

    print_divisors(num)

if __name__ == "__main__":
    main()