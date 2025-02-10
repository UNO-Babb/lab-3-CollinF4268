#TempConvert.py
#Name:Collin Frederick
#Date:2/9/25
#Assignment:

def main():
    tempF = float(input("Enter temperature in Fahrenheit: "))

    tempC = (tempF - 32) * 5 / 9

    print(f"{tempF}°F is {round(tempC, 1)}°C.")

if __name__ == "__main__":
    main()