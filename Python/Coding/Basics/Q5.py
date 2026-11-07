# Question 5: Write a Python program to calculate the factorial of a number.

def factorial_num_for(number):  #Using For loop
    fact = 1
    for i in range(1,number+1):
        fact*=i
    return fact

def factorial_num_while(number):  #using while loop
    fact=1
    while number>0:
        fact *= number
        number-=1
    return fact

def factorial_num_rec(number):  #using recursion
    if number>0:
        return number * factorial_num_rec(number-1)
    elif number==0:
        return 1

if __name__ == "__main__":
    a = 5
    print(factorial_num_rec(a))