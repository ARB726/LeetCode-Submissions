class Node:
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.hashMap:
            node =self.hashMap[key]
            self.DeleteNode(node)
            self.addAfterHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self.DeleteNode(node)
            self.addAfterHead(node)

        else:

            node = Node(key,value)
            self.hashMap[key] = node
            self.addAfterHead(node)

            if len(self.hashMap) > self.capacity:
                lru = self.tail.prev
                self.DeleteNode(lru)
                del self.hashMap[lru.key]            

    
    def addAfterHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def deleteAfterHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def DeleteNode(self,node):
        Prev = node.prev
        Next = node.next
        Prev.next = Next
        Next.prev = Prev


    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)