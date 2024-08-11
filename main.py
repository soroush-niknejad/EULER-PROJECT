def multipleof3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
sum = 0
for i in range(1,1000):
    if multipleof3or5(i)==True:
        sum +=i
print(sum)
