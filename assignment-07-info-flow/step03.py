def is_in_stock(product, stock):
    if product in stock and stock[product] > 0:
        return True
    else:
        return False

def main():
    stock = {
        "apple": 10,
        "banana": 0,
        "orange": 5,
        "grapes": 2
    }

    product = input("Enter the product name to check its stock: → ").lower()

    if is_in_stock(product, stock):
        print(f"✅ {product.capitalize()} is in stock!")
    else:
        print(f"❌ {product.capitalize()} is not in stock.")

if __name__ == "__main__":
    main()
