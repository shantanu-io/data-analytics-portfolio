# Q3 Write a program to find sum of cube of digits of number
i = int(input("Enter the number:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i = i//10
print("Sum pf cube of given number=",sum)
