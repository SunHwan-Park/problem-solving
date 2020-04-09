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

    def delete(self, item):
        temp = self.head
        if temp == item:
            if temp.next:
                self.head = temp.next
                temp.next = None
            else:
                self.head = None
    
        else:
            while temp.next != item:
                temp = temp.next
            temp2 = temp.next
            temp.next = temp.next.next
            temp2.next = None

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
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    LL = LinkedList(Node(arr[0]))
    for i in range(1, N):
        LL.append(Node(arr[i]))
    cursor = LL.head
    while K:
        for _ in range(M-1):
            cursor = cursor.next
        temp = Node(cursor.value + cursor.next.value)
        temp.next = cursor.next
        cursor.next = temp
        cursor = temp
        K -= 1
        N += 1
        