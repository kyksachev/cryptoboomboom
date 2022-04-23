posled = int(input())
even = 0
odd = 0
for i in range(posled):
    number = int(input())
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print ("chet -", odd, "nechet -", even)
