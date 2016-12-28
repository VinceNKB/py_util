#/usr/bin/env python

def getDivisor(num):
    "求num的因数，从小到大输出到divisorList中"
    divisorList = []

    for i in range(1, num//2+1):
        if num % i == 0:
            divisorList.append(i)

    return divisorList



if __name__ == '__main__':
    print(getDivisor(220))
