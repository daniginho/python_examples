###############################
# asking a question that goes with the array
###############################
#note int changes the string to a integer


# square brackets = empty array so you can store the numbers
a = []

d = int(input("How many numbers are there?"))

###############################
#append it adds a value to the end of a array
###############################

for i in range(d):
    c  = int(input("Enter a number:"))
    a.append(c)

result = 0
for i in range(len(a)):
    result = result + a[i]
print(result)

