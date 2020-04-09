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

    def size(self):
        count = 0
        current = self.head
        while current.next != None:
            current = current.next
            count += 1
        count += 1
        return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    LL = LinkedList(Node(arr[0]))
    for i in range(1, len(arr)):
        LL.append(Node(arr[i]))
    
    for _ in range(M-1):
        temp = list(map(int, input().split()))
        LL_tmp = LinkedList(Node(temp[0]))
        for i in range(1, len(temp)):
            LL_tmp.append(Node(temp[i]))
        
        LL_tmp_tail = LL_tmp.head
        for _ in range(LL_tmp.size()-1):
            LL_tmp_tail = LL_tmp_tail.next

        if LL.head.value > LL_tmp.head.value:
            LL_tmp_tail.next = LL.head
            LL = LL_tmp
        else:
            current = LL.head
            for _ in range(LL.size()-1):
                if current.next.value > LL_tmp.head.value:
                    tail_f = current.next
                    current.next = LL_tmp.head
                    LL_tmp_tail.next = tail_f
                    break
                else:
                    current = current.next
            else:
                current.next = LL_tmp.head

    result = []
    current = LL.head    
    for _ in range(LL.size()):
        result.append(current.value)
        current = current.next
    
    print('#{} {}'.format(tc, ' '.join(map(str, reversed(result[-10:])))))