# Import
import time

# Welcome
print("Welcome to the Temperature calculator.")

# Ask
time.sleep(1)
print("Choose an option:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

time.sleep(1)
wtw = input("Enter choice(1 or 2): ")
# Calculate
if wtw == "1":
    askfah = int((input("Enter temperature in Fahrenheit: ")))
    fah = (askfah * 1.8) + 32
    print("The temperature in Fahrenheit is: " + str(fah))
elif wtw == "2":
    askcel = int((input("Enter temperature in Celsius: ")))
    cel = (askcel - 32) * 5 / 9
    print("The temperature in Celsius is: " + str(cel))
else:
    print("Invalid option")