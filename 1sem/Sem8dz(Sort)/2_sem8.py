seq = input().split()

def sort(seq):
    if len(seq) < 2:
        return seq

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
