tabl_umnoj = [f'{j}x{i}={i*j}'
              for i in range(2,10)
              for j in range(2,10)
              ]
sch = 1
for i in tabl_umnoj:
    print(i, end = '\t')
    if sch == 8:
        print()
        sch = 1
    else:
        sch += 1