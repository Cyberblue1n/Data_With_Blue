#Question 10: Write a Python program to check if a variable is of a 
# specific data type.
a = 6.84
if type(a)==str:
    print(f"{a} is a String")
elif type(a)==int:
    print(f"{a} is a integer")
elif type(a)==float:
    print(f"{a} is a floating point number")
elif type(a)==bool:
    print(f"{a} is a boolean value")

# Using isinstace function (Qs10)
b = 6
if isinstance(b, str):
    print(f"{b} is a String")
elif isinstance(b, int):
    print(f"{b} is a integer")
elif isinstance(b, float):
    print(f"{b} is a floating point number")
elif isinstance(b, bool):
    print(f"{b} is a boolean value")


# Using try and except (Qs10)

c = input("Enter a value: ")
if c.lower()=="true" or c.lower()=="false":
    print(f"{c} is a boolean value")
else:
    try:
        int(c)
        print(f"{c} is an integer value")

    except ValueError:
        try:
            float(c)
            print(f"{c} is an floating value")
        except ValueError:
            print(f"{c} is String")





    
