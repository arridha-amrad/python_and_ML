# from datetime import datetime


# def print_task(task_name):
#     print("task name : ", task_name)
#     print("due at ", datetime.now())


# print_task("learn python")

# for index in range(0, 5):
#     print(index)
# print_task("calculating")

# / get initial name
# def get_initial(name, force_uppercase=True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial


# first_name = input("Enter your first name : ")
# first_initial = get_initial(first_name, False)
# last_name = input("Enter your last name : ")
# last_initial = get_initial(last_name)

# print(f"Your initial is : {first_initial}{last_initial}")

# / named parameters
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("Enter your first name : ")
first_initial = get_initial(name=first_name, force_uppercase=False)
last_name = input("Enter your last name : ")
last_initial = get_initial(name=last_name)

print(f"Your initial is : {first_initial}{last_initial}")
