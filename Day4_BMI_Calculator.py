#Created a function named bmi and passed two arguments height and weight
def calculator_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi

#created a function for bmi and its conditions using if else and conditional operators
def bmi_category(bmi):
    if bmi<18.5:
        return "underweight"
    elif bmi>=18.5 and bmi<24.9:
        return "Normal"
    elif bmi>=24.9 and bmi<29.9:
        return "Overweight"
    else:
        return "Obese"

#Created a main function to call functions amd print the final values
def main()
    weight=float("Enter weight in kgs: ")
    height=float("Enter height in ms: ")

    bmi=calculator_bmi(weight,height)
    category=bmi_category(bmi)
    print(f"\nYour bmi is: {bmi:.2f}")
    print(f"\nYou are of category: {category}")
if __name__=="__main__":
    main()
