﻿n = int(input())
sum = 0
i = 1

while(True):
    sum += i
    if sum >= n:
        print(sum)
        break
    i += 1
