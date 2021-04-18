# price = float(input("Enter the price : "))
# if price >= 1.00:
#     tax = 0.7
# else:
#     tax = 0
# print(tax)

country = input("Enter your country : ").lower()

if country == "indonesia":
    province = input("Enter your province : ").lower()
    if province == "riau":
        tax = 0.3
    elif province in("aceh", "sumut"):
        tax = 0.2
    elif province == "jambi" or province == "bengkulu":
        tax = 0.4
    else:
        tax = 0.5
else:
    tax = 0
print("Your tax : ", tax)

# gpa = float(input("Enter your gpa : "))
# lowest_grade = float(input("Enter your lowest grade : "))
# if gpa >= 0.85 and lowest_grade >= 75:
#     honour_of_roll = True
# else:
#     honour_of_roll = False
# if honour_of_roll:
#     print("You achieve Honour of Roll")
