#/usr/bin/env python

def getDivisor(num):
    divisorList = []
    for i in range(1, num//2+1):
        if num % i == 0:
            divisorList.append(i)

    return divisorList

if __name__ == '__main__':
    print(getDivisor(220))
