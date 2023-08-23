n = int(input("Enter n: ").strip())
res = 0;

while n:
    n //= 5;
    res += n
    
print(res)
