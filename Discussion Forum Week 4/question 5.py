print("Temperature converter")
def f_to_c(farenheit):
    celcius = (5 / 9) * (float(farenheit) - 32)
    return celcius

def c_to_k(celcius):
    kelvin = celcius + 273
    return kelvin

def convert_temp():
    farenheit = float(input("Enter a temperature in Farenheit: "))
    celcius = f_to_c(farenheit)
    print(" ")
    print("The temperature in Farenheit is:", farenheit)
    print("The temperature in Celcius is:", f_to_c(farenheit))
    print("The temperature in Kelvin is:", c_to_k(celcius))

convert_temp()
