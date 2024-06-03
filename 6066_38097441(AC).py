a,b,c = map(int,input().split(' '))
str = (a,b,c)

for s in str:
    if s % 2 == 0:
        print("even")
    else:
        print("odd")
