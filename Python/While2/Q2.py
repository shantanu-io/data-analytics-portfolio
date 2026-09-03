# Q2 Write a program to find sum of square of digits of agiven numbers

i = int(input("Enter the number:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("Sum of square of each digits =",sum)
