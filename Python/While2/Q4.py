# Q4 Write a program to check wheather a given number is Armstrong number or not
i =int(input("Enter the number"))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i = i//10
if orig==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
