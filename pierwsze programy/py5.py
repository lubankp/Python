calculation_to_seconds = 24

string_one = "days are"
string_two = "hours"


def days_to_units(num_of_days):
    return num_of_days * calculation_to_seconds   

def validate_and_execute():
    
    try:

        num_of_days = int(user_data_elememt)

        # We want to make convertion only to positives digits
        if num_of_days > 0:
            result = days_to_units(num_of_days)
            print(f"{num_of_days} {string_one} {result} {string_two}")
        elif num_of_days == 0:
            print( "You entered 0")
        else:
            print("You entered negative number")
        
        
    except ValueError:
        print("Your input is no valid number")


input_data = " "
while input_data != "exit":
    input_data = input("Hey user enter a numbers of days seperated by comas and I will convert it to hours \n")
    list_of_days = input_data.split(",")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for user_data_elememt in set(list_of_days):
        validate_and_execute()
