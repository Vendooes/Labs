s = input()

def hashx(s):
    pref = []
    for i in range(len(s)):
        pref.append(s[i:])
    pref.sort()

    fin = len(pref[0])
    for i in range(1, len(s)):

        mini = min(len(pref[i]), len(pref[i-1]))
        result =mini 
        for j in range(mini):
            if pref[i][j] != pref[i-1][j]:
                result = j
                break

        longp = result
        fin += len(pref[i]) - longp
    return fin
print(hashx(s))
