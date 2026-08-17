class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_num=float('-inf')
        for i in range(0,len(accounts)):
            # sum=accounts[i][i]+accounts[i][i+1]
            sum_num=sum(accounts[i])
            max_num=max(sum_num,max_num)
        return max_num

        

