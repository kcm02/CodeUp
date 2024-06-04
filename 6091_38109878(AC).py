a,b,c = map(int,input().split())
n = max(a,b,c)

while not (n % a == 0 and n % b == 0 and n % c == 0):
    n += 1

print(n)
