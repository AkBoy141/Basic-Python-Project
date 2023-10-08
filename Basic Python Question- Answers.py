# Question 1.

# Write a Python program that takes two numbers as input and prints the larger number.

# Answer 1.

Digit_1=int(input("Enter the first number here:"))
Digit_2=int(input("Enter the second number:"))
if Digit_1>Digit_2:
    print("Larger number is: ",Digit_1)
elif Digit_2>Digit_1:
    print("Larger number is: ",Digit_2)
elif Digit_1==Digit_2:
    print("Both are equal")
else:
    print("Both are Equal")





# Question 2.

# Create a Python program that asks the user for a month (1-12) and
# then prints the corresponding season ("Spring," "Summer," "Fall," or "Winter").

# Answer


Month=str(input("Enter Month: "))
if Month==("Jan"):
    print("Winter")
elif Month==("Feb"):
    print("Winter")
elif Month==("March"):
    print("Spring")
elif Month==("April"):
    print("Spring")
elif Month==("May"):
    print("Spring")
elif Month==("June"):
    print("Summer")
elif Month==("July"):
    print("Summer")
elif Month==("Aug"):
    print("Summer")
elif Month==("Sept"):
    print("Fall")
elif Month==("Oct"):
    print("Fall")
elif Month==("Nov"):
    print("Fall")
elif Month==("Dec"):
    print("Winter")




# Question 3.

# Write a Python program that determines whether a given year is a leap year or not. Use the leap year rules mentioned earlier.

Year=int(input("Enter Year Here: "))

if (Year%4==0 and Year%100 !=0) or (Year%400==0):
    print("Given Year is a Leap Year")

else:
    print("Given Year is not a Leap Year")





# Question 4.

# Create a program that takes an integer as input and checks if it's positive, negative, or zero. Print an appropriate message.
# Answer 4.

number = float(input("Enter the number : "))

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")




# Question 5.

#Write a Python program that asks the user for their age and gender.
# Based on their age and gender, print a message like "You are a young man" or "You are an old woman."

# Answer 5.

age = int(input("Enter the age: "))
gender = input("Enter the gender (Male/Female): ")

# Here Age: 18 is criteria that specified (below 18 or <18) are "Youngers" and (above 18 or 18<) are olders.
if age < 18:
    if gender == "Male":
        print("You are a young boy")
    elif gender == "Female":
        print("You are young girl")


else:
    if gender == "Male":
        print("you are an old man")
    elif gender == "Female":
        print("You are old woman ")





# Question 6.

# Create a program that takes a temperature in Celsius and converts it to Fahrenheit. Display the result with an appropriate message.

# Answer 6.

celsius = float(input("Enter the temp in Cel: "))

fahrenheit = (celsius * 9/5) + 32

print("Temp in fahrenheit will be: ", fahrenheit)





# Question 7.

# Write a Python program that calculates the shipping cost based on the weight of a package. Use the following rules:

# Weight <= 2 pounds:  5.00
# 2𝑝𝑜𝑢𝑛𝑑𝑠<𝑊𝑒𝑖𝑔ℎ𝑡<=10𝑝𝑜𝑢𝑛𝑑𝑠: 10.00
# Weight > 10 pounds: 15.00

# Answer 7.


weight = float(input("Enter the weight in pound: "))

# shipping cost based on weight

if weight <= 2:
    print("shipping_cost= 5.00")
elif weight <= 10:
    print("shipping_cost = 10.00")
else:
    print("shipping_cost = 15.00")






# Question 8.

# Create a program that asks the user for three numbers and then prints them in ascending order.

# Answer 8.

number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))
number_3 = int(input("Enter the number 3: "))


# sort the numbers in ascending order

sorted_numbers = sorted([number_1,number_2,number_3])

print("Numbers in ascending order are: ", sorted_numbers)





# Question 9.

# Write a Python program that checks if a given year is a "century year" (ends in 00). If it's a century year, check if it's a leap year.

# Answer 9.

year = int(input("Enter year here: "))

# check if the year is a century year

if year%100==0:
    print("This year is a century year")

if year%400==0:
        print("This is a leap year century")
else:
    print("This is not a century leap year")






# Question 10.

# Create a program that asks the user for a number and then determines if it's even or odd. Print an appropriate message.

# Answer 10.

Digit=int(input("Enter your Digit here: "))

if Digit%2==0:
    print("Given number is Even number")
else:
    print("Given number is Odd number")
