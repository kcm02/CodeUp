a,b,c = map(int,input().split())
print(c) if c<(a if a<b else b) else print(a if a<b else b)
