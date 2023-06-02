sum = 0
num = 1

while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        sum = sum + num

    num = num + 1
print(sum)
