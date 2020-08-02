#！/usr/bin/python3
#Author:pliu

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部(变成最新访问的)，所以定义一个方法
    def move_node_to_header(self, key):

        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def add_node_to_header(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new

    def pop_tail(self):
        last_node = self.tail.prev
        # 去掉链表尾部的节点在哈希表的对应项
        self.hashmap.pop(last_node.key)
        # 去掉最久没有被访问过的节点，即尾部Tail之前的一个节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到头部（变成最新访问的）
            self.move_node_to_header(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:

            self.hashmap[key].value = value
            self.move_node_to_header(key)
        else:
            if len(self.hashmap) >= self.capacity:
                self.pop_tail()
            self.add_node_to_header(key, value)

if __name__ == "__main__":
    # n1 = ListNode("a",1)
    # n2 = ListNode("b",2)
    # n3 = ListNode("c",3)
    # n4 = ListNode("d",4)
    lru = LRUCache(100)
    lru.put("a",1)
    lru.put("b",2)
    lru.put("c",3)
    lru.put("d",4)
    lru.put("a",11)
    print(lru.get("a"))

