class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        line_list=s.split()
        final_list=[]
        for char in range(len(line_list)-1,-1,-1):
            final_list.append(line_list[char])
        return " ".join(final_list)
        


        