class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        while True:
            for i in range(len(s)-1, 0, -1):
                j = i-1
                curr = s[i]
                last = s[i]
                tobreak = False
                while j >= 0:
                    if s[j] == curr:
                        #print i, j, last, curr
                        if last == curr:
                            s = s[0:j]+s[j+1:]
                        elif last > curr:
                            s = s[0:i]+s[i+1:]
                        elif last < curr:
                            s = s[0:j]+s[j+1:]
                        tobreak = True
                        #print i,j, s
                        break
                    else:
                        last = s[j]
                        j -= 1
                if tobreak:
                    break
            else:
                break
        return s

s = Solution()
print s.removeDuplicateLetters('bcabc')
print s.removeDuplicateLetters('cbacdcbc')


