from operator import neg
from typing import List, Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:  
    return dfs(head)

# Time: O(n), Space: O(n)
def dfs(head):
    if not head:
        return False
    if not head.next:
        return False
    
    visited = set()
    stack = list()
    stack.append(head)

    while(stack):
        curr = stack.pop()
        visited.add(curr)

        if not curr:
            return False

        if curr in visited:
            return True
        else:
            stack.append(curr.next)

# Floyd's tortoise and hare algo, two pointers approach
# Time: O(n), Space: O(1)
def tortoise_and_hare(head):
    tortoise = head
    hare = head

    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise: 
            return True

    return False

zero = ListNode(0)
two = ListNode(2)
negfour = ListNode(-4)
three = ListNode(3)
three.next = two
two.next = zero
zero.next = negfour
negfour.next = two

head = three

print(hasCycle(head))
print(tortoise_and_hare(head))