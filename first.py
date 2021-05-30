calculation_to_seconds = 24

string_one = "days are"
string_two = "hours"


def days_to_units(num_of_days):
    
    if num_of_days > 0:
        return f"{num_of_days} {string_one} {num_of_days * calculation_to_seconds} {string_two}"
    elif num_of_days == 0:
        return "you entered 0"

def validate_and_execute():

    input_data = input("Hey user enter number of days \n")
    if input_data.isdigit():
        print(type(input_data))

        my_var = days_to_units(int(input_data))

        print(my_var)
    else:
        print("your input is no valid number")


validate_and_execute()