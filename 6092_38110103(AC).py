n = int(input())
list = list(map(int,input().split()))
student = [i for i in range(1,24)]
count = [0 for _ in range(23)]

for i in list:
    for j in student:
        if i == j:
            count[j-1] += 1

for i in count:
    print(i, end=' ')
