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