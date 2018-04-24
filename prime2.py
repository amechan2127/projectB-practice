num = int(input('input>> '))
 
num_list = [x for x in range(2, num + 1)]
sosu = []
i = 0
while i * i < num:
    sosu.append(num_list[0])
    p = sosu[-1]
    num_list = [x for x in num_list if x % p != 0]
    i += 1
sosu += num_list
print(sosu)
if sosu[-1] == num:
    print(str(num) + 'は素数です')
else:
    print(str(num) + 'は素数ではないです')