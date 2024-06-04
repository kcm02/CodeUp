n = int(input())
n_list = list(map(int,input().split()))
n_list.reverse()

for i in n_list:
    print(i, end=' ')
