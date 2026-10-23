class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        temp=""
        for i in range(0,len(path)+1):
            if i<len(path) and path[i]!="/":
                temp+=path[i]
            else:
                if temp=="" or temp==".":
                    pass
                elif temp=="..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(temp)
                temp=""




        list=[]
        for char in stack:
            list.append('/'+char)

        if len(list)==0:
            return '/'

        return "".join(list)
