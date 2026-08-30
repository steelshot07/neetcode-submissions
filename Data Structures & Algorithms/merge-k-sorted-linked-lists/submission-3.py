import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        # Put first node of every list into heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next