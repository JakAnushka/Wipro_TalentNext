''' 1.	create a python program that asks the user how far they want to travel.
if they want to travel less than three miles tell them to ride Bicycle.
if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle.
if they want to travel three hundred miles or more tell them to driver '''
user_distance=int(input("How far they want to travel"))
if user_distance<=3:
    print("I suggest Super-Bicycle to your destination")
elif user_distance>3 and user_distance<300:
    print("I suggest Super-Motor-cycleto your destination")
else:
    print("I suggest Super-Car to your destination")

'''2.Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. 
you pick a hosting provider that charges $0.51 per hour. 
you will launch your services using one server and want to know how much it will cost to operate per day,
 per week, per month.
'''
cost_per_hr=0.51
cost_per_day=0.51*24
cost_per_week=0.51*7
cost_per_month=0.51*30
budget=918
days_budget=budget/cost_per_day

print(f"hosting provider that charges ${cost_per_day} per day")
print(f"hosting provider that charges ${cost_per_week} per week")
print(f"hosting provider that charges ${cost_per_month} per month")
print(f"With ${budget}, you can operate one server for approximately {days_budget} days.")
