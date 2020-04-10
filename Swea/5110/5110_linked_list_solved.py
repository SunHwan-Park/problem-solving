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

    def index(self, idx):
        if self.nodeCnt == 0:
            raise IndexError
        elif idx >= 0: # 양수 인덱싱
            cursor = self.head
            for _ in range(idx):
                if cursor.next == None:
                    raise IndexError
                cursor = cursor.next
            return cursor
        else: # 음수 인덱싱
            cursor = self.tail
            for _ in range(abs(idx)-1):
                if cursor.prev == None:
                    raise IndexError
                cursor = cursor.prev
            return cursor
      
    def append(self, node):
        cursor = self.tail
        if cursor == None:
            self.head = node
        else:
            cursor.next = node
            node.prev = cursor
        self.tail = node
        self.nodeCnt += 1

    def insert(self, idx, node):
        if idx in [0, -(self.nodeCnt + 1)]: # 첫 요소로 들어갈 때
            if self.nodeCnt == 0:
                self.head = node
                self.tail = node
            else:
                cursor = self.head
                cursor.prev = node
                node.next = cursor
                self.head = node
        elif idx in [-1, (self.nodeCnt)]: # 마지막 요소로 들어갈 때
            if self.nodeCnt == 0:
                self.head = node
                self.tail = node
            else:
                cursor = self.tail
                cursor.next = node
                node.prev = cursor
                self.tail = node
        elif idx > 0: # 양수 인덱스 일때
            cursor = self.index(idx)    
            node.prev = cursor.prev
            cursor.prev.next = node
            cursor.prev = node
            node.next = cursor
        else: # 음수 인덱스 일때
            cursor = self.index(idx)    
            node.next = cursor.next
            cursor.next.prev = node
            node.prev = cursor
            cursor.next = node
        self.nodeCnt += 1

    def delete(self, node):
        cursor = self.index(node)
        cursor.prev.next = cursor.next
        cursor.next.prev = cursor.prev
        self.nodeCnt -= 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    LL = LinkedList()
    for i in range(N):
        LL.append(Node(arr[i]))
    
    for _ in range(M-1):
        arr = list(map(int, input().split()))
        LL_tmp = LinkedList()
        for i in range(len(arr)):
            LL_tmp.append(Node(arr[i]))
        
        insert_idx = LL.nodeCnt
        for i in range(LL.nodeCnt):
            if LL.index(i).value > arr[0]:
                insert_idx = i
                break
        
        if insert_idx == LL.nodeCnt:
            LL.tail.next = LL_tmp.head
            LL_tmp.head.prev = LL.tail
            LL.tail = LL_tmp.tail
            LL.nodeCnt += len(arr)
        elif insert_idx == 0:
            LL_tmp.tail.next = LL.head
            LL.head.prev = LL_tmp.tail
            LL_tmp.tail = LL.tail
            LL_tmp.nodeCnt += LL.nodeCnt
            LL = LL_tmp
        else:
            temp = LL.index(insert_idx)
            temp.prev.next = LL_tmp.head
            LL_tmp.head.prev = temp.prev
            temp.prev = LL_tmp.tail
            LL_tmp.tail.next = temp
            LL.nodeCnt += len(arr)

    print('#{}'.format(tc), end=" ")
    current = LL.tail
    for _ in range(10):
        print(current.value, end=" ")
        current = current.prev
    print()