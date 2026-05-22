class ListNode(object):
    pass
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


"""
Approach:
- Traverse both linked lists together
- Add corresponding digits along with carry
- Create a new node for the current digit
- Update carry for the next iteration
- Continue until both lists and carry become empty

Example:
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4

Step 1:
2 + 5 = 7

Step 2:
4 + 6 = 10
digit = 0
carry = 1

Step 3:
3 + 4 + 1 = 8

Result:
7 -> 0 -> 8

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""
