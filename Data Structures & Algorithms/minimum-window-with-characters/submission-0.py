class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        l,r = 0, 0
        frequency = {}
        window = {}
        for char in t:
            frequency[char] = frequency.get(char, 0) + 1

        need = len(frequency)
        have = 0
        best = ""
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            #if char in s, is in t and it matches the frequency then its added to have count
            if char in frequency and window[char] == frequency[char]:
                have += 1
            while have == need:
                #updating best to store smallest valid window
                if not best or r - l + 1 < len(best):
                    best = s[l:r+1]
                left = s[l]
                window[left] -= 1 #updating window dictionary
                if left in frequency and window[left] < frequency[left]:
                    have -= 1
                l += 1
            r += 1
        return best