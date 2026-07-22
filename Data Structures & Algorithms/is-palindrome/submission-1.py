class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use .isalnum() returns true or false
        s = s.lower()
        character_list = list(s)
        counter = 0
        s_alnum = []
        c1 = []
        c2 = []
        for char in character_list:
            if char.isalnum() == False:
                continue
            else:
                s_alnum.append(char)
            counter += 1
        
        if counter % 2 == 0:
            for i in range(0,counter//2):
                c1.append(s_alnum[i])
            for j in range(counter//2, counter):
                c2.append(s_alnum[j])
        else:
            for i in range(0,(counter-1)//2):
                c1.append(s_alnum[i])
            for j in range((counter+1)//2, counter):
                c2.append(s_alnum[j])

        c2.reverse()
        if c1 == c2:
            return True
        else:
            return False
