#Weather Forecast 
def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (float(fahrenheit) - 32) * 5/9
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

def main():
    fahrenheit = input("Enter the temperature in Fahrenheit: ")
    fahrenheit_to_celsius(fahrenheit)

if __name__ == "__main__":
    main()