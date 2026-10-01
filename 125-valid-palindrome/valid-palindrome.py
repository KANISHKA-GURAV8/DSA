class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sentence=re.sub(r"[^\w]","",s).replace("_","")
        sentences=sentence.lower()
        i=0
        j=len(sentences)-1
        while i<=j:
            if sentences[i]!=sentences[j]:
                return False
            else:
                i+=1
                j-=1
        return True

        