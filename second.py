calculation_to_seconds = 24

string_one = "days are"
string_two = "hours"


def days_to_units(num_of_days):
    return num_of_days * calculation_to_seconds
        
    

def validate_and_execute():

    input_data = input("Hey user enter number of days and I will convert it to hours\n")

    if input_data.isdigit():

        num_of_days = int(input_data)

        if num_of_days > 0:
            result = days_to_units(num_of_days)
            print(f"{num_of_days} {string_one} {result} {string_two}")
        elif num_of_days == 0:
            print( "You entered 0")
        
        
    else:
        print("Your input is no valid number")


validate_and_execute()
