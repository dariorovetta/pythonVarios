
def primos(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

for i in range(1, 101):
    print(i, primos(i))


""" 
def primos(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True """
            


""" print("2" + str(primos(2)))
print("3" + str(primos(3)))
print("4" + str(primos(4)))
print("5" + str(primos(5)))
print("6" + str(primos(6)))
print("7" + str(primos(7)))
print("8" + str(primos(8)))
print("9" + str(primos(9))) """
