def print_multiples(n, count):
    print(f"First {count} multiples of {n} are:")
    for i in range(1, count + 1):
        print(f"➤ {n} × {i} = {n * i}")

def main():
    try:
        num = int(input("Enter a number to find its multiples: → "))
        count = int(input("How many multiples do you want to see? → "))
        if num <= 0 or count <= 0:
            print("⚠️ Please enter positive numbers only.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
        return

    print_multiples(num, count)

if __name__ == "__main__":
    main()