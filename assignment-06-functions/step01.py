import random
import time

def chaotic_counting(start, end, delay=0.5):
    numbers = list(range(start, end + 1))
    random.shuffle(numbers)  # Random order

    print("🤪 Chaotic Counting Begins!")
    for number in numbers:
        print(number)
        time.sleep(delay)  # Small delay for effect
    print("🎉 Done with chaotic counting!")

def main():
    print("Enter start and end numbers for chaotic counting.")
    try:
        start = int(input("Start → "))
        end = int(input("End → "))

        if start > end:
            print("❌ Start should be less than or equal to end!")
            return

        chaotic_counting(start, end)
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()