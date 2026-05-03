class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        length = 0

        count = {}

        for end in range(0, len(s)):
            
            count[s[end]] = count.get(s[end], 0) + 1
            print(count)
            while count[s[end]] > 1:
                count[s[start]] -= 1
                start += 1           
            length = max(end-start+1, length)
        
        return length



        