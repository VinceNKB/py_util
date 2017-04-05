#!/usr/bin/env python3

def manacher(s):
    s = '#'.join('^{}$'.format(s))
    mx = 0
    index = -1
    P = [0] * len(s)
    for i in range(1, len(s)-1):
        if mx > i:
            j = 2*index-i
            if P[j] > mx-i:
                P[i] = mx-i
            else:
                P[i] = P[j]
        while s[i+P[i]+1] == s[i-P[i]-1]:
            P[i] += 1
        if i + P[i] > mx:
            mx = i + P[i]
            index = i

    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[centerIndex - maxLen: centerIndex + maxLen + 1].replace('#', '')


print(manacher('abababa'))




