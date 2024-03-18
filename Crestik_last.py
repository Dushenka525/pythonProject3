setka=[['*','*','*'],['*','*','*'],['*','*','*']]
k=0
count=0
symvol='x'
print('Перед вами сетка нужно ввести цифры,которы пересекаются с выбранной вами клеткой сначала выбираете строку на которой ваша клетка, а затем столбик.')
for i in range(9):
    print('', ' '.join(str(m) for m in ['', 0, 1, 2]))
    for i in setka:
        print(k,' '.join(str(m) for m in i))
        k += 1
    k=0
    if symvol=='x':
        print('Ходит, тот кто ставит крестик!')
        m,n=map(int,input('Ввести:').split())
        while 2 < m or m < 0 or 2 < n or n < 0:
            m, n = map(int, input('Ввести:').split())
        setka[m][n]=(symvol)

        if m + 1 <= 2:
            if setka[m][n] == setka[m + 1][n]:
                count += 1
        if m + 2 <= 2:
            if setka[m][n] == setka[m + 2][n]:
                count += 1
        if m - 1 >= 0:
            if setka[m][n] == setka[m - 1][n]:
                count += 1
        if m - 2 >= 0:
            if setka[m][n] == setka[m - 2][n]:
                count += 1

        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count = 0

        if (m == 0 and n == 0) or (m == 2 and n == 0) or (m == 2 and n == 0) or (m == 2 and n == 2):
            if m - 1 >= 0 and n - 1 >= 0:
                if setka[m][n] == setka[m - 1][n - 1]:
                    count += 1
            if m - 2 >= 0 and n - 2 >= 0:
                if setka[m][n] == setka[m - 2][n - 2]:
                    count += 1

            if m + 1 <= 2 and n + 1 <= 2:
                if setka[m][n] == setka[m + 1][n + 1]:
                    count += 1
            if m + 2 <= 2 and n + 2 <= 2:
                if setka[m][n] == setka[m + 2][n + 2]:
                    count += 1

        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count = 0

        if n + 1 <= 2:
            if setka[m][n] == setka[m][n + 1]:
                count += 1
        if n + 2 <= 2:
            if setka[m][n] == setka[m][n + 2]:
                count += 1
            if count == 2:
                print('Выйграл кто играл за', symvol)
        if n - 1 >= 0:
            if setka[m][n] == setka[m][n - 1]:
                count += 1
        if n - 2 >= 0:
            if setka[m][n] == setka[m][n - 2]:
                count += 1
        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count = 0

        symvol='o'

    else:
        print('Ходит, тот кто ставит нолик!')
        m,n=map(int,input('Ввести:').split())
        while 2 < m or m < 0 or 2 < n or n < 0:
            m, n = map(int, input('Ввести:').split())
        setka[m][n]=(symvol)
        if m + 1 <= 2:
            if setka[m][n] == setka[m + 1][n]:
                count += 1
        if m + 2 <= 2:
            if setka[m][n] == setka[m + 2][n]:
                count += 1
        if m - 1 >= 0:
            if setka[m][n] == setka[m-1][n]:
                count += 1
        if m - 2 >= 0:
            if setka[m][n] == setka[m - 2][n]:
                count += 1

        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count=0

        if (m==0 and n==0) or (m==2 and n==0) or (m==2 and n==0) or (m==2 and n==2):
            if m - 1 >= 0 and n-1>=0:
                if setka[m][n] == setka[m-1][n-1]:
                    count += 1
            if m - 2 >= 0 and n-2>=0:
                if setka[m][n] == setka[m-2][n-2]:
                    count += 1

            if m + 1 <= 2 and n+1 <= 2:
                if setka[m][n] == setka[m+1][n+1]:
                    count += 1
            if m + 2 <= 2 and n+2 <= 2:
                if setka[m][n] == setka[m+2][n+2]:
                    count += 1


        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count = 0

        if n + 1 <= 2:
            if setka[m][n] == setka[m][n+1]:
                count += 1
        if n + 2 <= 2:
            if setka[m][n] == setka[m][n+2]:
                count += 1
            if count == 2:
                print('Выйграл кто играл за', symvol)
        if n - 1 >= 0:
            if setka[m][n] == setka[m][n-1]:
                count += 1
        if n - 2 >= 0:
            if setka[m][n] == setka[m][n-2]:
                count += 1
        if count == 2:
            print('Выйграл кто играл за', symvol)
            break
        count = 0

        symvol='x'
    # if m+1<=2:
    #     if setka[m][n]==setka[m+1][n]:
    #         count += 1
    # if m+2<=2:
    #     if setka[m][n] == setka[m + 2][n]:
    #         count +=1
    #     if count==2:
    #         print('Выйграл кто играл за', symvol)
k=0
if count==2:
    print('', ' '.join(str(m) for m in ['', 0, 1, 2]))
    for i in setka:
        print(k,' '.join(str(m) for m in i))
        k += 1
    print('Выйграл тот кто играл за',symvol)
else:
    print('Ничья')