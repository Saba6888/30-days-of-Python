type_conversion = {1: "Kelvin", 2: "Celsius", 3: "Fahrenheit"}
convert_into = {1: "Kelvin", 2: "Celsius", 3: "Fahrenheit"}

print("Welcome to the temperature converter!")
print("Your options are:- 1: Kelvin, 2: Celsius, 3: Fahrenheit, 4: Exit")

option = int(input("Enter the type of conversion (1, 2, 3, 4): "))
if option == 4:
    print("Thank you for coming!")
else:
    option1 = int(input("Enter the unit to convert into (1, 2, 3): "))
    temp_value = float(input("Enter the temperature value: "))

    if option == 1:  # Kelvin
        if option1 == 1:
            answer = temp_value
        elif option1 == 2:
            answer = temp_value - 273.15
        elif option1 == 3:
            answer = (temp_value - 273.15) * 1.8 + 32

    elif option == 2:  # Celsius
        if option1 == 1:
            answer = temp_value + 273.15
        elif option1 == 2:
            answer = temp_value
        elif option1 == 3:
            answer = temp_value * 1.8 + 32

    elif option == 3:  # Fahrenheit
        if option1 == 1:
            answer = (temp_value - 32) / 1.8 + 273.15
        elif option1 == 2:
            answer = (temp_value - 32) / 1.8
        elif option1 == 3:
            answer = temp_value

    print(f"Your desired conversion is: {answer} {convert_into[option1]}")
    print("Thank you for coming!")
