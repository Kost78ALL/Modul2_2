def result(n, res_Sp = None):
    if res_Sp == None:
        res_Sp = []
    for i in range(1,20):
        for j in range(1,20):
            if i == n or j == n:
                continue
            elif j in res_Sp:
                continue
            elif n % (i + j) == 0:
                #print(i,j)
                res_Sp.append(i),res_Sp.append(j)
    return res_Sp
n = int(input('Введите число от 3 до 20 -'))
print(*result(n), sep =',')