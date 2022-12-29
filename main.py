#Write a function called number_compare. This function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater" If the second number is greater than the first, the function returns "Second is greater" Otherwise the function returns "Numbers are equal"
first=0
f=0
second=0
s=0

#start with making a function with comparing for <>=
def number_compare(first,second):
        if (first == second):
            print("Numbers are equal.")
        elif (first > second):
            print("First is greater.")
        else: print ("Second is greater.")

#entering two numbers to compare
f = input("Please enter your first number")
first=int(f)
s = input("Please enter a second number")
second=int(s)
#compare the numbers
number_compare (first, second)