A = [6, 2, 3, 9, 10, 1, 4, 7, 8, 5]

def Quicksort(A):
    if len(A) <= 1:
        return A
    reference = A[len(A) // 2]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]
    return Quicksort(small) + equal + Quicksort(big)

B = Quicksort(A)
print(B)
