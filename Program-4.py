list = eval(input("Enter list : "))
result = {}

for i in range(1, 10):
    count = 0
    for item in list:
        if item % i == 0:
            count += 1
    result[i] = count

print(result)
