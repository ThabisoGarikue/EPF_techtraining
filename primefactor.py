def findLargePF(num):
    index = 2
    while index * index < num:
        if num % index :
            index = index + 1
        else:
            num = num / index
    return num
print(int(findLargePF(600851475143)))
