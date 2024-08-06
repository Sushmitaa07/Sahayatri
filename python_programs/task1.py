Q.No.1
a = input("Enter a value of a:")
b = input("Enter a valur of b:")
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")
 
#Q.No.2
a = input("Enter a value of a:")
b = input("Enter a value of b:")
c = input("Enter a value of c:")
d = input("Enter a value of d:")
if a==b or c==d:
    print("Hello")
else:
    print("invalid")
 
#Q.No.3
a = input("Enter a value of a:")
b = input("Enter a value of b:")
c = input("Enter a value of c:")
d = input("Enter a value of d:")
if a==b and c==d:
    print("Hello")
else:
    print("Incorrect")
 
#Q.No. 4
x = int(input("Enter the value of x"))
if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("zero")
 
 
#Q.No. 5
number = int(input("Enter a number"))
if number%2==0:
    print("The given number is even")
else:
    print("The number is odd")

#6. WAP which accepts marks of four subjects and display total marks, percentage and grade.
#Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –> pass, less than 40 –> fail
a=float(input("enter marks of maths:"))
b=float(input("enter marks of science:"))
c=float(input("enter marks of social:"))
d=float(input("enter marks of nepali:"))
totalmarks=float(a+b+c+d)
print("the total marks is:",totalmarks)
percentage=float(totalmarks/400)*100
print("the total percentage is:",percentage)
if percentage >=70:
    print("Distinction")
elif percentage >=60:
    print("First")
elif percentage >=40:
    print("pass")   
else:
    print("fail")

    #8. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
#Cost price(in Rs)                  Tax
#>100000                              15%
#>50000 and <=100000      10%
#<=50000                               5%

a=float(input("enter the price of bike:"))
if a>100000:
    print("The tax to be paid is 15%")
elif a>50000 and a<=100000:
    print("The tax to be paid is 10%")
else:
    print("The tax is 5%")


    # 11. Accept the grades from the user and display the grade according to the following criteria:
#Below 25 --D
#25 to 45  -- C
#45 to 50 -- B
#50 to 60 --B+
#60 to 80 -- A
#Above 80 -- A+

marks = float(input("Enter the marks: "))

if marks < 25:
    print("Grade: D")
elif 25 <= marks < 45:
    print("Grade: C")
elif 45 <= marks< 50:
    print("Grade: B")
elif 50 <= marks < 60:
    print("Grade: B+")
elif 60 <= marks < 80:
    print("Grade: A")
else:
    print("Grade: A+")






'''12. A company decided to give bonus to employee according to following criteria:
Time period of service     Bonus
More than 10 years            10%
>=6 and <=10                       8%
Less than 6 years                5%'''

years_of_service = float(input("Enter the number of years of service: "))


if years_of_service > 10:
    bonus = 0.10
elif years_of_service >= 6:
    bonus = 0.8
else:
    bonus = 0.05

# Displaying the bonus percentage
print("Bonus percentage:{}%".format(bonus * 100))

'''14. Accept the number of days from the user and calculate the charge for library according to following:
Till five days: Rs 2/day
Six to ten days: Rs 3/day
11 to 15 days: Rs 4/day
After 15 days: Rs 5/day'''

number_of_days=int(input("The number of days:"))

if number_of_days==5:
    rate=2
elif number_of_days>=6 and number_of_days<=10:
    rate=3
elif number_of_days>=11 and number_of_days<=15:
    rate =4
else :
    rate=5
print("the charge for libary is Rs {} for {} days".format(number_of_days*rate,number_of_days))

#15. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. .
#Ask user for their salary and year of service and print the net bonus amount.
salaryofemployee=float(input("enter the salary of employee:"))
yearofservice=float(input("The year of service of employee:"))
if yearofservice>5:
    bonus=float(0.05)

    print("You are eligible for bonus.")
else:
    print("There is no bonous")
print("the net bonous amount is Rs{}".format(salaryofemployee*bonus))

#17. Write a Python program to display your details like name, age, address in three different lines.
print("Name of person:{}\n the age of person:{}\n adress of person:{}".format("prakriti",19,"dillibajar"))

#18. Write a python program which accepts the radius of circle from user and compute the area.
radius=float(input("Enter the radius of circle:"))
area=float( 3.14*radius**2)
print("the area of the circle is {}".format(area))

'''19. A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
 The second group has 21 students, so they can get by with no fewer than 11 desks.
   11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.'''

student_in_class1=int(input("Enter the number of students:"))
student_in_class2=int(input("Enter the number of students:"))
student_in_class3=int(input("Enter the number of students:"))

desk1=(student_in_class1+1)/2
desk2=(student_in_class1+1)/2
desk3=(student_in_class1+1)/2

totaldesk=desk1+desk2+desk3
print("The total no of desk:",totaldesk)

'''20. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. 
It should print the two answers for the questions above.'''

N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))


apples_per_student = K // N #quotient

remaining_apples = K % N #reminder
print("Each single student will get {} apples.".format(apples_per_student))
print("There will be {} apples remaining in the basket.".format(remaining_apples))


'''21. A company decided to give bonus to employee according to following criteria:
Time period of service     Bonus
More than 10 years            10%
>=6 and <=10                       8%
Less than 6 years                5%'''

years_of_service = float(input("Enter the number of years of service: "))


if years_of_service > 10:
    bonus = 0.10
elif years_of_service >= 6:
    bonus = 0.8
else:
    bonus = 0.05

# Displaying the bonus percentage
print("Bonus percentage:{}%".format(bonus * 100))

'''22. Accept three numbers from the user and display the second largest number.'''

A=float(input("Enter the first number is:"))
B=float(input("Enter the second number is:"))
C=float(input("Enter the third number is:"))

if A>=B and A>=C:
    second_largest=max(B,C)
elif B>=A and B>=C:
    second_largest=max(A,C)
else:
    second_largest=C
print("The second largest number is ",second_largest)

#23. Write a program to check whether a person is eligible for voting or not. (accept age from user)

age_of_person=int(input("Enter the age of a person:"))
if age_of_person>=18:
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

    #24. Write a program to check whether a number is divisible by 7 or not.

number=int(input("Enter a number:"))
if number%7==0:
    print("{} is divisible by 7".format(number))
else :
    print("{} is not divisible by 7".format(number))

    '''25. Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Taj Mahal
                  Jaipur                              Jal Mahal'''

city_monument={
    "Delhi": "Red Fort",
    "Agra": "Taj Mahal",
    "Jaipur": "Jal Mahal"
}
city_name=input("Enter the name of city:")
if city_name in city_monument:
    monument = city_monument[city_name]
    print("The monument of {} is: {}".format(city_name, monument))
else:
    print("Monument information for {} is not available.".format(city_name))


#26. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both

number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print("{} is divisible by both 2 and 3.".format(number))
else:
    print("{} is not divisible by both 2 and 3.".format(number))



'''27. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
Like:
Enter First Number: 7
Enter Second Number : 9
Enter operator : +
Your Answer is : 16'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Your Answer is:", result)

#28. Write a program to check whether a number entered is three digit number or not.

number = int(input("Enter a number: "))
if 100 <= number <= 999:
    print("{} is a three-digit number.".format(number))
else:
    print("{} is not a three-digit number.".format(number))

    '''29. Accept the following from the user and calculate the percentage of class attended:
a. Total number of working days
b. Total number of days for absent
After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.'''

working_days=int(input("Enter the total  number of working days:"))
absent_days=int(input("Enter the total number of absent days:"))
percentage=((working_days-absent_days)/working_days)*100
print("the percentage of class attended is {} %".format(percentage))
if percentage<75:
    print("The student will not be able to sit in exam.")
else:
    print("The student can sit in exam.")

'''30. Write a program to accept percentage and display the category according to the following criteria:
Percentage                                   Category
<40                                              Failed
>=40 and <55                             Fair
>=55 and <65                             Good
>=65                                            Excellent    '''

percentage = float(input("Enter the percentage: "))


if percentage < 40:
    category = "Failed"
elif percentage >= 40 and percentage < 55:
    category = "Fair"
elif percentage >= 55 and percentage < 65:
    category = "Good"
else:
    category = "Excellent"


print("Category: {}".format(category))

'''31. Accept the age, gender('M', 'F'), number of days and display the wages accordingly.
Age               Gender    Wage/day
>=18 and <30      M             700
                  F              750
>=30 and <=40    M             800
                 F              850'''

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
days_worked = int(input("Enter the number of days worked: "))

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
else:
    wage_per_day = 0
    print("Sorry! Age category not defined for the given age range.")

total_wages = days_worked * wage_per_day if wage_per_day > 0 else 0
if total_wages > 0:
    print("Total wages: Rs", total_wages)

    '''32. Accept three numbers from the user and display the second largest number.'''

A=float(input("Enter the first number is:"))
B=float(input("Enter the second number is:"))
C=float(input("Enter the third number is:"))

if A>=B and A>=C:
    second_largest=max(B,C)
elif B>=A and B>=C:
    second_largest=max(A,C)
else:
    second_largest=C
print("The second largest number is ",second_largest)

    for i in range(10):
        print('softwarica')


a='softwarica'
for i in a:
    print(i)

    a='python'
    b=len(a)
    for i in range(b):
        print(i, '=',a[i])

   #provide a multipication table for given number
   a=2
   for i in range (1,11 ):
    print(a,'x',i,'=',a*1)













        
    
        


    