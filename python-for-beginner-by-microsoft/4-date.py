from datetime import datetime, timedelta
# / get current date
# current_date = datetime.now()
# print(current_date)

# print("Today is" + " " + str(current_date))

# / date function
# today = datetime.now()
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print("yesterday is " + str(yesterday))

# two_week = timedelta(weeks=2)
# last_two_week = today - two_week
# print(last_two_week)

# / format date
# today = datetime.now()
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.hour)
# print(today.minute)
# print(today.second)

# / input date
birthday = input("Please enter your birthday in(mm/dd/yyyy) : ")
my_birth_day = datetime.strptime(birthday, "%m/%d/%Y")
# using dash - as separator also possible
# birthday = input("Please enter your birthday in(mm-dd-yyyy) : ")
# my_birth_day = datetime.strptime(birthday, "%m-%d-%Y")
print("Birthday : " + str(my_birth_day))
