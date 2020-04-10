import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCnt = 0
      
    def append(self, node):
        cursor = self.tail
        if cursor == None:
            self.head = node
        else:
            cursor.next = node
            node.prev = cursor
        self.tail = node
        self.nodeCnt += 1

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    LL = LinkedList()
    for i in range(N):
        LL.append(Node(arr[i]))

    LL.head.prev = LL.tail
    LL.tail.next = LL.head

    insert_idx = M
    cursor = LL.head
    for _ in range(K):
        for _ in range(M):
            cursor = cursor.next
        new = Node(cursor.prev.value + cursor.value)
        new.prev = cursor.prev
        cursor.prev.next = new
        new.next = cursor
        cursor.prev = new
        cursor = new
        LL.nodeCnt += 1

    print('#{}'.format(tc), end=' ')
    current = LL.head.prev
    for _ in range(min([LL.nodeCnt, 10])):
        print(current.value, end=' ')
        current = current.prev
    print()