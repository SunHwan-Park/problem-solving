import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, item):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = item
            
    def insert(self, item, position):
        temp = self.head
        if position == 0:
            item.next = temp
            self.head = item
        else:
            while position > 1:
                temp = temp.next
                position -= 1
            temp2 = temp.next
            temp.next = item
            item.next = temp2

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    LL = LinkedList(Node(arr[0]))
    for i in range(1, N):
        LL.append(Node(arr[i]))

    for _ in range(M):
        idx, value = map(int, input().split())
        LL.insert(Node(value), idx)

    current = LL.head
    for i in range(L):
        current = current.next
    
    print('#{} {}'.format(tc, current.value))