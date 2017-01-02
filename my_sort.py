#!/usr/bin/env python3
import math

def counting_sort(array, k):
    """
    :param array: list[int] or list[(int, ...)] unsorted-array
    :param k: int size of extra space
    :return: list[int] or list[(int, ...)] sorted-array
    """

    temp = [0] * k
    result = [0] * len(array)

    if isinstance(array[0], int): #根据是否附带卫星数据分情况
        for i in range(len(array)):
            temp[array[i]] += 1

        for i in range(1, k):
            temp[i] = temp[i] + temp[i-1]

        for i in range(len(array)):
            result[temp[array[i]]-1] = array[i] #这里-1是因为在temp中index最小是1。0是没有的意思，不是index为0的意思
            temp[array[i]] -= 1

    else:
        for i in range(len(array)):
            temp[array[i][0]] += 1

        for i in range(1, k):
            temp[i] = temp[i] + temp[i-1]

        for i in range(len(array))[::-1]: #倒序遍历以保证稳定
            result[temp[array[i][0]]-1] = array[i] #这里-1是因为在temp中index最小是1。0是没有的意思，不是index为0的意思
            temp[array[i][0]] -= 1

    return result

def radix_sort_10(array, d): # radix = 10
    """
    :param array: list[int] or list[(int, ...)] unsorted-array
    :param d: int the length of digit
    :return: list[int] or list[(int, ...)] sorted-array
    """


    if isinstance(array[0], int): #根据是否附带卫星数据分情况
        if d <= 0:
            maxNum = max(array)
            d = 0
            while maxNum > 1:
                maxNum //= 10
                d += 1

        base = 1
        for i in range(1, d+1):
            temp = [(x // base % 10, x) for x in array]
            array = [x[1] for x in counting_sort(temp, 10)] # 使用了上面的counting_sort
            base *= 10
    else:
        if d <= 0:
            maxNum = max([x[0] for x in array])
            d = 0
            while maxNum > 1:
                maxNum //= 10
                d += 1

        base = 1
        for i in range(1, d+1):
            temp = [(x[0]//base%10, x) for x in array]
            array = [x[1] for x in counting_sort(temp, 10)]
            base *= 10
    return array

def radix_sort(array, r):
    """
    :param array: list[int] or list[(int, ...)] unsorted-array
    :param r: int radix
    :return: list[int] or list[(int, ...)] sorted-array
    """


    if isinstance(array[0], int): #根据是否附带卫星数据分情况
        maxNum = max(array)
        b = 0
        while maxNum > 1:
            maxNum //= 2
            b += 1

        d = math.ceil(b/r)
        r = 2**r

        base = 1
        for i in range(1, d+1):
            temp = [(x//base%r, x) for x in array]
            array = [x[1] for x in counting_sort(temp, r)] # 使用了上面的counting_sort
            base *= r
    else:

        maxNum = max([x[0] for x in array])
        b = 0
        while maxNum > 1:
            maxNum //= 2
            b += 1

        d = math.ceil(b/r)
        r = 2**r

        base = 1
        for i in range(1, d+1):
            temp = [(x[0]//base%r, x) for x in array]
            array = [x[1] for x in counting_sort(temp, r)]
            base *= r
    return array


class ListNode(object):
        def __init__(self, val):
            self.val = val
            self.next = None

def bucket_sort(array):
    """
    :param array: list[float] or list[(float, ...)] unsorted-array
    :return: list[float] or list[(float, ...)] sorted-array
    """
    n = len(array)
    linkArray = [ListNode(-1) for i in range(n)]
    result = []

    if isinstance(array[0], int): #根据是否附带卫星数据分情况
        for i in range(n):
            index = math.floor(n * array[i])
            newNode = ListNode(array[i])
            cur = linkArray[index]
            while cur.next:
                if cur.next.val >= array[i]:
                    newNode.next = cur.next
                    cur.next = newNode
                    break
                cur = cur.next
            else:
                cur.next = newNode

        for i in range(len(linkArray)):
            if linkArray[i].next:
                cur = linkArray[i].next
                while cur:
                    result.append(cur.val)
                    cur = cur.next
    else:
        for i in range(n):
            index = math.floor(n * array[i][0])
            newNode = ListNode(array[i])
            cur = linkArray[index]
            while cur.next:
                if cur.next.val[0] >= array[i][0]:
                    newNode.next = cur.next
                    cur.next = newNode
                    break
                cur = cur.next
            else:
                cur.next = newNode

        for i in range(len(linkArray)):
            if linkArray[i].next:
                cur = linkArray[i].next
                while cur:
                    result.append(cur.val)
                    cur = cur.next

    return result

def bucket_sort_pretreatment(array):
    new_array = []

    if isinstance(array[0], int):
        maxNum = max(array)
        minNum = min(array)
        length = maxNum - minNum + 1
        new_array = [((x-minNum)/length, x) for x in array]
    else:
        maxNum = max([x[0] for x in array])
        minNum = min([x[0] for x in array])
        length = maxNum - minNum + 1
        new_array = [((x[0]-minNum)/length, x) for x in array]

    return new_array


if __name__ == '__main__':
    #print(counting_sort([(2,'a'),(5,'b'),(3,'c'),(1,'d'),(2,'e'),(3,'f'),(1,'g'),(3,'h')], 10))
    #print(radix_sort([(26,'a'),(51,'b'),(33,'c'),(1432,'d'),(122,'e'),(3,'f'),(13,'g'),(93,'h')], 3))
    #print(radix_sort([12,5332,52671,235,98,4,740], 3))
    #print(bucket_sort([(.1, 'a'), (.3, 'b'), (.5, 'c'), (.7, 'd'), (.35, 'e')]))
    print([x[1] for x in bucket_sort(bucket_sort_pretreatment([(1, 'a'), (3, 'b'), (5, 'c'), (7, 'd'), (3.5, 'e')]))])
    pass


