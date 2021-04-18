x = 40
y = 0

try:
    print(x / y)
except ZeroDivisionError as error:
    print("Not allowed divided by zero")
else:
    print("Something went wrong")
finally:
    print("disconnect")
