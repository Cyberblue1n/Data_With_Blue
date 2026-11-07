# Question 3: Write a Python program to check if a number 
# is positive, negative, or zero.
def program_check(num):
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    number = 5
    program_check(number)