def squares(n):
    for i in range(1, n+1):
        yield pow(i, 2)

n = int(input())
for i in squares(n):        
    print(i)