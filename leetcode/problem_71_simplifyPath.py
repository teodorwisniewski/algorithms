


# class Solution:
#     def simplifyPath(self, path: str) -> str:
        
        

#         def is_valid_token(token: str) -> bool:
#             return len(token) > 0 and token != "."
        
#         tokens = filter(is_valid_token, path.split("/"))

#         stack = []

#         for token in tokens:
#             if token == "..":
#                 if stack:
#                     stack.pop()
                
#             else:
#                 stack.append(token)
#         if not stack:
#             return "/"
#         return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        tokens = path.split("/")

        stack = []

        for token in tokens:
            if token == "..":
                if stack:
                    stack.pop()

            elif len(token) > 0 and token != ".":
                stack.append(token)
            
                
        if not stack:
            return "/"
        return "/" + "/".join(stack)