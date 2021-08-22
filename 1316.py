N = int(input())
word_count = 0
str_TF = []
for x in range(N):
    str_input = list(str(input()))
    str_TF = []
    for index in range(len(str_input)-1) :
        if str_input[index] != str_input[index+1]: 
            str_next = str_input[index+1: ]
            if str_next.count(str_input[index]) > 0 :
                str_TF.append(False)
    if str_TF.count(False) !=0:
        N -=1
print(N)