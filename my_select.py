#!/usr/bin/env python3
import random

def partition(A, p, r):
    i = p - 1
    j = p
    x = A[r]

    while j < r:
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1

    i += 1
    A[i], A[r] = A[r], A[i]
    return i

def random_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

# quick select
def random_selection(A, p, r, i):
    if p == r:
        return A[p]

    q = random_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return random_selection(A, p, q - 1, i)
    else:
        return random_selection(A, q+1, r, i - k)

'''
A = [4,2,3,8,6,7,1,5]
print(random_selection(A, 0, 7, 5))
print(A)
'''




