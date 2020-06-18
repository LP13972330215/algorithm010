class Solution(object):
    def hasCycle(self, head):
        """
        TODO：给定一个链表，判断链表中是否有环。为了表示给定链表中的环，
        我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1，则在该链表中没有环。
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        # if not head：  # 没必要这样写可以加入while循环判断更简洁
        #     return False

        while fast and fast.next:  # 防止head为空和出现空指针的next的情况
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


