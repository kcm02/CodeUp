w,h,b = map(int,input().split(' '))
n = (w*h*b)/8/1024

print(f"{format(float(n/1024),'.2f')} MB")
