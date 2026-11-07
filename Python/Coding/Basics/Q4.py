# Question 4: Write a Python program to find the largest 
# of three numbers.
def largest_of_three_num(a,b,c):
    if a>b and a>c:
        print(a,"is largest")
    elif b>a and b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")

if __name__ == "__main__":
    a=40;b=50;c=45
    largest_of_three_num(a,b,c)
