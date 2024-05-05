# Temperature Conversion

# Write two functions named celsiusToFahrenheit and fahrenheitToCelsius to convert between Celsius and Fahrenheit.

# Use the functions to convert a given temperature.

def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = 20
fahrenheit = celsiusToFahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

fahrenheit = 68
celsius = fahrenheitToCelsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
