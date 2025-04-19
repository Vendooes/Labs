def z_function(s):
    long = len(s)
    z_f = [0]*long
    left_f,right_f = 0,0
    for i in range(1,long):
        z_f[i] = max(0,min(right_f-i,z_f[i-left_f]))
        while i+z_f[i]<long and s[z_f[i]]==s[i+z_f[i]]:
            z_f[i]+=1
        if i+z_f[i]>right_f:
            left_f=i
            right_f=i+z_f[i]
    return z_f
s = input()
print(z_function(s))