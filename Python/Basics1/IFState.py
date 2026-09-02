# Statements are executed in the order they are written. 
# The first statement is executed first, followed by the second statement, and so on.
# 1 Selection statements allow you to execute certain statements based on a condition.
# if statement: The if statement is used to execute a block of code if a specified condition is true.
# Example:
x = 10
if x > 5:
    print("x is greater than 5")

# while statement: The while statement is used to execute a block of code repeatedly as long as a specified condition is true.
# Example:
y = 0
while y < 5:
    print("y is:", y)
    y += 1

# another example of while statement
z = 0
while z < 3:
    print("z is:", z)
    z += 1

# for statement: The for statement is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
# Example:
for i in range(5):
    print("i is:", i)
