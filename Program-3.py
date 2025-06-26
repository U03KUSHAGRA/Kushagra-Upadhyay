a = int(input("Enter a: "))
if a % 2 == 0:
    a -= 1

odd_numbers = []
for i in range(1, 2*a, 2):
    odd_numbers.append(str(i))

print(", ".join(odd_numbers))
