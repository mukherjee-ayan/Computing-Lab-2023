n = int(input("Enter n: "))

sieve = [True] * (n+1)
values = []
i = 2

while i*i <= n:
    if sieve[i]:
        for j in range(i*i,n+1,i):
            sieve[j] = False
    i += 1        

for i in range(1,n+1):
    if sieve[i]:
        values.append(i)

p = n // 2

for i in range(p):
    for j in range(p, p-i-1, -1):
        print(values[j], end="")
    for j in range(n-i-i-2):
        print(values[p-i], end="")
    for j in range(p-i, p+1):
        print(values[j], end="")
    print("\n")
    
for i in range(p,-p-1,-1):
    print(values[abs(i)], end="")
print("\n")

for i in range(p-1, -1, -1):
    for j in range(p, p-i-1, -1):
        print(values[j], end="")
    for j in range(n-i-i-2):
        print(values[p-i], end="")
    for j in range(p-i, p+1):
        print(values[j], end="")
    print("\n")
