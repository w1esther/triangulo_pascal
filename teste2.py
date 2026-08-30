
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

#     somatorio = 0
#     print(f'{m}\n{n}')
#     while somatorio < x - 2:
#         soma_anteriores = m + n

#         print(soma_anteriores)

#         n = m

#         m = soma_anteriores

#         somatorio += 1  


print(fibo(6))