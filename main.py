


def create_array():
    a =[]
    while True:
        c  = int(input("Enter a number:"))
        if c == 0:
            break
        a.append(c)
    return a

def sum_array(p):
    result = 0
    for i in range(len(p)):
        result = result + p[i]
    return result

def multiply_array(m):
    result = 1
    for i in range(len(m)):
        result =result * m[i]
    return result


m = create_array()
print(multiply_array(m))



