class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s:
            stack = []
            for x in s:
                if x == '(' or x =='{' or x =='[':
                    stack.append(x)
                elif x == ')' or x =='}' or x ==']':
                    if stack:
                        y = stack.pop()
                        if x ==')':
                            if y == '(':
                                continue
                            else:
                                return False
                        elif x =='}':
                            if y == '{':
                                continue
                            else:
                                return False
                        else:
                            if y == '[':
                                continue
                            else:
                                return False
                    else:
                        return False
                else:
                    return True
            if len(stack) is 0:
                return True
            else:
                return False
                                       
        else:
            return True
        
