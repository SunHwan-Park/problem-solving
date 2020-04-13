class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt
 
class LinkedList:
    def __init__(self, val=None):
        if val == None:
            self.head = val
            self.tail = val
        else:
            new = Node(val)
            self.head = new
            self.tail = new
     
    def insert(self, idx, val):
        # 추가할 인덱스 위치의 노드 찾기
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            raise IndexError
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
        new = Node(val) # 새로 추가할 노드
        if idx == 0:    # 맨 앞에 추가
            curr.pre = new
            new.nxt = curr
            self.head = new
        else:
            # 앞 노드와 새 노드 연결
            node_front = curr.pre
            node_front.nxt = new
            new.pre = node_front
            # 새 노드와 현재 노드 연결
            new.nxt = curr
            curr.pre = new
 
    def append(self, val):
        curr = self.tail
        new = Node(val)
        if curr == None:
            self.head = new
        else:
            curr.nxt = new
            new.pre = curr
        self.tail = new
     
    def index(self, idx):
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            raise IndexError
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
        return curr.val
 
    def __repr__(self):
        result = '['
        curr = self.head
        while curr.nxt:
            result += str(curr.val) + ', '
            curr = curr.nxt
        result += ']'
        return f'{result}'
 
 
t = int(input())
for test_case in range(1, t+1):
    n, m, l = map(int, input().split())
    data = list(map(int, input().split()))
    # linked-list 만들기
    link = LinkedList()
    for datum in data:
        link.append(datum)
    for _ in range(m):
        idx, num = map(int, input().split())
        # linked-list에 삽입
        link.insert(idx, num)
    result = link.index(l)
    print('#{} {}'.format(test_case, result))