def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True

a = int(input())
b = 0
isOn = True
while isOn:
    b+=1
    if isPrime(a + b):
        print(a+b)
        isOn=False