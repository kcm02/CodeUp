n = input()

for i in range(15):
    result = int(n, 16) * (i + 1)
    print(f'{n}*{hex(i+1)[2:].upper()}={hex(result)[2:].upper()}')
