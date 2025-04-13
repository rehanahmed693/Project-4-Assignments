import random

nouns = ["cat", "boy", "girl", "dog", "robot"]
verbs = ["eats", "plays with", "runs to", "looks at", "builds"]
places = ["the park", "school", "home", "the moon", "a castle"]

def generate_sentence():
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    place = random.choice(places)
    return f"The {noun} {verb} {place}."
def main():
    try:
        count = int(input("📄 How many sentences do you want to generate? → "))
        if count <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return

    print("\n📝 Generated Sentences:")
    for _ in range(count):
        print("➤", generate_sentence())

if __name__ == "__main__":
    main()