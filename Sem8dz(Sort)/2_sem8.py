# seq = input().split()

# def sort(seq):

#     med = int((len(seq)-1)//2)
#     medi = int(seq[med])
#     if len(seq)<2:
#         return seq
#     else:
#         mini = []
#         ser = []
#         big = []
#         for i in seq:
#             if int(i)<medi:
#                 mini.append(int(i))
#             if int(i) == medi:
#                 ser.append(int(i))
#             if int(i)>medi:
#                 big.append(int(i))
#         return sort(mini) + ser + sort(big)
# print(sort(seq))

seq = input("Введите числа через пробел: ").split()

def sort(seq):
    if len(seq) < 2:
        return seq

    # Преобразуем строковые значения в целые числа
    seq = list(map(int, seq))
    
    med_index = (len(seq) - 1) // 2
    medi = seq[med_index]

    mini = []
    ser = []
    big = []

    for i in seq:
        if i < medi:
            mini.append(i)
        elif i == medi:
            ser.append(i)
        else:
            big.append(i)

    return sort(mini) + ser + sort(big)

print(sort(seq))
