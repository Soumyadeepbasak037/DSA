class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck=[-1] # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                stck.pop()
                if not stck: # if popped -1, add a new start index (())
                    stck.append(i)
                else:
                    max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
        return max_length

###
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
        
#         prev_open_pos = 0
#         prev_close_pos = 0
        
#         req_len = 0
#         stack = []
#         for pos in range(len(s)):
#             if(s[pos] == "("):
#                  stack.append(pos)
#             elif s[pos] == ")":
#                 if stack:
#                     open_pos = stack.pop()
                    
#                     if (stack == [] or pos == len(s)-1):
#                         length = (pos-open_pos)+1
                    
#                         if(prev_close_pos + 1 == open_pos):
#                             req_len += length
#                         else:
#                             if(length > req_len):
#                                 req_len = length
                        
#                         prev_open_pos = open_pos
#                         prev_close_pos = pos

#         return req_len
    


ans = Solution()

print(ans.longestValidParentheses("(())"))
print(ans.longestValidParentheses("(()"))
print(ans.longestValidParentheses(")()())"))
print(ans.longestValidParentheses(""))
print(ans.longestValidParentheses("()(())"))
                