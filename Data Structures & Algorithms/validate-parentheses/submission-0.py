class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        close={")":"(","]":"[","}":"{"}
        for c in s:
            if c in close:
                if stk and stk[-1]==close[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False

        