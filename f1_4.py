def prime(numbers):
    p=[]
    for n in numbers:
        if n > 1:
            for i in range(2, n):
                if (n % i == 0):
                    break
            else:
                p.append(n)
    print(p)
nums=input()
numbers=[]
for n in nums.split():
    numbers.append(int(n))
prime(numbers)