calculation_to_seconds = 24

string_one = "days are"
string_two = "hours"


def days_to_units(num_of_days):
    return num_of_days * calculation_to_seconds   

def validate_and_execute():
    
    try:

        num_of_days = int(input_data)

        if num_of_days > 0:
            result = days_to_units(num_of_days)
            print(f"{num_of_days} {string_one} {result} {string_two}")
        elif num_of_days == 0:
            print( "you entered 0")
        else:
            print("negative number")
        
        
    except ValueError:
        print("your input is no valid number")


input_data = " "
while input_data != "exit":
    input_data = input("Hey user enter number of days \n")
    validate_and_execute()
