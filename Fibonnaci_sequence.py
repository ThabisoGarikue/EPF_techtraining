var1 = 0
var2 = 1
temp = 1 
sum = 0

while sum < 4000000:
    temp = var1 + var2

    var1 = var2
    var2 = temp

    if temp % 2 == 0:
        sum = sum + temp
print(sum)