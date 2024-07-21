def get_temperature():
  while True:
    try:
      temperature = float(input("Enter a temperature: "))
      return temperature
    except ValueError:
      print("Invalid input. Please enter a number.")

def convert_temperature(temperature, from_unit, to_unit):
  """Converts temperature between Fahrenheit and Celsius."""
  if from_unit == "C" and to_unit == "F":
    return (temperature * 9/5) + 32
  elif from_unit == "F" and to_unit == "C":
    return (temperature - 32) * 5/9
  else:
    print("Invalid conversion direction. Please choose 'C' to 'F' or 'F' to 'C'.")
    return None  # Indicate invalid conversion

def main():
  print("Temperature Converter")

  while True:
    # Get temperature input
    temperature = get_temperature()

    # Get conversion direction
    from_unit = input("Enter the unit of the temperature (C or F): ").upper()
    to_unit = input("Enter the unit to convert to (C or F): ").upper()

    # Convert temperature
    converted_temp = convert_temperature(temperature, from_unit, to_unit)

    if converted_temp is not None:
      print(f"{temperature:.2f} {from_unit} is equal to {converted_temp:.2f} {to_unit}")
      break  # Exit loop on successful conversion

    # Handle invalid conversion direction and prompt user again
    print("Conversion failed. Please try again.")

if __name__ == "__main__":
  main()
