# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temperature_input = input("Enter the temperature to convert (or type 'exit' to quit): ")
            if temperature_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Validate if the input is numeric
            temperature = float(temperature_input)

            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if unit not in ['C', 'F']:
                raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

            if unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
        except ValueError as e:
            print(f"Invalid input. {e}. Please enter a numeric temperature.")

if __name__ == "__main__":
    main()
