# Q1 Write a program to find sum of digits of given numbers
i = int(input("Enter the number:"))
sum = 0
while(i>0):
    sum=sum+i%10
    i = i//10
print("Sum of digits=",sum)
