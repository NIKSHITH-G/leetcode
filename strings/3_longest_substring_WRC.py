class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = set()

        left = 0
        max_len = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len


"""
Approach:
- Use a sliding window with two pointers
- 'left' represents the start of the window
- 'right' represents the end of the window
- Use a set to store unique characters in the current window
- If duplicate character appears:
    - remove characters from the left side
    - move left pointer forward
- Update maximum substring length each time

Example:
s = "abcabcbb"

Window Process:

a -> length = 1
ab -> length = 2
abc -> length = 3

Next character = a (duplicate)
Remove old 'a'
Window becomes "bca"

Continue until end

Longest substring = "abc"
Answer = 3

Time Complexity: O(n)
Space Complexity: O(n)
"""