import helper

input_data = " "
while input_data != "exit":
    input_data = input("Hey user enter a numbers of days and conversion unit \n")
    days_and_unit = input_data.split(":")

    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

    helper.validate_and_execute(days_and_unit_dictionary)
