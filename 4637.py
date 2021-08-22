n = 10000
print_output = list(map(int, range(1, 1+n)))

for j in range(1, n+1):
    strn = list(str(j))
    for i in strn:
        j += int(i)
    if j in print_output:
        print_output.remove(j)

for x in print_output:
    print(x)