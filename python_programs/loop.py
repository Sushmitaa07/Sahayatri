#1. print"softwarica"10 times
for i in range(11):
    print('softwarica')

#2. Sum of a list
numbers =[1, 2, 3, 4,5]
total = 0
for number in numbers:
    total += number
    print(total)

#3. print each character using indexing
a='programming'
b=len(a)
for i in range(b):
    print(i, '=', a[i] )

#4. write a program to display integer from of a list.given list=[1,"a","c",2,3,4]
list=[1,"a","c",2,3,4]
for i in list:
    if isinstance (i,int):
        print(i)

#5. multiplication of a each element. given list={4,5,3,2}
list=[4,5,3,2]
total=1
for i in list:
    total *=i
print(total)


#6. multiplication table of a given number
a = 3
for i in range(1,11):
    print(a,'x',i,'=',a*i)

#7. Reverse a list
a=[1,2,3]
a=[1,2,3,4]
reverse_list=[] #[4,3,2,1]
#Q.No. 7 reverse a list
a=[1,2,3,4]
reverse_list=[] #[4,3,2,1]
 
# for i in a:
reverse_list = [i]+reverse_list
print(reverse_list)



#Q.No. 8 given list is [1,2,3,4] but expected output in new list [2,3,4,5]
a=[1,2,3,4]
# print(len(a))
b=[]
for i in range(len(a)): #0 1 2 3
    if i==0:
        continue
    else:

        b.append(a[i])
        if i==3:
            b.append(5)
print(b)

#9 given list is [1,2,3,4] but expected output in new list [2,3,4,5]
a=[1,2,3,4]
# print(len(a))
b=[]
for i in range(len(a)): #0 1 2 3
    if i==0:
        continue
    
    else:

        b.append(a[i])
        if i==3:
            b.append(5)
print(b)

#10 Given list is lst=[1,2,3,4] but print 1 and 4 only 
lst=[1,2,3,4]
print(lst[0],lst[-1])

#Given list is lst=[1,2,3,4] but print 1 2 and 4 only 
lst=[1,2,3,4]
print(lst[0],lst[1],lst[-1])

#11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]
new_lst = []

for i in range(len(lst)):
    if i == 1:
        new_lst.append("a")
    else:
        new_lst.append(lst[i])

print(new_lst)
    

#12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
list=[1,2,3,4,5]
odd=[]
even=[]
for a in list:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
print("even number:",even)
print("odd number:",odd)

#13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
list=[1,2,3,"d",4,5,"a"]
integers=[]
strings=[]
for x in list:
    if isinstance(x,int):
        integers.append(x)
    elif isinstance(x,str):
        strings.append(x)
print("the integers are:",integers)
print("the string are:",strings)

#14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
list=[1,2,3,4,"a","b"]
integer=[]
string=[]
for x in list:
    if isinstance(x,int):
        integer.append(x)
    elif isinstance(x,str):
        string.append(x)
print("Integers=",integer)
print("String=",string)

#15. Python program that accepts a string and calculate the number of digits and letters and space
input_string = input("Enter a string: ")

num_digits = 0
num_letters = 0
num_spaces = 0

for char in input_string:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1
    elif char.isspace():
        num_spaces += 1

print(f"Number of digits: {num_digits}")
print(f"Number of letters: {num_letters}")
print(f"Number of spaces: {num_spaces}")

#17. program to print the given number is odd or even 
a=int(input("enter a number:"))
if a%2==0:
    print("the number is even")
else :
    print ("the number is odd")

    #19. Print multiplication table of  1,2,3,4,5,6,7,8 
for i in range(1, 9):  
        print(f"Multiplication table of {i}:")
        for j in range(1, 11):  
            print(f"{i} * {j} = {i * j}")
        print()  


#20. Given list is lst=[1,2,3,4] but print 1 and 2 only
lst=[1,2,3,4]
print(lst[0],lst[1])

#23. Python program to count the space of a given string.
input_string = input("Enter a string: ")
num_spaces = 0
for char in input_string:
    if char.isspace():
        num_spaces += 1
print(f"Number of spaces: {num_spaces}")

#24. given list is [1,2,3,4] but expected output is [1,8,27,64]
list=[1,2,3,4]
new_list=[]
for z in list:
    new_list.append(z**3)
print(new_list)

#25. reverse of a string a="programming". 
a = "programming"
reversed = ""
for i in range(len(a) - 1, -1, -1):
    reversed += a[i]
print(reversed)

#26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(50):
    print(i)
    if i == 7:
        break

#27Write a for loop that iterates through a string and prints every character.
string = "Good Morning"
for char in string:
    print(char)

    #28Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a=["ram","shyam",1,2]
for name in a:
    if isinstance(name, str):  
        print(f"Hello!, {name}")


#29Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a=["ram","shyam"]
lst=[]
for name in a:
    lst.append(f"Dr{name}")
print(lst)

#30Write a for loop which appends the square of each number to the new list.
lst=[1,2,3,4,5]
new_list=[]
for x in lst:
    new_list.append(x**2)
print(new_list)

#31Write a for loop using an if statement, that appends each number to the new list if it's positive. 
#given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
new_list=[]
for x in lst1:
    if x>0:
        new_list.append(x)
print(new_list)

#32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
list=[0,1,2,3,4,5,6]
for num in list:
    if num != 3 and num != 6:
        print(num)

 # 33. Write a for loop which appends the type of each element in the first list to the second list.
 
first_list=[1,3,4,'apple',3.01,'game']
second_list=[]
for items in first_list:
    second_list.append(items)
print(second_list)





 # 34. Use else block to display a message “Done” after successful execution of for loop.
 #34. Use else block to display a message “Done” after successful execution of for loop.
lst=['a','b','c','d','e']
for i in lst:
    print(i)
else:
    print("Done")




 # 35. Write a for loop statement to print the following series: 
#105 98 -------7
for i in range(105, 6, -7):
   print(i,end = ' ')




#36removal bad characters from the given string.
# Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython

bad_chars = [';', ':', '!', "*",' ']
string = "py;th* o:n ! ;py * t*h:o !n"
a = 0
for i in bad_chars:
    string = string.replace(i, '')

print(string)
 


# 37. Python program to count the number of even and odd numbers from a series of numbers.
a = eval(input('Enter list elements: '))
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('Total Even numbers: ', even)
print('Total Odd numbers: ', odd)




 38.# Write a python program to display all the prime numbers within a given range.
a = int(input('Enter the range of number: '))
count = 0
if a == 1:
    print(f'{a} is neither prime nor composite: ')
elif a == 0:
    print("The number is zero")
else:
   print ("\n the prime numbers are : ")
   for i in range (1,a+1):
    count = 0
    for j in range(1,i):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i, end = " ")


39.# given number is prime or not
a = int(input("Enter a number to check whether it is prime or not: "))
count = 0
if a != 1 and a != 0:
 for i in range(1, a):
    if a % i == 0:
         count +=1

 if count == 1:
    print("The number is prime")
 else:
    print("The number is composite")
else:
   print('Neither prime nor composite')



40.# program to check given number is palindrome or not
number = int(input("Enter a number: "))
num_str = str(number)
length = len(num_str)
 is_palindrome = True
 for i in range(length // 2):
  #   if num_str[i] != num_str[length - 1 - i]:
         is_palindrome = False
        break
 if is_palindrome:
    print(f"{number} is a palindrome.")

41# program to check given number is armstrong or not
number = int(input("Enter a number: "))
num_str = str(number)
num_length = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_length

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


#42 python program to check a number is perfect number
number = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")






