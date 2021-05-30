


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute():
    
    try:

        num_of_days = int(days_and_unit_dictionary["days"])

        # We want to make convertion only to positives digits
        if num_of_days > 0:
            result = days_to_units(num_of_days,days_and_unit_dictionary["unit"])
            print(result)
        elif num_of_days == 0:
            print( "You entered 0")
        else:
            print("You entered negative number")
        
        
    except ValueError:
        print("Your input is no valid number")


input_data = " "
while input_data != "exit":
    input_data = input("Hey user enter a numbers of days and conversion unit \n")
    days_and_unit = input_data.split(":")

    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

    validate_and_execute()
