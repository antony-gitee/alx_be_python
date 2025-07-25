def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # May raise ValueError

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
