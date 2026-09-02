# Write a program to find max between two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Max is:", a)
else:
    print("Max is:", b)

# Write a program to find Age eligibility for voting
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Write a program to check if a number is positive, negative, or zero
num = int(input("Enter the number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Write a program to find the middle number in a group of three numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if (a > b and a < c) or (a < b and a > c):
    print("The middle number is:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("The middle number is:", b)
else:
    print("The middle number is:", c)

# Write a program to calculate total marks in 5 subjects.
# Full marks = 100 as wel as percentge of marks and division of marks.
# per >=80 Grade A
# per >=60 Grade B
# per >=40 Grade C
# per <40 Grade D


a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))
d = int(input("Enter marks of subject 4: "))
e = int(input("Enter marks of subject 5: "))

total = a + b + c + d + e

percentage=(total/500)*100
print("Total marks:", total, "Percentage:", percentage)

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: D")