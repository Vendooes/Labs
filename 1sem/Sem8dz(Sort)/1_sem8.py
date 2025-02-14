seq = input().split()
fir = 0
sec = 1
for i in range(len(seq)):
    fir = 0
    sec = 1
    for q in range(len(seq)):
        if sec<len(seq) and fir<len(seq) and seq[sec]<seq[fir]:
            seq[fir],seq[sec] = seq[sec],seq[fir]
        fir+=1
        sec+=1
print(' '.join(seq))