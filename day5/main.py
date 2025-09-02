monthConversions = {
    1: {"name": "January", "fact": "January is named after Janus, the Roman god of doors."},
    2: {"name": "February", "fact": "February is the shortest month of the year."},
    3: {"name": "March", "fact": "March was the first month in the original Roman calendar."},
    4: {"name": "April", "fact": "April's name is derived from the Latin word 'aperire' which means 'to open.'"},
    5: {"name": "May", "fact": "May is named after Maia, the goddess of growth."},
    6: {"name": "June", "fact": "June is named after Juno, the Roman goddess of marriage and childbirth."},
    7: {"name": "July", "fact": "July is named after Julius Caesar."},
    8: {"name": "August", "fact": "August is named after Augustus Caesar."},
    9: {"name": "September", "fact": "September's name comes from the Latin word 'septem,' meaning seven."},
    10: {"name": "October", "fact": "October was the eighth month in the old Roman calendar."},
    11: {"name": "November", "fact": "November's name comes from the Latin word 'novem,' meaning nine."},
    12: {"name": "December", "fact": "December's name comes from the Latin word 'decem,' meaning ten."}
}

option = int(input("Enter month number (1-12): "))

if option in monthConversions:
    month_info = monthConversions[option]
    print(f"Month: {month_info['name']}")
    print(f"Fun Fact: {month_info['fact']}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
