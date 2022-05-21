import datetime

user_input = input("enter your goal with a deadline seperated by coln \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")
#calculation how many days flom now to deadline

today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Dear user time till your goal: {goal} is {time_till.days} days")ggfgd