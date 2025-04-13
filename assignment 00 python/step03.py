def temp():
    fahrenheit_degree = float(input("enter your fahrenheit degree "))
    celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
    print(f'temperature {fahrenheit_degree}f = {celsius_degree}c')

if __name__ == "__main__" :
    temp()   
