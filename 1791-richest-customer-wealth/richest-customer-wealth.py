class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # max_num=float('-inf')
        # for i in range(0,len(accounts)):
        #     sum_num=sum(accounts[i])
        #     max_num=max(sum_num,max_num)
        # return max_num

        max_sum=float('-inf')
        for i in range(0,len(accounts)):
            sum=0
            for j in range(0,len(accounts[i])):
                sum+=accounts[i][j]
            max_sum=max(sum,max_sum)
        return max_sum


        

