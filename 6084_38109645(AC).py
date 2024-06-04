h,b,c,s = map(int,input().split(' '))
n = (h*b*c*s)/8/1024

print(f"{format(float(n/1024),'.1f')} MB")
