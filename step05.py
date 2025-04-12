def triangle():
    side1:float = float(input("enter your first side of triangle "))
    side2:float = float(input("enter your second side of triangle "))
    side3:float = float(input("enter your third side of triangle "))
    total:float = float (side1 + side2 + side3)
    print(f"The parameter of the triangle is {total}")

if __name__ == "__main__":  
    triangle()  