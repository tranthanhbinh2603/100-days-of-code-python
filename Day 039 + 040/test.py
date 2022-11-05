n = int(input('Nhap so sao toi da: '))
strtemp = ''
for i in range(1,n+1):
    for z in range(1,i+1):
        strtemp += '*'
    print(f'{strtemp}')
    strtemp = ''
for i in range(n-1, 0, -1):
    for z in range(1,i+1):
        strtemp += '*'
    print(f'{strtemp}')
    strtemp = ''