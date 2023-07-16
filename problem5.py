def LCM():
    multiple = 20
    sum = 0

    while sum == 0:
        found = True
        for num in range(11, 21):
            if multiple % num != 0:
                found = False
                break

        if found:
            sum = multiple
        else:
            multiple += 20

    return sum

print(LCM())
