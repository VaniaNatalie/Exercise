print("Temperature converter")
def convert_temp():
    farenheit = float(input("Enter a temperature in Farenheit: "))
    celcius = (5 / 9) * (float(farenheit) - 32)
    kelvin = celcius + 273
    print(" ")
    print("The temperature in Farenheit is:", farenheit)
    print("The temperature in Celcius is:", celcius)
    print("The temperature in Kelvin is:", kelvin)

convert_temp()