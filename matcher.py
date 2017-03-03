#!/usr/bin/env python3

'''
算法        |   预处理时间   |   匹配时间
朴素算法    |   0           |   O((n-m+1)m)
Rabin-Karp  |   O(m)        |   O((n-m+1)m)
有限自动机   |   O(m|Sigma|) |   O(n)
KMP         |   O(m)        |   O(n)
'''

def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)

    match_pos = []
    for s in range(n-m+1):
        if P == T[s:s+m]:
            match_pos.append(s)

    return match_pos




def rabin_karp_matcher(T, P, q):
    d = 26
    n = len(T)
    m = len(P)
    h = d ** (m - 1) % q
    p = 0
    t = 0
    match_pos = []

    for i in range(m):
        p = (d * p + ord(P[i]) - ord('a')) % q
        t = (d * t + ord(T[i]) - ord('a')) % q

    for s in range(n-m+1):
        if p == t:
            if P == T[s:s+m]:
                match_pos.append(s)
        if s < n - m:
            t = (d * (t - (ord(T[s])-ord('a')) * h) + (ord(T[s+m]) - ord('a'))) % q

    return match_pos





def KMP_matcher(T, P):
    n = len(T)
    m = len(P)
    match_pos = []
    pi = compute_prefix_function(P)
    print(pi)
    q = -1
    for i in range(n):
        while q >= 0 and P[q+1] != T[i]:
            q = pi[q]
        if P[q+1] == T[i]:
            q = q + 1
        if q == m-1:
            match_pos.append(i-m+1)
            q = pi[q]
    return match_pos

def compute_prefix_function(P):
    m = len(P)
    pi = [-1] * m
    k = -1
    for q in range(1, m):
        while k >= 0 and P[k+1] != P[q]:
            k = pi[k]
        if P[k+1] == P[q]:
            k = k + 1
        pi[q] = k
    return pi


if __name__ == '__main__':
    print(KMP_matcher('adasdfassadasadsad43adas', 'adas'))
